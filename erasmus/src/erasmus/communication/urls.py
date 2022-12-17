from . import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('faq/', views.FAQView.as_view(),  name="faq"),
    path('add-question/', views.AddQuestion.as_view(), name="add-question"),
    path('delete-question/<int:question_id>', views.DeleteQuestionView.as_view(), name="delete-question"),
    path('edit-question/<int:question_id>', views.EditQuestionView.as_view(), name="edit-question"),
    path('notification/', views.NotificationView.as_view(), name="notification"),
    path('', include('accounts.urls')),
]
