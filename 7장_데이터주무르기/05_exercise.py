''' 7장 데이터 주무르기 연습문제 '''
import unicodedata
import re


# 7-1 유니코드 문자열 변수 mystery를 생성하고 여기에 값 '\U0001f4a9'를 할당하라
# mystery와 mystery에 대한 유니코드 이름을 찾아서 출력하라

mystery = '\U0001f4a9'
print('7-1.', unicodedata.name(mystery))
print('7-1.', unicodedata.lookup(unicodedata.name(mystery)))


# 7-2 mystery를 인코딩해보자. utf-8로 바이트 변수 pop_bytes에 할당하고 출력하라
pop_bytes = mystery.encode('utf-8')
print('7-2', pop_bytes)

# 7-3 utf-8을 이용하여 pop_bytes를 문자열 변수 pop_string에 디코딩하여 출력하라
pop_string = pop_bytes.decode('utf-8')
print('7-3.', pop_string)

# 7-4 옛날 스타일의 포맷팅을 사용하여 시를 써보자
before_string = '''
    my kitty cat likes %s,
    my kitty cat likes %s,
    my kitty cat fell on his %s,
    And now thinks he's a %s
''' % ('roast beef', 'ham', 'head', 'clam') # 튜플로 넘긴다.
print('7-4.', before_string)


# 7-5 새로운 스타일의 포맷팅으로 다음을 출력하라
# 7-6 response 딕셔너리를 만들어보라. 문자열의 키값은... 
letters = '''
    Dear {salutation} {name}

    Thank you for your letter. We are sorry that our {product} {verbed} in your
    {room}. please note that it should never be used in a {room}, especially
    near any {animals}

    Send us your receipt and {amount} for shipping and handling. We still send
    you another {product} that, in our test, is {percent}% less likely
    to have {verbed}

    Thank you for your support.abs

    Sincerely,
    {spokesman}
    {job_title}
'''
response = {
    'salutation': 'sal',
    'name': 'sjh',
    'product': '맥북',
    'verbed': '과거형',
    'room': '좋은방',
    'animals': '장군이',
    'amount': '25개',
    'percent': '77%',
    'spokesman': '말하는사람',
    'job_title': '개발자'
}

print('7-6.', letters.format(**response)) # kwargs 형태로 넘긴다.

# 7-7. 다음의 시를 mammoth변수에 할당하라

mammoth = '''
    We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no files dare seize.

    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.

    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.

    May you not receive a scar as
    We have heard that Mr. Harris
    Intedns to send you off as far as
    the great worlds show at Paris.

    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs of glees
    We could not sing, oh! queen of cheese.abs

    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon.
'''

print('7-8', re.findall(r'\bc\w*', mammoth))    # c로 시작하는 단어찾기
print('7-9', re.findall(r'\bc\w{3}\b', mammoth)) # c로 시작하고 네글자인 단어 모두 찾기
print('7-10.', re.findall(r'\b\w*r\b', mammoth)) # r로 끝나는 단어 찾기
print('7-11.', re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth)) # aeiou가 세번 연속으로 나오는 단어를 모두 찾아라

