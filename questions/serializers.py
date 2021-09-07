from rest_framework import serializers

from quesAPP.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        field = ('question',)

