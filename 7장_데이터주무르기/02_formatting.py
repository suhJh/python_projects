'''
구버젼 / 신버젼이 있다. 파이썬2, 3는 모두 지원한다.
'''

__str__ = '{} {} {}'.format(123, 456, 789)
print(__str__)

__str__ = '{n} {f} {s}'.format(n=123, f=456, s=789)
print(__str__)
