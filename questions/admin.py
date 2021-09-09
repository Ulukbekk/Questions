from django.contrib import admin

from questions.models import Question, Answer

@admin.register(Answer)
class AnserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'answer',
        'is_correct',
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'question')
