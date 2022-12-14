from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Course
from accounts.models import UserCourse, Student, ErasmusUser, Coordinator, BoardMember
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import ToDoForm

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
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        # get which user wants to add an approved course ?
        if Student.objects.filter(name=erasmus_user.name).exists():
            todo_user = Student.objects.get_object_or_404(user=erasmus_user)
        elif Coordinator.objects.filter(name=erasmus_user.name).exists():
            todo_user = Coordinator.objects.get_object_or_404(user=erasmus_user)
        elif BoardMember.objects.filter(name=erasmus_user.name).exists():
            todo_user = BoardMember.objects.get_object_or_404(user=erasmus_user)
        else:
            todo_user = None

        username = request.user.username

        new_todo = None

        todo_form = ToDoForm()

        return render(request,
                      'accounts/add_todo.html',
                      {'new_todo': new_todo,
                       'todo_form': todo_form,
                       'username': username})
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
        return render(request, 'accounts/todo.html', context)

class DeleteToDoView(View):
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


<<<<<<< Updated upstream
class StarToDo(View): # ! changed the name from flag to star
=======
class AddUnapprovedCourse(LoginRequiredMixin, View): # ? Form required

    def get(self, request):
        username = request.user.username

        new_course = None

        course_form = CourseForm()

        return render(request,
                      'courses/add_unapproved_course.html',
                      {'new_course': new_course,
                       'course_form': course_form,
                       'username': username})

class FlagToDo(View):
>>>>>>> Stashed changes
    '''
    is_flagged : boolean, whether the todo should be starred
    '''
    def get(self, request, todo_id, is_flagged):
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

        todo.is_flagged = is_flagged
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
    def post(self, request):
        searched = request.POST.get('searched', False)

        # search for the query in the todo's header and body
        todo = ToDo.objects.filter(Q(header__contains=searched) | Q(body__contains=searched))

        return render(request, 'accounts/todo_search.html', {'searched': searched, "todo": todo})

    def get(self, request):
        return render(request, 'accounts/todo_search.html')

