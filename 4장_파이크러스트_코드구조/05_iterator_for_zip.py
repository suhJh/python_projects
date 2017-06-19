rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current = current + 1


for rabbit in rabbits:
    print(rabbit)

for letter in 'this is word':
    print(letter)

some_dictionary = {
    'dic_key1': 'dic_val1',
    'dic_key2': 'dic_val2',
    'dic_key3': 'dic_val3',
    'dic_key4': 'dic_val4',
    'dic_key5': 'dic_val5',
}

for k, v in some_dictionary.items():
    print(k, v)


cheeses = []
for cheese in cheeses:
    print('this shop has some lovely ', cheese)
    break
else:   #   break확인용도로 사용하면 좋다.
    print('this is not much of a cheese shop. is it?')



days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']  # 위의 배열과 크기가 다르므로 안나온다.

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, fruit, drink, dessert)


english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi', '???'

print(list(zip(english, french)))
print(dict(zip(english, french)))