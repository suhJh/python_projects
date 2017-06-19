import itertools

# itertools.chain -> 순회 가능한 인자들을 하나씩 반환한다.
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)


# 무한이터레이터. 실행시키지말 것
#for item in itertools.cycle([1, 2]):
#    print(item)


# 축적된 값을 계산
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)


def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)



