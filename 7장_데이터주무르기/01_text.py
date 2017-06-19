'''
파이썬 3 유니코드 문자열
'''
import unicodedata

def unicode_test(value):
    '''
    유니코드 문자를 취하는 함수
    '''
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('ㄱ')
unicode_test('\u00a2')
unicode_test('\u2603')


unicode_test('\u00e9')
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))


'''인코딩/디코딩'''
snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(ds)

'''인코딩 옵션'''
ds2 = snowman.encode('ascii', 'ignore') # 사용할 수 없는 문자는 인코딩하지 않는다.
ds2 = snowman.encode('ascii', 'replace') # 알 수 없는 문자를 ?로 대체한다.
ds2 = snowman.encode('ascii', 'backslashreplace') # 이스케이프처리한다.
ds2 = snowman.encode('ascii', 'xmlcharrefreplace') # 이스케이프 시퀀스를 출력할 수 있는 문자열로 만든다.


place = 'caf\u00e9'
print(place)
place_bytes = place.encode('utf-8')
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)
