"""
연습문제
"""
from collections import namedtuple

# 6-1
class Thing:
    '''아무 내용도 없는 Thing클래스를 만들어 출력하라'''
    pass

__example__ = Thing()
print(__example__)


# 6-2
class Thing2():
    '''Thing2 클래스를 만들고 이 클래스의 letters 속성의 값 abc를 할당한 후 letters 를 출력하라'''
    def __init__(self, letters):
        '''생성자'''
        self.letters = letters

__example2__ = Thing2('abc')
print(__example2__.letters)


# 6-3
class Thing3:
    '''이번에는 인스턴스의 letters속성에 xyz를 할당한 후 letters를 출력하라. letters를 출력하기 위해 객체를 생성해야 하는가 -> 당연하지.'''
    pass

# 6-4
'''네임드 튜플을 이용한 방법'''
__el_dict__ = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Element = namedtuple('Element', 'name symbol number')
__hydrogen__ = Element(**__el_dict__)
print(__hydrogen__)


# 6-5
class Element2():
    '''일반 클래스를 이용한 방법'''
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __repr__(self):
        return self.name + ' ' + self.symbol + ' ' + str(self.number)
__hydrogen2__ = Element2(**__el_dict__)
print(__hydrogen2__)


# 6-6, 6-7
class Element3():
    '''Element클래스에서 객체의 속성 값을 출력하는 dump메서드를 정의하고 출력하라'''
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return '그냥 만들어봤어..'
    def dump(self):
        '''해당메서드다.'''
        print(self.name + self.symbol + str(self.number))

__hydrogen3__ = Element3(name="sjh", symbol="fuck", number=18)
__hydrogen3__.dump()


# 6-8
class Hidden():
    '''프라이빗을 구현해보아라'''
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        '''getter'''
        return self.__name
    @property
    def symbol(self):
        '''getter'''
        return self.__symbol
    @property
    def number(self):
        '''getter'''
        return self.__number

__hidden__ = Hidden('H_SJH', 'FUCK', 1818)
print(__hidden__.name)
print(__hidden__.symbol)
print(__hidden__.number)


# 6-9
class Bear():
    "곰클래스다"
    def eats(self):
        "먹는다."
        return 'berries'

class Rabbit():
    "토끼다."
    def eats(self):
        "먹는다."
        return 'clover'

class Octothorpe():
    "뭔지 모르겠네."
    def eats(self):
        "먹는다."
        return 'campers'

print(Bear().eats())
print(Rabbit().eats())
print(Octothorpe().eats())


# 6-10
class Abstact:
    '부모클래스'
    def does(self):
        '딱히 자녀에서 오버라이딩하는데 정의할 필요가 있는지..'
        return '아버지다.'

class Laser(Abstact):
    'Laser'
    def does(self):
        'Laser.does'
        return 'disintegrate'

class Claw(Abstact):
    'Claw'
    def does(self):
        'Claw.does'
        return 'crush'

class SmartPhone(Abstact):
    'SmartPhone'
    def does(self):
        'SmartPhone.does'
        return 'ring'


class Robot:
    '''위에서 선언한 클래스의 인스턴스들을 가지고 있는 클래스를 만들라'''
    def __init__(self, laser, claw, smart_phone):
        self.laser = laser
        self.claw = claw
        self.smart_phone = smart_phone
    def does_sequence(self):
        '''멤버들의 함수를 연달아 실행'''
        print(self.laser.does())
        print(self.claw.does())
        print(self.smart_phone.does())

Robot(Laser(), Claw(), SmartPhone()).does_sequence()
