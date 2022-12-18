from .models import Question, Notification,  Post, Response

from .models import Question, Notification, Post, Response, Forum, FAQ

from django.views import View
from accounts.models import ErasmusUser, Coordinator, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm, PostForm, ResponseForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Count

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
            if FAQ.objects.filter().first() is None:
                faq = FAQ()
                faq.save()
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

#######################################################################################################################
# Forum Views


class ForumView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        forum_user = get_forum_user(user)
        new_response = None
        response = ResponseForm()
        posts = Post.objects.all().order_by('-date').annotate(number_of_responses=Count('responses'))
        context = {'forum_user': forum_user, 'posts': posts, 'new_response': new_response}
        return render(request, 'communication/forum.html', context)


class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        forum_user = ErasmusUser.objects.filter(user=user).first()
        new_post = None

        post_form = PostForm()

        context = {'forum_user': forum_user, 'post_form': post_form, 'new_post': new_post}

        return render(request, 'communication/add-post.html', context)

    def post(self, request):
        user = request.user
        forum_user = ErasmusUser.objects.filter(user=user).first()
        forum = Forum.objects.filter().first()

        post_form = PostForm(data=request.POST)
        if forum_user is None:
            # messsages.error(request, 'user does not exist in erasmus user')
            return redirect("/forum")

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.forum = forum
            new_post.user = forum_user

            # Save the question to the database
            new_post.save()

        else:
            messages.info(request, "Post Form is not valid")
            return redirect("/forum")

        messages.success(request, " Post is added")
        return redirect("/forum")


class DeletePostView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        user = request.user

        forum_user = get_forum_user(user)

        post = get_object_or_404(Post, pk=post_id, user=forum_user)  # Check whether given course object exists

        post.delete()

        messages.success(request, "Question is deleted")
        return redirect("/forum")


class DeleteResponseView(LoginRequiredMixin, View):
    def get(self, request, response_id):
        user = request.user
        forum_user = get_forum_user(user)

        if forum_user is None:
            redirect('/forum')

        response = get_object_or_404(Response, pk=reponse_id, user=forum_user)

        response.delete()

        messages.success(request, "Response is deleted")
        return redirect("/faq")


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        user = request.user
        forum_user = get_forum_user(user)

        post = Post.objects.filter(pk=post_id).first()
        responses = None
        if post.exists():
            responses = Response.objects.filter(post=post)

        new_response = None

        response_form = ResponseForm()

        context = {'forum_user': forum_user, 'response_form': response_form, 'new_response': new_response, 'post': post,
                   'responses': responses}

        return render(request, 'communication/detail-post.html', context)

    def post(self, request):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        forum_user = get_forum_user(user)

        response_form = ResponseForm(data=request.POST)

        if forum_user is None:
            # messsages.error(request, 'user does not exist in erasmus user')
            return redirect("/accounts/profile")

        if response_form.is_valid():
            new_response = response_form.save(commit=False)
            new_response.post = post
            new_response.user = forum_user

            # Save the response to the database
            new_response.save()

        else:
            messages.error(request, "Response Form is not valid")
            context = {'forum_user': forum_user, 'response_form': response_form, 'new_response': new_response,
                       'post': post}
            return render(request, 'communication/detail-post.html', context)

        messages.success(request, " Response is added")
        return render(request, 'communication/detail-post.html', context)


























def get_forum_user(user):

    erasmus_user = ErasmusUser.objects.filter(user=user).first()
    forum_user = None
    if erasmus_user is not None:
        forum_user = Coordinator.objects.filter(user=erasmus_user).first()  # get coordinator
        if forum_user is None:
            forum_user = Student.objects.filter(user=erasmus_user).first()  # get student

    return forum_user


