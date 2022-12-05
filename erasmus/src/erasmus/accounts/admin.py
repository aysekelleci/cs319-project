from django.contrib import admin

from .models import ErasmusUser, Student, Coordinator, BoardMember

admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(BoardMember)
