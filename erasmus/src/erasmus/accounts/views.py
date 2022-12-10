from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Course
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from courses.forms import CourseForm

from django.db.models import Q


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'courses/home.html')


class ToDo(View):
    def get(self, request):
        user = request.user
        todo = ToDo.objects.all()

        context = {'user': user, 'todo': todo}
        return render(request, 'accounts/todo.html', context) # ? supposed to be on the home page


class AddToDoView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(ToDo, pk=todo_id)  # Check whether given todo object exists
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        # get which user wants to add an approved course ?
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None

        # check whether todo item already added
        try:
            todo_item = ToDo.objects.get(user=todo_user,course=todo)
        except:
            todo_item = None

        if todo_item is not None:
            messages.info(request, "This todo already added to the todo list.")
            return redirect("/courses") # ?
        else:
            ToDo.objects.create(user=todo_user, course=todo)
            messages.info(request, "Todo added to your todo list.")
            return redirect("/courses") # ?


class DeleteCourseView(View):
    def get(self, request, todo_id):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        # get which user wants to add an approved course ?
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None
        todo = get_object_or_404(ToDo, pk=todo_id) # ? what if this gives an error

        try:
            todo_item = ToDo.objects.get(user=todo_user, course=todo)  # control whether todo item already added
        except:
            todo_item = None
        if todo_item is not None:
            todo_item.delete()
            messages.info(request, "This todo removed the list.")
            return redirect("/courses") # ?


class StarToDo(View): # ! changed the name from flag to star
    '''
    is_starred : boolean, whether the todo should be starred
    '''
    def get(self, request, todo_id, is_starred):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        # get which user wants to add an approved course
        # ? code below can be a function
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None
        todo = get_object_or_404(ToDo, pk=todo_id)  # ? what if this gives an error

        todo.is_starred = is_starred
        todo.save() # update the todo object


class UpdateToDoState(View):

    def get(self, request, todo_id, is_done):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        # get which user wants to add an approved course
        # ? code below can be a function
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None
        todo = get_object_or_404(ToDo, pk=todo_id)  # ? what if this gives an error

        todo.is_done = is_done
        todo.save()  # update the todo object


class SearchToDo(View):

    def get(self, request, query):
        user = request.user
        erasmus_user = ErasmusUser.objects.get(user=user)
        # get which user wants to add an approved course
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None

        # search for the query in the todo's header and body
        todo = ToDo.objects.get(Q(header__contains=query) | Q(body__contains=query))

        if todo is not None:
            return todo # ? how do we return

