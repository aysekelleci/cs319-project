from django import forms

from .models import Question, Post, Response


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'answer')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'text')


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text',)

