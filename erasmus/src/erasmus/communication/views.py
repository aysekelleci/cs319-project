from django.shortcuts import render

from .models import Question
from django.views import View
from accounts.models import ErasmusUser, Coordinator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


class FAQView(View):
    def get(self, request):
        user = request.user
        username = request.user.username
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        else:
            coordinator = None

        questions = Question.objects.all()
        context = {'username': username, 'coordinator': coordinator, 'questions': questions}
        return render(request, 'communication/faq.html', context)


class AddQuestion(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        else:
            coordinator= None

        new_question = None

        question_form = QuestionForm()

        context = {'coordinator': coordinator, 'question_form': question_form, 'new_question': new_question}

        return render(request, 'communication/add-question.html', context)

    def post(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()
        else:
            coordinator = None

        question_form = QuestionForm(data=request.POST)
        new_question = None

        if question_form.is_valid():
            new_question.user = coordinator
            new_question = question_form.save(commit=False)
            # Save the question to the database
            new_question.save()

        else:
            messages.info(request, "Question Form is not valid")
            return redirect("/faq")

        context = {'coordinator': coordinator, 'question_form': question_form, 'new_question': new_question}
        messages.info(request, "Question is added")
        return render(request, 'communication/faq.html', context)






