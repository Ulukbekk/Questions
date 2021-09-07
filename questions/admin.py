from django.contrib import admin

from questions.models import Question, Answer

admin.site.register(Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'question')
