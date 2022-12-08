from django.shortcuts import render
from django.views import View

from .models import Course
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'courses/home.html')


class CourseView(View):
    def get(self, request):
        user = request.user
        courses = Course.objects.all()

        context = {'user': user, 'courses': courses}
        return render(request, 'courses/courses.html', context)
