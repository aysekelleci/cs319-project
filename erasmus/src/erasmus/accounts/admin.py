from django.contrib import admin

from .models import *


class ErasmusUserAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)


admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(BoardMember)
admin.site.register(ErasmusUser)

admin.site.register(UserCourse)
admin.site.register(ToDo)
admin.site.register(University)

