from question_model import Question
from data import question_data
from new_data import question_data2
from quiz_brain import QuizBrain

# cara kerja app :
# buat question bank kosong, isi question bank dengan pertanyaan dari data yang dimodel dengan question model
# sambungkan ke quiz brain

question_bank = []

for question in question_data2:  # question is a --> dictionary in question_data list
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz, your final score is {quiz.score}/{len(quiz.question_list)}")
