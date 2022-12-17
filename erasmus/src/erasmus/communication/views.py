from .models import Question, Notification
from django.views import View
from accounts.models import ErasmusUser, Coordinator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
# Create your views here.


class FAQView(LoginRequiredMixin, View):
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
            coordinator = None

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
            new_question = question_form.save(commit=False)
            new_question.user = coordinator

            # Save the question to the database
            new_question.save()

        else:
            messages.info(request, "Question Form is not valid")
            return redirect("/faq")

        context = {'coordinator': coordinator, 'question_form': question_form, 'new_question': new_question}
        messages.info(request, "Question is added")
        return redirect("/faq")


class DeleteQuestionView(LoginRequiredMixin, View):
    def get(self, request, question_id):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator

            if coordinator is None:
                return redirect("/faq")

        question = get_object_or_404(Question, pk=question_id)  # Check whether given course object exists

        question.delete()

        messages.info(request, "Question was deleted")
        return redirect("/faq")


class EditQuestionView(View):
    def get(self, request, question_id):
        old_question = get_object_or_404(Question, pk=question_id)
        user=request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator

            if coordinator is None:
                return redirect("/faq")

            question_form = QuestionForm(instance=old_question)

            context = {'old_question': old_question, 'question_form': question_form, 'coordinator': coordinator}

            return render(request, 'communication/edit-question.html', context)

    def post(self, request, question_id):
        old_question = get_object_or_404(Question, pk=question_id)
        user=request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            coordinator = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator

            if coordinator is None:
                return redirect("/faq")

            question_form = QuestionForm(instance=old_question, data=request.POST)

            if question_form.is_valid():
                messages.info(request, "This question was successfully updated.")
                question_form.save()
                return redirect("/faq")

            else:
                messages.info(request, "This question form is not valid.")
                return render(request, "communication/edit-question.html", context)


class NotificationView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        notifications = Notification.objects.filter(user=erasmus_user)
        context = {'user': erasmus_user, 'notifications': notifications}
        return render(request, 'communication/notifications.html', context)





