from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include


urlpatterns = [
    path('accounts/profile/', views.HomeView.as_view(),  name="profile"),
    path('add-todo/', views.DeleteToDoView.as_view(),  name="add-todo"),
    path('delete-todo/<int:todo_id>/', views.DeleteToDoView.as_view(),  name="delete-todo"),
    path('todo-state/<int:todo_id>/<int:is_done>/', views.UpdateToDoStateView.as_view(),  name="todo-state"),
    path('flag-todo/<int:todo_id>/<int:is_flagged>/', views.FlagToDoView.as_view(),  name="flag-todo"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:student_id>', views.StudentProfilesView.as_view(), name="student-profile"),
]
