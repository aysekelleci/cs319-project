from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import ToDo, ErasmusUser, Student

from django.forms import ModelForm
from django.core.exceptions import ValidationError


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('header', 'body', 'due_date')


class PhoneForm(forms.ModelForm):
    class Meta:
        model = ErasmusUser
        fields = ('phone', 'email')


class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email_visibility', 'phone_visibility', 'mobility_visiblity', 'status_visibility')




