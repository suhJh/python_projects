
# 리스트 컴프리헨션
number_list = [number for number in range(1, 6)]
print(number_list)


rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)


# 딕셔너리 컴프리헨션
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)    

letter_counts2 = {letter: word.count(letter) for letter in set(word)}



# 셋 컴프리헨션
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)



# 제너레이터 컴프리헨션
number_thing = (number for number in range(1, 6))
print(number_thing)
for number in number_thing:
    print(number)
print(number_thing)