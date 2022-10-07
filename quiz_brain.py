class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"{self.question_number + 1}: {current_question.question_text} True/False?: ")
        self.question_number = self.question_number + 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score = self.score + 1
            print(f"Your current score is {self.score}/{len(self.question_list)}")
        else:
            print("That's wrong")
            print(f"Your current score is {self.score}/{len(self.question_list)}")

        print(f"The Correct answer is: {correct_answer}")
        print("\n")
