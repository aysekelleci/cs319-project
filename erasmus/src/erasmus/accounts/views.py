from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from courses.models import Course, Document
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator, BoardMember, ToDo
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import ToDoForm

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
                      'accounts/add_todo.html',
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
                new_todo.user = erasmus_user
                new_todo = todo_form.save(commit=False)
                new_todo.save()

        context = {'user': erasmus_user, 'todo_form': todo_form, 'new_todo' : new_todo}
        return render(request, 'accounts/add_todo.html', context)

class DeleteToDoView(LoginRequiredMixin,View):
    def get(self, request, todo_id):
        user = request.user
        todo_user = getUser(user)
        todo = get_object_or_404(ToDo, pk=todo_id)

        try:
            todo_item = ToDo.objects.get(user=todo_user, course=todo)  # control whether todo item already added
        except:
            todo_item = None
        if todo_item is not None:
            todo_item.delete()
            messages.info(request, "This todo removed the list.")
            return redirect("accounts/profile")


class FlagToDo(LoginRequiredMixin,View):

    '''
    is_flagged : boolean, whether the todo should be flagged
    '''
    def get(self, request, todo_id, is_flagged):
        user = request.user
        todo = get_object_or_404(ToDo, pk=todo_id)

        todo.is_flagged = is_flagged
        todo.save() # update the todo object
        return redirect("accounts/profile")

class UpdateToDoState(LoginRequiredMixin,View):

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
        # if visitor is Coordinator, add students courses, files
        documents = Document.objects.filter(user=student)
        courses = UserCourse.objects.filter(user=student)
        context = {'documents': documents, 'courses': courses, 'visitor': visitor, 'student': student}
        return render(request, 'accounts/student_profile.html', context)












"""
class SearchToDo(LoginRequiredMixin,View):
    def post(self, request):
        searched = request.POST.get('searched', False)

        # search for the query in the todo's header and body
        todo = ToDo.objects.filter(Q(header__contains=searched) | Q(body__contains=searched))

        return render(request, 'accounts/todo_search.html', {'searched': searched, "todo": todo})

    def get(self, request):
        return render(request, 'accounts/todo_search.html')
"""
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















