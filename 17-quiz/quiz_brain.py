class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO 1. asking the questions
    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, question.answer)

    # TODO 2. Checking if the answer is correct
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print(f"You got it wrong - {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    # TODO 3. Checking if we're at the end of the quiz
    def is_finish(self):
        bank_size = len(self.question_list)
        return self.question_number >= bank_size
