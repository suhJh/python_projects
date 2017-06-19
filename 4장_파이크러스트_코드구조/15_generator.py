# range는 시퀀스를 생성하는 객체다.

def my_range(first=0, last=0, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
print(type(ranger))


for x in ranger:
    print(x)
