from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for question in question_data:
#     question_bank.append(Question(question["text"], question["answer"]))

# Get into the results of question_data from opentdb
new_questions = question_data["results"]
for question in new_questions:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while not quiz.is_finish():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
