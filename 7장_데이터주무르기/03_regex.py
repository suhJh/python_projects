'''
정규표현식
re는 정규표현식을 임포트할 수 있는 표준 모듈이다.
'''
import re
result = re.match('You', 'Young Frankenstein')
print(result)

"""
match() 패턴이 처음부터 일치하는지를 체크  -> m.group()
search() 첫번째로 일치하는 객체를 반환   -> m.group()
findall() 중첩에 상관없이 모두 일치하는 문자열 리스트를 반환
split() 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트를 반환
sub() 대체 인자를 하나 더 받아 패턴과 일치하는 모든 소스부분을 대체 인자로 변경한다.
"""

__source__ = 'Young Frankenstein'
__m__ = re.match('You', 'Young Frankenstein')
if __m__:
    print('1. ', __m__.group())


__source2__ = "Frank"
__m2__  = re.search('Frank', __source2__)

if __m2__:
    print('2. ', __m2__.group())

__m2__ = re.match('.*Frank', __source2__)
if __m2__:
    print('3. ', __m2__.group())

'''
정규식 설명
.: 한 문자
*: 이전 패턴이 여러 개 올 수 있다.

'''


# 첫번째로 일치하는 패턴 찾기
m = re.search('Frank', __source__)
if m:
    print('4. ', m.group())



# 일치하는 모든 패턴 찾기
m = re.findall('n', __source__)
if m:
    print('5. ', m)

m = re.findall('n.', __source__)
if m:
    print('6. ', m)

m = re.findall('n.?', __source__)
if m:
    print('7. ', m)

# 패턴으로 쪼개기. 문자열에서 split하는 것과 같은 결과이다.
m = re.split('n', __source__)
if m:
    print('8, ', m)


# 일치하는 패턴 대체하기
m = re.sub('n', '?', __source__)
if m:
    print('9', m)


import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

m = re.findall('\d', printable)
print('10. ', m)

m = re.findall('\s', printable)
print('11. ', m)





'''
패턴: 지정자
'''

source = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''

m = re.findall('wish', source)
print('12. ', m)

m = re.findall('wish|fish', source)
print('13. ', m)

m = re.findall('^wish', source)
print('14. ', m)

m = re.findall('^I wish', source)
print('15. ', m)

m = re.findall('fish$', source)
print('16. ', m)

m = re.findall('tonight\.$', source)    # 그냥 .도 되기는 하지만 \. 이스케이프 처리하는 것이 더 정확
print('17. ', m)

m = re.findall('[wf]ish', source)
print('18. ', m)

m = re.findall('[wsh]+', source)
print('19. ', m)

m = re.findall('ght\W', source)
print('20. ', m)

m = re.findall('I (?=wish)', source)
print('21. ', m)    # wish 이전에 나오는 I를 찾아라

m = re.findall('(?<=I) wish', source)
print('22. ', m)

m = re.findall('\bfish', source)    # 파이썬과 충돌
print('23. ', m)

m = re.findall(r'\bfish', source)   # 충돌방지로 r을 표현식 앞에 삽입한다.
print('24. ', m)


'''패턴: 매칭 결과 지정하기'''
m = re.search(r'(. dish\b).*(\bfish)', source)
print('25', m.groups())
