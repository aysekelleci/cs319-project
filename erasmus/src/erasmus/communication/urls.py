from . import views
from django.urls import path, include

urlpatterns = [
    path('faq/', views.FAQView.as_view(),  name="faq"),
    path('add-question/', views.AddQuestion.as_view(), name = "add-question"),
]
