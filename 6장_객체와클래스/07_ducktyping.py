# 덕타이핑: 클래스와 상관없이 같은 동작을 다른 객체에 적용한다.
# 파이썬이 지향하는 다형성의 원리

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'    



hunter = Quote('Elmer Fudd', 'I am hunting wabbits')
print(hunter.who(), 'says: ', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up doc")

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")

print(hunted1.who(), hunted1.says())
print(hunted2.who(), hunted2.says())





class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'


brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says ', obj.says())


who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook) # -> 덕타이핑


