from django.contrib.auth.models import User
from django.db import models

from questions.models import Question


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='account')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class User_question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL,
                             related_name='profile', null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 related_name='user_question', null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.question.question}'
