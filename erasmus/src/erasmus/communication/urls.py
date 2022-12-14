from . import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('faq/', views.FAQView.as_view(),  name="faq"),
    path('add-question/', views.AddQuestion.as_view(), name = "add-question"),
    path('', include('accounts.urls')),
]
