from django.urls import path

from questions.views import post, QuestionAPIView
urlpatterns = [
    path('<int:pk>/', post),
    path('test/<int:pk>/', QuestionAPIView.as_view()),
    # path('quest/<int:pk>/<int:pk>/', question_and_answer),
]
