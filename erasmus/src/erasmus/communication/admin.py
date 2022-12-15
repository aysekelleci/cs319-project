from django.contrib import admin

# Register your models here.

from .models import FAQ, Question, Notification

admin.site.register(FAQ)

admin.site.register(Question)
admin.site.register(Notification)
