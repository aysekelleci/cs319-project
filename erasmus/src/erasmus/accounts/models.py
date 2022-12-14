from django.db import models
from django.contrib.auth.models import User

from courses.models import Course


class ErasmusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    bilkent_id = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.user.username)


class Student(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)
    gpa = models.FloatField()
    score = models.FloatField()
    status = models.CharField(max_length=100, blank=True)
    #coordinator = models.ForeignKey(Coordinator)
    is_erasmus_done = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.user.user.username)


class Coordinator(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)

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
    takenInsteadOf = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.course.course_codes + self.course.course_name)

class ToDo(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=400)
    link = models.CharField(max_length=200, blank=True)
    is_flagged = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    due_date = models.CharField(max_length=50)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='erasmus_user')

    def __str__(self):
        return '{}'.format(self.header)


class University(models.Model):
    university_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    # TODO courses ==> course object should have University (?)
    lowest_grade = models.CharField(max_length=20)
    highest_grade = models.CharField(max_length=20)
    passing_grade = models.CharField(max_length=20)
    inverted_scale = models.BooleanField(default=False)
    department = models.CharField(max_length=200) # supposed to be a list of strings

    def __str__(self):
        return '{}'.format(self.header)



