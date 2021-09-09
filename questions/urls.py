from django.urls import path

from questions.views import post

urlpatterns = [
    path('<int:pk>/', post),
]
