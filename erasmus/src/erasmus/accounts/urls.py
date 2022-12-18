from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views
from django.urls import path, include


urlpatterns = [
    path('accounts/profile/', views.HomeView.as_view(),  name="profile"),
    path('add-todo/', views.AddToDoView.as_view(),  name="add-todo"),
    path('delete-todo/<int:todo_id>/', views.DeleteToDoView.as_view(),  name="delete-todo"),
    path('todo-state/<int:todo_id>/<int:is_done>/', views.UpdateToDoStateView.as_view(),  name="todo-state"),
    path('flag-todo/<int:todo_id>/<int:is_flagged>/', views.FlagToDoView.as_view(),  name="flag-todo"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('student-list/', views.StudentListView.as_view(), name= "student-list"),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html',
                                                                     success_url='done'), name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change.html'),
         name='password_change_done'),
    path('profile/<int:student_id>', views.StudentProfilesView.as_view(), name="student-profile"),
]
