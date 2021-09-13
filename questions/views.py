from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from questions.models import Question, Answer
from questions.serializers import QuizTestSerializers, QuestionSerializer, AnswerQuestionSerializer
from questions.services import IsCorrectAnswerService, QuestionAnswerService
from questions.validators import UserAnswerValidator, QuestionUrlValidator
from users.models import UserQuestion, Account


service_class = IsCorrectAnswerService
validator_class_q_u = QuestionUrlValidator
validator_class = UserAnswerValidator


@csrf_exempt
@api_view(['POST'])
def post(request, pk):
    user_answer = request.data.get('user_answer')
    user = request.user
    account = Account.objects.filter(user=user).first()
    question = Question.objects.filter(id=pk).first()

    if validator_class_q_u.question_answer(pk, account):
        is_correct = service_class.is_correct(user_answer, pk, user)

        user_question = UserQuestion.objects.create(
            account=account,
            question=question,
            is_correct=is_correct['bool'],
        )
        return HttpResponse(is_correct['response'], status=status.HTTP_200_OK)
    else:
        return HttpResponse('you answer the wrong question', status.HTTP_400_BAD_REQUEST)

        # account = self.request.user.account
        # account.is_correct = self.service_class.is_correct(user_answer, pk)
        # account.save()
    # def post(self, request, *args, **kwargs):
    #     user_answer = request.data.get('user_answer')
    #
    #     if not self.validator_class.validate_answer(user_answer):
    #         return Response('You need to write an integer', status=status.HTTP_400_BAD_REQUEST)
    #
    #     self.service_class.is_correct(user_answer, request.data.get('question'))
    #
    #     return Response('Ok', status=status.HTTP_200_OK)
        # User_question.objects.create(user=request.data.get('user'), question=request.data.get('question'), is_correct=self.validator_class.validate_answer(user_answer))


class QuestionAPIView(generics.RetrieveAPIView):
    serializer_class = AnswerQuestionSerializer
    queryset = Question.objects.all()















