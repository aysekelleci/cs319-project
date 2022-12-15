from django.db import models

# Create your models here.
from accounts.models import Coordinator


# Singleton object for FAQ
class FAQ(models.Model):
    _faq = models.BooleanField(default=True, editable=False, unique=True)


class Question(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name="faq_singleton", default=True)
    user = models.ForeignKey(Coordinator, on_delete=models.CASCADE, related_name='coordinator')
    question = models.TextField()
    answer = models.TextField()

class Notification(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=400, blank=True)
    link = models.CharField(max_length=200, blank=True)
    is_flagged = models.BooleanField(default=False)
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ErasmusUser, on_delete=models.CASCADE, related_name='erasmus_user', default = 1)
    def __str__(self):
        return '{}'.format(self.header)



