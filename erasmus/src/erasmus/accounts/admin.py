from django.contrib import admin

from .models import ErasmusUser, Student, Coordinator, BoardMember, UserCourse


class ErasmusUserAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)


admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(BoardMember)
admin.site.register(ErasmusUser, ErasmusUserAdmin)

admin.site.register(UserCourse)

