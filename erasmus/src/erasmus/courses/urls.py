from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include

urlpatterns = [
    path('accounts/profile/', views.HomeView.as_view(),  name="profile"),
    path('courses/', views.CourseView.as_view(), name="courses")
]
