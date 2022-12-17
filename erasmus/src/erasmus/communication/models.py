from django.db import models

# Create your models here.
from accounts.models import Coordinator, ErasmusUser


# Singleton object for FAQ
class FAQ(models.Model):
    _faq = models.BooleanField(default=True, editable=False, unique=True)


class Question(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name="faq_singleton", default=True)
    user = models.ForeignKey(Coordinator, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    answer = models.TextField()

class Notification(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=400, blank=True)
    link = models.CharField(max_length=200, blank=True)
    is_flagged = models.BooleanField(default=False)
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='notification_user', default=1)
    def __str__(self):
        return '{}'.format(self.header)


class Forum(models.Model):
    _forum = models.BooleanField(default=True, editable=False, unique=True)
    name = models.CharField(max_length=30)


class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="forum_singleton", default=True)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=50)
    text = models.TextField()


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='responses')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()




