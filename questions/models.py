from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=20)
    question = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 related_name='question_answer', blank=True, null=True)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question.title
