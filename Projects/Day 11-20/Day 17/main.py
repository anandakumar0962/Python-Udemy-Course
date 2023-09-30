from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for datas in question_data:
    new_q = Question(datas['question'], datas['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed.")
print(f"Your final score was: {quiz.score}/{quiz.question_no}.")