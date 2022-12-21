from django.contrib import admin

from .models import *


class ErasmusUserAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

class UserCourseAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(BoardMember)
admin.site.register(ErasmusUser)

admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(ToDo)


