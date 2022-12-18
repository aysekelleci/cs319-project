from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from courses.models import Course, Document, MUST_COURSE, ELECTIVE_COURSE, PREAPPROVAL_FORM, STATIC_DOCUMENTS_FOLDER
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator, BoardMember, ToDo
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import ToDoForm, PhoneForm

from django.db.models import Q


# Create your views here.
class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()

        unflagged_todo = ToDo.objects.filter(user=erasmus_user, is_done=False, is_flagged=False)
        flagged_todo = ToDo.objects.filter(user=erasmus_user, is_done=False, is_flagged=True)
        done = ToDo.objects.filter(user=erasmus_user, is_done=True)

        if Student.objects.filter(user=erasmus_user).exists():
            todo_user = Student.objects.filter(user=erasmus_user).first()
        elif Coordinator.objects.filter(user=erasmus_user).exists():
            todo_user = Coordinator.objects.filter(user=erasmus_user).first()
        elif BoardMember.objects.filter(user=erasmus_user).exists():
            todo_user = BoardMember.objects.filter(user=erasmus_user).first()
        else:
            todo_user = None

        context = {'user': todo_user, 'unflagged_todo': unflagged_todo, 'flagged_todo': flagged_todo, 'done': done}
        return render(request, 'accounts/home.html', context)


class AddToDoView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        todo_user = getUser(user)

        username = request.user.username

        new_todo = None

        todo_form = ToDoForm()

        return render(request,
                      'accounts/add-todo.html',
                      {'new_todo': new_todo,
                       'todo_form': todo_form,
                       'username': username,
                       'todo_user': todo_user})
    def post(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            todo_form = ToDoForm(data=request.POST)
            new_todo = None

            if todo_form.is_valid():
                new_todo = todo_form.save(commit=False)
                new_todo.user = erasmus_user
                new_todo.save()

        context = {'user': erasmus_user, 'todo_form': todo_form, 'new_todo' : new_todo}
        messages.success(request, "Todo was added successfully")
        return redirect('/accounts/profile')

class DeleteToDoView(LoginRequiredMixin,View):
    def get(self, request, todo_id):
        try:
            todo_item = get_object_or_404(ToDo, pk=todo_id)
        except:
            todo_item = None
        if todo_item is not None:
            todo_item.delete()
            messages.info(request, "This todo removed from the list.")
            return redirect("/accounts/profile")


class FlagToDoView(LoginRequiredMixin,View):

    '''
    is_flagged : boolean, whether the todo should be flagged
    '''
    def get(self, request, todo_id, is_flagged):
        user = request.user
        todo = get_object_or_404(ToDo, pk=todo_id)

        todo.is_flagged = is_flagged
        todo.save() # update the todo object
        return redirect("/accounts/profile")

class UpdateToDoStateView(LoginRequiredMixin,View):

    def get(self, request, todo_id, is_done):
        user = request.user
        todo = get_object_or_404(ToDo, pk=todo_id)

        todo.is_done = is_done
        todo.save()  # update the todo object
        return redirect("/accounts/profile")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            student = Student.objects.filter(user=erasmus_user).first()
            courses = UserCourse.objects.filter(user=student)
            documents = Document.objects.filter(user=student)
            context = {'student': student, 'courses': courses, 'documents':documents}
            return render(request, 'accounts/profile.html', context)

        return redirect("/login")


class StudentProfilesView(LoginRequiredMixin, View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        visitor = None
        if erasmus_user is not None:
            visitor = Student.objects.filter(user=erasmus_user).first()
            if visitor is not None:
                context = {'visitor': visitor, 'student': student}
                return render(request, 'accounts/student_profile.html', context)

        visitor = Coordinator.objects.filter(user=erasmus_user).first()
        _courses_user = [user_course.course for user_course in UserCourse.objects.filter(user=student)]
        _merged_courses = {course.merged_course for course in _courses_user if course.is_merged is True}
        student_merged_course_dict = getMergedCoursesDict(_courses_user, _merged_courses)
        student_unmerged_courses = [course for course in _courses_user if course.is_merged is False]

        # if visitor is Coordinator, add students courses, files
        documents = Document.objects.filter(user=student)
        courses = UserCourse.objects.filter(user=student)
        context = {'documents': documents, 'courses': courses, 'visitor': visitor, 'student': student,
                   'student_unmerged_courses': student_unmerged_courses, 'student_merged_course_dict': student_merged_course_dict,
                   'MUST_COURSE': MUST_COURSE, 'ELECTIVE_COURSE': ELECTIVE_COURSE}
        return render(request, 'accounts/student_profile.html', context)

def getMergedCoursesDict(courses, merged_courses):
    merged_course_dict = {}
    for merged_course in merged_courses:
        one_merged_course_contents = []  # each list contains the courses composing one merged course
        for course in courses:
            if ( course.is_merged and (course.merged_course.pk is merged_course.pk) ):
                one_merged_course_contents.append(course)
        merged_course_dict[merged_course] = one_merged_course_contents
    return merged_course_dict

def getUser(user):
    erasmus_user = ErasmusUser.objects.filter(user=user).first()

    if Student.objects.filter(user=erasmus_user).exists():
        todo_user = Student.objects.filter(user=erasmus_user).first()
    elif Coordinator.objects.filter(user=erasmus_user).exists():
        todo_user = Coordinator.objects.filter(user=erasmus_user).first()
    elif BoardMember.objects.filter(user=erasmus_user).exists():
        todo_user = BoardMember.objects.filter(user=erasmus_user).first()
    else:
        todo_user = None

    return todo_user

'''

import pandas as pd
from django.contrib.auth.models import User
class PlacementView(LoginRequiredMixin, View):
    # read the placement table
    dataframe1 = pd.read_excel('book2.xlsx')
    # create students

    user = User(username="", password='')
    user.save()
    erasmus_user = ErasmusUser(user=user, name = '', email = '', bilkent_id = '', department = '')
    erasmus_user.save()
    student = Student(user=erasmus_user, gpa = '', score = '', status='', is_erasmus_done = False, academic_year = '', semester = '')

    # place students


    # send notification to students

class CancelPlacement(LoginRequiredMixin, View):
'''


class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            redirect("accounts/profile")

        else:
            students_of_cooordinator = Student.objects.filter(coordinator=coordinator)
            other_students = Student.objects.exclude(coordinator=coordinator)

            context = {"other_students": other_students, "students_of_coordinator": students_of_cooordinator}
            return render(request, "accounts/student_list.html", context)

        redirect("/login")



class ChangePhoneView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            phone_form = PhoneForm()

            new_phone = None

            return render(request,
                          'accounts/change_phone.html',
                          {'new_phone': new_phone,
                           'phone_form': phone_form,
                           'erasmus_user': erasmus_user})

    def post(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            phone_form = PhoneForm(data=request.POST)
            new_phone= None

            if phone_form.is_valid():
                erasmus_user.phone = phone_form

                erasmus_user.save()

                messages.success(request, 'phone number is updated')
                redirect('/accounts/profile')

            else:
                messages.error(request, 'form is not valid')
                return render(request, 'accounts/change_phone.html',
                              {'new_phone': new_phone, 'phone_form': phone_form, 'erasmus_user': erasmus_user})




















