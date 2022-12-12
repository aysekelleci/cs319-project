from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include

app_name = 'communication'

urlpatterns = [
    path('accounts/profile/', views.HomeView.as_view(),  name="profile"),
    path('courses/', views.CourseView.as_view(), name="courses"),
    path('add-to-courses/<int:course_id>', views.AddCourseView.as_view(), name="add-course"),
    path('remove-from-courses/<int:course_id>', views.DeleteCourseView.as_view(), name="remove-course"),
    path('add-unapproved-course/', views.AddUnapprovedCourse.as_view(), name="add-unapproved-course"),
    path('documents/', views.DocumentView.as_view(), name="documents"),
    path('', include('communication.urls')),

]
