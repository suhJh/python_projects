arr = ['some', 'c', "quotes"]
arr2 = sorted(arr)
print(arr, arr2)
print('삭제하기전..', len(arr))

del arr[1]

print('삭제한 후:', len(arr), arr)


arr = tuple(arr);
print('튜플로 바뀐 arr', arr)


someTuple = 'abcd',

print(someTuple)
