
from zxcvbn import zxcvbn

class Passlyzer():

    def __init__(self, password, userInput=[]) -> None:
        self.results = zxcvbn(password, user_inputs=userInput)
        self.score = self.results['score']
        
    def analyze(self):
        if self.score == 1:
            return 'Bad'
        elif self.score == 2:
            return 'Sus'
        elif self.score == 3:
            return 'Decent'
        else:
            return 'Great'

