#   파이썬은 이게 주석이라고 한다.

#   associative array
#   hash
#   hashmap
#   -> dict

#   edit on desktop
#   it works?

empty_dict = {}
empty_dict = {}

bierce = {
    'day': 'A period of twenty-four hours, mstly misspent',
    'positive': 'Mistaken at the top of one\'s voice',
    'misfortune': 'the kind of fortune that never misses',
    'willbedeleted': 'yeah',
    'target': 'willbedeleted',
    'target': 'will override prev data'
}

print(bierce)

del bierce['target']

print(bierce)


bierce.update({'target': 'same as javascript?'})

print(bierce)

print('sjh' in bierce)

bierce.clear()

bierce.update({'a': 1})
bierce.update({'b': 2})
bierce.update({'c': 3})
bierce.update({'d': 4})
bierce.update({'e': 5})

print(bierce)

keys = bierce.keys()
print(keys)
keys = list(keys)
keys.sort()
print(keys)

print(bierce.items())


for name, value in bierce.items():
    print(name, value)
