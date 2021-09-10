from questions.models import Question, Answer
from users.models import Account


class IsCorrectAnswerService:

    @classmethod
    def is_correct(cls, user_answer: str, question_id):
        question = Question.objects.filter(id=question_id).first()
        correct_answer = Answer.objects.filter(question=question).filter(is_correct=True).filter(
            answer=user_answer).first()

        if correct_answer == None:
            return {
                'bool': False,
                'response': 'incorrect answer'}
        account = Account.objects.filter(user=user).first()
        account.total += 1
        account.save()

        return {
            'bool': True,
            'response': 'correct answer'
        }
        # for user_answer in user_answers:

        # for answer in answers:
        #     if answer.answer == user_answers:
        #         print('hi')
        #     print('hello')
        #     print(type(answers))
        # return True

class QuestionAnswerService:
    @classmethod
    def answer(cls, quest):
        answer = Answer.objects.filter(question=quest)
        print(answer)
        return answer