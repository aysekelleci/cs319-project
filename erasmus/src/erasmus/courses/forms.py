from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Course, Document, BilkentCourse

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ('product_text', 'product_description')
        fields = ('course_name', 'code', 'course_credit', 'bilkent_equivalent')


class BilkentCourseForm(forms.ModelForm):
    class Meta:
        model = BilkentCourse
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_name', 'document', 'document_type')
        labels = {
            'document_type': _('Document Type'),
            'document_name': _('Document Name'),
        }

class CoordinatorDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_name', 'document', 'document_type', 'user')
        labels = {
            'user': _('Student'),
            'document_name': _('Document Name'),
        }


