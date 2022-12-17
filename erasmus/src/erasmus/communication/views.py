from .models import Question, Notification,  Post, Response
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

        questions = Question.objects.all()
        context = {'coordinator': coordinator, 'question_form': question_form,
                   'new_question': new_question, 'questions': questions}
        messages.success(request, "Question is added")
        return render(request, 'communication/faq.html', context)


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

        messages.success(request, "Question is deleted")
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
                messages.info(request, "This question is successfully updated.")
                question_form.save()
                return redirect("/faq")

            else:
                context = {'old_question': old_question, 'question_form': question_form, 'coordinator': coordinator}

                messages.error(request, "This question form is not valid.")

                return render(request, "communication/edit-question.html", context)


class NotificationView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()

        unflagged_notifications = Notification.objects.filter(user=erasmus_user, is_flagged=False)
        flagged_notifications = Notification.objects.filter(user=erasmus_user, is_flagged=True)

        context = {'user': erasmus_user, 'unflagged_notifications': unflagged_notifications,
                   "flagged_notifications": flagged_notifications}
        return render(request, 'communication/notifications.html', context)

class DeleteNotificationView(LoginRequiredMixin, View):
        def get(self, request, notification_id):

            try:
                notification = get_object_or_404(Notification, pk=notification_id)
            except:
                notification = None
            if notification is not None:
                notification.delete()
                messages.info(request, "Notification removed.")
                return redirect("/notification")


class FlagNotificationView(LoginRequiredMixin, View):
    def get(self, request, notification_id, is_flagged):
        notification = get_object_or_404(Notification, pk=notification_id)

        notification.is_flagged = is_flagged
        notification.save()  # update the todo object
        return redirect("/notification")


class ForumView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        erasmus_user = ErasmusUser.objects.filter(user=user).first()
        if erasmus_user is not None:
            forum_user = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator
            if forum_user is None:
                forum_user = Coordinator.objects.filter(user=erasmus_user).first()  # get student

        posts = Post.objects.all
        context = {'forum_user': forum_user, 'posts': posts}
        return render(request, 'communication/forum.html', context)


class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        forum_user = get_forum_user(user)
        










def get_forum_user(user):

    erasmus_user = ErasmusUser.objects.filter(user=user).first()
    forum_user = None
    if erasmus_user is not None:
        forum_user = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator
        if forum_user is None:
            forum_user = Coordinator.objects.filter(user=erasmus_user).first()  # get student

    return forum_user


