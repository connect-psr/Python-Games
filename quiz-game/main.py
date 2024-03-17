from question_model import Question
from data import question_data
from quiz_game import QuizBrain

question_bank = []
for que in question_data:
    question_text = que["text"]
    question_answer = que["answer"]
    new_que = Question(question_text, question_answer)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.has_new_que():   # if quiz still has que remaining..
    quiz.next_que()

print("You've completed the quiz..")
print(f"Your final score: {quiz.score}/{quiz.question_num}")