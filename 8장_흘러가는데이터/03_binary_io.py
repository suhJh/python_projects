''' 모드에 b를 포함시키면 파일을 이진 모드로 연다. 문자열 대신 바이트를 읽고 쓸 수 있다.'''

bdata = bytes(range(0, 256))
print(len(bdata))

# 방법 1
fout = open('bfile.txt', 'wb')
fout.write(bdata)
fout.close()

# 방법 2
fout = open('bfile.txt', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()


# 이진데이터 읽기
fin = open('bfile.txt', 'rb') # rt는 텍스트, rb는 바이트
bdata = fin.read()
print(len(bdata))
print(bdata)
fin.close()

    