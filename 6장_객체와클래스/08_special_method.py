'''파이린트가 잡아서 독스트링을 넣어본다.'''
class Word():
    '''THIS IS SAMPLE CLASS'''
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        '''
        두 문자열이 같은지를 비교한다.
        파이썬의 내장 메서드다.
        이 경우 오버라이드한 개념이라고 보면 된다.
        :parameter {string}: some1
        :return {bool}: true/false
        '''
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "Word('" + self.text + "')"

__first__ = Word('ha')
__second__ = Word('HA')
__third__ = Word('eh')

print(__first__ == __second__)  # equals로 비교.
print(__first__)
