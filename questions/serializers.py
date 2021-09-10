from rest_framework import serializers

from questions.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'title',
            'question',)
        depth = 1


class QuizTestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',)


class AnswerQuestionSerializer(serializers.ModelSerializer):
    question_answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ('id',
                  'title',
                  'question',
                  'question_answer',)
