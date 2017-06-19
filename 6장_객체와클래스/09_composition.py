"""상속보다 컴포지션이나 어그리게이션의 사용이 더 적절한 경우가 있다."""
class Bill():
    '''부리 클래스'''
    def __init__(self, description):
        self.description = description

class Tail():
    '''꼬리 클래스'''
    def __init__(self, length):
        self.length = length

class Duck():
    '''오리 클래스'''
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        '''자기소개'''
        print("duck has a", self.bill.description, 'bill and a ', self.tail.length, 'tail')

__tail__ = Tail('long')
__bill__ = Bill('wide orange')
__duck__ = Duck(__bill__, __tail__)
__duck__.about()
