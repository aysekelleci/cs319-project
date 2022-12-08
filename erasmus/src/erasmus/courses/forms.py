from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Course

from django.forms import ModelForm
from django.core.exceptions import ValidationError


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ('product_text', 'product_description')
        fields = ('course_name', 'course_codes', 'course_credit', 'courseType')

