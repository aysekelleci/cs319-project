from django.contrib import admin

# Register your models here.

from .models import FAQ, Question, Notification, Forum, Post, Response

admin.site.register(FAQ)

admin.site.register(Question)

admin.site.register(Notification)

admin.site.register(Forum)

admin.site.register(Post)

admin.site.register(Response)



