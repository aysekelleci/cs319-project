from django.db import models
from django.contrib.auth.models import User


class ErasmusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    bilkent_id = models.IntegerField()
    phone = models.IntegerField()


class Student(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)
    gpa = models.FloatField()
    score = models.FloatField()
    status = models.CharField(max_length=100, blank=True)
    #coordinator = models.ForeignKey(Coordinator)
    is_erasmus_done = models.BooleanField(default=False)


class Coordinator(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)


class BoardMember(models.Model):
    user = models.OneToOneField(ErasmusUser, on_delete=models.CASCADE)

