from data import question_data
from question_model import Question
from quiz_brain import QuizGame

question_bank = []
for q_data in question_data:
    question = Question(q_data["question"], q_data["correct_answer"])
    question_bank.append(question)


game = QuizGame(question_bank)

while game.still_has_questions():
    game.next_question()

print(f"You've completed the quiz")
print(f"Your final score was:{game.score}/{game.question_number}")




