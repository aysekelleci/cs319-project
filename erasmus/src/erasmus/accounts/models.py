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




