from questions.models import Question
from users.models import Account, UserQuestion


class UserAnswerValidator:

    @classmethod
    def validate_answer(cls, user_answer: str) -> bool:
        if not user_answer:
            return False

        try:
            str(user_answer)
        except ValueError:
            return False
        return True


class QuestionUrlValidator:

    @classmethod
    def question_answer(cls, pk, account) -> bool:
        last_user_question = UserQuestion.objects.filter(account=account).order_by('-id').first() #the last question answered by the user

        if last_user_question == None and pk == 1:
            return True
        elif last_user_question == None and pk != 1:
            return False
        else:
            return True if last_user_question.get_id() == pk - 1 else False

