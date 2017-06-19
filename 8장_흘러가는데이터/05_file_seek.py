'''파일의 위치(파일이 저장된 경로가 아닌...) 찾기'''

fin = open('./bfile.txt', 'rb')
print(fin.tell())

'''
seek(offset, origin)
origin == 0: 기본값 시작위치에서 오프셋으로 이동
origin == 1: 현재 오프셋에서 이동
origin == 2: 마지막 위치에서 offset 전으로 이동
'''
import os
print(os.SEEK_SET)  # 0
print(os.SEEK_CUR)  # 1
print(os.SEEK_END)  # 2

fin.seek(255)   # 해당 오프셋으로 이동

bdata = fin.read()
print(len(bdata))
fin.close()


