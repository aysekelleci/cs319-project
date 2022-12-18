from django.contrib import admin

# Register your models here.
from .models import Course, Document, University, MergedCourse, BilkentCourse


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Course, CourseAdmin)
admin.site.register(University)
admin.site.register(Document)
admin.site.register(MergedCourse)
admin.site.register(BilkentCourse)
