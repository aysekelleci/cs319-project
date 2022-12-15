from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from courses.models import Course


class ErasmusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    bilkent_id = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.user.username)

class Coordinator(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.user.user.username)

class Student(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)
    gpa = models.FloatField()
    score = models.FloatField()
    status = models.CharField(max_length=100, blank=True)
    coordinator = models.ForeignKey(Coordinator, blank=True, on_delete=models.SET_NULL, null=True)
    is_erasmus_done = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.user.user.username)


class BoardMember(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.user.username)


class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_user')
    grade = models.IntegerField(blank=True)

    def __str__(self):
        return '{}'.format(self.course.course_codes + self.course.course_name)

class ToDo(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=400, blank=True)
    link = models.CharField(max_length=200, blank=True)
    is_flagged = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='erasmus_user', default = 1)

    def __str__(self):
        return '{}'.format(self.header)






