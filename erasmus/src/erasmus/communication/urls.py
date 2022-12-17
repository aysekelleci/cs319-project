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
    path('delete-notification/<int:notification_id>/', views.DeleteNotificationView.as_view(),  name="delete-notification"),
    path('flag-notification/<int:notification_id>/<int:is_flagged>/', views.FlagNotificationView.as_view(),  name="flag-notification"),
    path('', include('accounts.urls')),
]
