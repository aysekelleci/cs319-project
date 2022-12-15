from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Course, Document, MergedCourse
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator, ToDo, BoardMember
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from courses.forms import CourseForm


# Create your views here.
class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user
        todo = ToDo.objects.all()
        erasmus_user = ErasmusUser.objects.filter(user=user).first()

        if Student.objects.filter(user=erasmus_user).exists():
            todo_user = Student.objects.filter(user=erasmus_user).first()
        elif Coordinator.objects.filter(user=erasmus_user).exists():
            todo_user = Coordinator.objects.filter(user=erasmus_user).first()
        elif BoardMember.objects.filter(user=erasmus_user).exists():
            todo_user = BoardMember.objects.filter(user=erasmus_user).first()
        else:
            todo_user = None

        context = {'user': todo_user, 'todo': todo}
        return render(request, 'courses/home.html', context)


class CourseView(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        if Coordinator.objects.filter(user=erasmus_user).first():
            user_type = "Coordinator"
        elif Student.objects.filter(user=erasmus_user).first():
            user_type = "Student"
        else:
            user_type = "Board Member"

        courses = Course.objects.all()

        context = {'user': user, 'courses': courses, "user_type": user_type}
        return render(request, 'courses/courses.html', context)


class AddCourseView(LoginRequiredMixin,View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)  # Check whether given course object exists
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.get(user=erasmus_user)  # get which student wants to add approved course
        try:
            course_item = UserCourse.objects.get(user=student,
                                                 course=course)  # control whether course item already added
        except:
            course_item = None
        if course_item is not None:
            messages.info(request, "This course already added to course list.")
            return redirect("/courses")

        else:
            course = UserCourse.objects.create(user=student, course=course)
            messages.info(request, "This course was added to your course list.")
            return redirect("/courses")


class DeleteCourseView(LoginRequiredMixin,View):
    def get(self, request, course_id):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.get_object_or_404(user=erasmus_user)  # get which student wants to add approved course
        course = get_object_or_404(Course, pk=course_id)

        try:
            course_item = UserCourse.objects.get(user=student, course=course)  # control whether course item already added
        except:
            course_item = None
        if course_item is not None:
            course_item.delete()
            messages.info(request, "This item removed from course list.")
            return redirect("/courses")


class AddUnapprovedCourse(LoginRequiredMixin, View):

    def get(self, request):
        username = request.user.username

        new_course = None

        course_form = CourseForm()

        return render(request,
                      'courses/add_unapproved_course.html',
                      {'new_course': new_course,
                       'course_form': course_form,
                       'username': username})

    def post(self, request):
        user = request.user
        username = user.username
        erasmus_user = ErasmusUser.objects.get(user=user)
        student = Student.objects.filter(user=erasmus_user).first()

        course_form = CourseForm(data=request.POST)
        if course_form.is_valid():
            # Create Comment object but don't save to database yet
            new_course = course_form.save(commit=False)

            # Save the comment to the database
            new_course.save()

            # add a todo item for the coordinator to evaluate the unapproved course
            coordinator_todo = ToDo(header=f"Evaluate new unapproved course of {erasmus_user.name}", user=student.coordinator.user,
                                    link="waiting-courses/")
            coordinator_todo.save()

        else:
            messages.info(request, "Course Form is not valid")
            return redirect("add_unapproved_course")

        return render(request,
                      'courses/add_unapproved_course.html',
                      {'new_course': new_course,
                       'course_form': course_form,
                       'username': username})


class DocumentView(LoginRequiredMixin,View):
    def get(self, request):
        documents = Document.objects.all()
        user = request.user

        context = {'documents': documents}
        return render(request, 'courses/documents.html', context)


class GetWaitingCoursesView(LoginRequiredMixin, View):
    def get(self, request):
        unapproved_courses = Course.objects.filter(approved=False)

        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            redirect('accounts/profile')

        else:
            context = {'coordinator': coordinator, 'unapproved_courses': unapproved_courses}
            return render(request, 'courses/waiting_courses.html', context)


class ApproveCoursesView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        unapproved_courses = Course.objects.filter(approved=False)

        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            redirect('accounts/profile')

        else:
            course = Course.objects.get_or_404(pk=course_id)
            if course is not None:
                course.approved = True

        redirect('waiting-courses')


class RejectCourseView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        unapproved_courses = Course.objects.filter(approved=False)

        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        if coordinator is None:
            redirect('accounts/profile')

        else:
            course = Course.objects.get_or_404(pk=course_id)
            if course is not None:
                # todo add the course to rejected course then delete it
                # course.delete()
                x = 5

        redirect('waiting-courses')

class MergeCourseView(LoginRequiredMixin, View):
    def get(self, request, course_type, bilkent_eq_id, course_id1, course_id2, course_id3, course_id4, course_id5,
            course_id6, course_id7, course_id8, course_id9, course_id10):

        if not Course.objects.filter(pk=course_id1).exists() and not Course.objects.filter(pk=course_id2).exists():
            # get the bilkent equivalent course
            bilkent_equivalent = Course.objects.filter(pk=bilkent_eq_id).first()

            # create a "parent" merged course instance
            merged_course = MergedCourse(course_type=course_type, bilkent_equivalent=bilkent_equivalent)
            merged_course.save()

            course_ids = [course_id1, course_id2, course_id3, course_id4, course_id5, course_id6, course_id7, course_id8,
                          course_id9, course_id10]

            # merge up to 10 courses by designating their parent course as the created MergedCourse instance
            for course_id in course_ids:
                course = Course.objects.filter(pk=course_id).first()
                if course is not None:
                    course.is_merged = True
                    course.merged_course = merged_course
                    course.save()

            return redirect("add_unapproved_course")
        else:
            messages.info(request, "You need to choose at least two courses to merge.")
            return redirect("add_unapproved_course")















