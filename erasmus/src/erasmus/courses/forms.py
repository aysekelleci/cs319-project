from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Course, Document

from django.forms import ModelForm
from django.core.exceptions import ValidationError


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ('product_text', 'product_description')
        fields = ('course_name', 'code', 'course_credit', 'bilkent_equivalent')

        field_names = {
            'code': 'CODE',
            'course_name': 'NAME',
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_name', 'document', 'is_signed', 'document_type')

class CoordinatorDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_name', 'document', 'document_type', 'user')


