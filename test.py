#building game through Python.

class Hangman:
    def __init__(self, incor_att):
        self.incorrect_attempts = incor_att

    #incoorect attempts counting here
    def Incorrect_attempt_counting(self):
        try:
            # incorrect_attempts=int(input("How many Incorrect attempts you want(1-10) ??? - "))
            if self.incorrect_attempts >7:
                print("Limit is exceeded(7 set as default.)!!!")
                self.incorrect_attempts=7
            elif self.incorrect_attempts <1:
                print("Limit set to default 1.")
                self.incorrect_attempts = 1
        except ValueError:
            print("Invalid Input --- Only integers allowed!!!")

#testing game from here
incorrect_attempts=int(input("How many Incorrect attempts you want(1-7) ??? - "))
h_obj = Hangman(incorrect_attempts)
h_obj.Incorrect_attempt_counting()
print(h_obj.incorrect_attempts)
