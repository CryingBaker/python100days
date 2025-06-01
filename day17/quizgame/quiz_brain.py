class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def check_answer(self,user_answer):
        if self.question_list[self.question_number].answer == user_answer:
            return True
        return False

    def check_quizend(self):
        if self.question_number >= len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question_asked = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1} {question_asked.question} (True/False): ")
        if self.check_answer(answer):
            self.score += 1
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Your current score is {self.score}/{self.question_number+1}")
        self.question_number+=1
        if self.check_quizend():
            return False
        return True
