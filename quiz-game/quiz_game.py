class QuizBrain:
    def __init__(self, lis):
        self.question_num = 0
        self.question_list = lis
        self.score = 0

    def has_new_que(self):
        return self.question_num < len(self.question_list)

    def next_que(self):
        current_que = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_que.text}(True/False): ")
        self.check_answer(user_answer, current_que.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it...Its right.")
            self.score += 1
        else:
            print("Ohh.! That's Wrong.")
            print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is:{self.score}/{self.question_num}. ")
        print("-----------------------------------------------------------------------------------------------------------------")
        print()
