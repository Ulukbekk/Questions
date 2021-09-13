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
        last_user_answer = UserQuestion.objects.filter(account=account).order_by(
            '-id').first()  # the last question answered by the user

        if last_user_answer is not None:
            last_user_question = Question.objects.filter(id=last_user_answer.question.get_id()).first()
            if last_user_question.id == pk:
                account.total -= 1
                account.save()
                return False
            return True if last_user_answer.get_id() == pk - 1 else False
        else:
            if pk == 1:
                return True
            elif pk != 1:
                return False

