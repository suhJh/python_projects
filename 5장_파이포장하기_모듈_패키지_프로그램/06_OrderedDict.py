quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!'
}

for stooge in quotes:
    print(stooge)   # 순서가 입력한 것과 다르게 나온다.


from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk')
])

for stooge in quotes:
    print(stooge)