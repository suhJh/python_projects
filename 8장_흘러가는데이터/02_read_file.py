''' 파일 읽기 '''


# 파일 용량이 크면 메모리가 소비되므로 주의
fin = open('./relativity.txt', 'rt')
poem = fin.read()
fin.close()
print('1', len(poem))


# 끊어서 읽기
poem = ''
fin = open('./relativity.txt', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print('2', len(poem))

# 라인단위로 읽기
poem = ''
fin = open('./relativity.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
print('3', len(poem))



# 파일을 읽는 가장 쉬운 방법
poem = ''
fin = open('./relativity.txt', 'rt')
for line in fin:
    poem += line
fin.close()
print('4', len(poem))


# 한 번에 모든 라인을 읽고, 한 라인으로 된 문자열들의 리스트를 반환하는 함수
poem = ''
fin = open('./relativity.txt', 'rt')
lines = fin.readlines()
fin.close()
print('5', len(lines), 'lines read')    # 라인의 갯수를 반환한다.
for line in lines:
    print(line, end='\n')

