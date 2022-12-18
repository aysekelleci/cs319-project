from . import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('faq/', views.FAQView.as_view(),  name="faq"),
    path('add-question/', views.AddQuestion.as_view(), name="add-question"),
    path('delete-question/<int:question_id>', views.DeleteQuestionView.as_view(), name="delete-question"),
    path('edit-question/<int:question_id>', views.EditQuestionView.as_view(), name="edit-question"),
    path('notification/', views.NotificationView.as_view(), name="notification"),
    path('forum/', views.ForumView.as_view(), name="forum"),
    path('delete-notification/<int:notification_id>/', views.DeleteNotificationView.as_view(),
         name="delete-notification"),
    path('flag-notification/<int:notification_id>/<int:is_flagged>/', views.FlagNotificationView.as_view(),
         name="flag-notification"),
    path('add-post/', views.AddPostView.as_view(), name="add-post"),
    path('delete-post/<int:post_id>', views.DeletePostView.as_view(), name="delete-post"),
    path('post-detail/<int:post_id>', views.PostDetailView.as_view(), name="post-detail"),
    path('delete-response/<int:response_id>', views.DeleteResponseView.as_view(), name="delete-response"),

    path('', include('accounts.urls')),
]
