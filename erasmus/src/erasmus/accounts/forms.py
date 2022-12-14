from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import ToDo

from django.forms import ModelForm
from django.core.exceptions import ValidationError


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('header', 'body', 'due_date')


