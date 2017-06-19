periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(periodic_table)

from collections import defaultdict

def no_idea():
    return 'huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

for k, v in bestiary.items():
    print(k, v)

print(bestiary['C'])

food_counter = defaultdict(int) # int는 함수, 마찬가지로 list, set, dict를 입력할 수 있다. generic처럼 사용가능
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)


