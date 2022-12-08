from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Course
from accounts.models import UserCourse, Student, ErasmusUser
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from courses.forms import CourseForm


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


class AddCourseView(View):
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


class DeleteCourseView(View):
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









