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




