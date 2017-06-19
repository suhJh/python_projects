''' 
파일 입출력

기본적인 파일 리딩
fileobj = open(filename, mode)

mode
    첫번째 글자
    -r: 파일 읽기
    -w: 파일 쓰기
    -x: 파일 쓰기(파일이 존재하지 않을 경우에만 해당)
    -a: 파일 추가하기(파일이 존재하면 파일의 끝에서부터 쓴다.

    두번째 글자
    -t: (또는 아무것도 명시하지 않을 경우 디폴트): 텍스트 타입
    -b: 이진 타입
'''

poem = '''There was a young lady named Bright,
Whose spped was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

# write를 사용할 경우
print(len(poem))
fout = open('./relativity.txt', 'wt')
fout.write(poem)
fout.close()

# print를 사용할 경우
fout = open('./relativity2.txt', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

# 파일에 쓸 문자열이 크면 특정 단위로 나누어서 파일에 쓴다.
fout = open('./relativity3.txt', 'wt')
size = len(poem)
offset = 0
chunk = 50
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset = offset + chunk
fout.close()

# 파일이 중요한 경우 덮어쓰지 않도록 한다.
fout = open('./relativity.txt', 'xt')
# -> error

try:
    fout = open('./relativity.txt', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity.txt already exists!. That was a close one.')

