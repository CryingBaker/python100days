from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_object = Question(question["question"],question["correct_answer"])
    question_bank.append(question_object)

quizbrain = QuizBrain(question_bank)

while quizbrain.next_question():
    print("")
    continue

print(f"Your final score:{quizbrain.score}/{len(quizbrain.question_list)}")