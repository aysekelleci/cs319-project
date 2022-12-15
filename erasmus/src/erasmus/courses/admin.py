from django.contrib import admin

# Register your models here.
from .models import Course, Document, University, MergedCourse

admin.site.register(Course)
admin.site.register(University)
admin.site.register(Document)
admin.site.register(MergedCourse)
