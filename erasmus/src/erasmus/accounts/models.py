from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from courses.models import Course, University



INITIAL = "Account created"
PLACED = "Placement done"
NO_PLACEMENT = "No placement"
CHOOSING_COURSES = "Choosing courses"
WAIT_COURSE_APPROVAL = "Waiting for the course approval"
WAIT_FINAL_LIST_APPROVAL = "Waiting for the final course list approval"
FINAL_LIST_APPROVED =  "Final course list is approved, generate pre-approval form"
WAIT_PRE_APPROVAL_FORM = "Waiting for the pre-approval form to be signed"
WAIT_MOBILITY = "Waiting for the mobility period"
IN_MOBILITY = "In mobility period"
FINISHED_MOBILITY = "Finished mobility period"

status_list = [INITIAL, PLACED, NO_PLACEMENT, CHOOSING_COURSES, WAIT_COURSE_APPROVAL, WAIT_FINAL_LIST_APPROVAL,
               FINAL_LIST_APPROVED, WAIT_PRE_APPROVAL_FORM, WAIT_MOBILITY, IN_MOBILITY, FINISHED_MOBILITY]

STATUS_TYPE_CHOICES = [(status, status) for status in status_list]

class ErasmusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='erasmus_user')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    bilkent_id = models.IntegerField()
    phone = models.CharField(default="", blank=True, max_length=100) # fixit charfield olsun
    department = models.CharField(max_length=100, default="Computer Engineering")

    def __str__(self):
        return '{}'.format(self.user.username)

class Coordinator(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE, related_name='coordinator')
    def __str__(self):
        return '{}'.format(self.user.user.username)


class Student(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE, related_name='student')
    gpa = models.FloatField()
    score = models.FloatField()
    status = models.CharField(max_length=200, choices=STATUS_TYPE_CHOICES, default=STATUS_TYPE_CHOICES[0][0])
    coordinator = models.ForeignKey(Coordinator, blank=True, on_delete=models.SET_NULL, null=True,
                                    related_name='students')
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    is_erasmus_done = models.BooleanField(default=False)
    academic_year = models.CharField(max_length=20, default="")
    semester = models.CharField(max_length=20, default="")
    email_visibility = models.BooleanField(default=True)
    phone_visibility = models.BooleanField(default=True)
    mobility_visiblity = models.BooleanField(default=True)
    status_visibility = models.BooleanField(default=True)
    final_list_submitted = models.BooleanField(default=False)
    final_list_approved = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.user.name)


class BoardMember(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.user.username)


class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_user')
    grade = models.IntegerField(blank=True, null=True)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.course.code + self.course.course_name)

class ToDo(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=400, blank=True)
    link = models.CharField(max_length=200, blank=True)
    is_flagged = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='todos', default=1)

    def __str__(self):
        return '{}'.format(self.header)






