

myFirstSet = {1, 3, 5, 7, 10, 22, 2, 99, 3, 5, 7, 10}
print(myFirstSet)


drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'},
    'all': {'a'}
}

for name, contents in drinks.items():
    subset = set(contents.copy() & drinks['all'])
    drinks['all'] = subset
    print('result is ', drinks['all'])


for name, contents in drinks.items():
    if 'cream' in contents:
        print('cream', contents)

counter = 0
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        counter = counter + 1
        print('vermouth & orange juice', counter, name)


counter = 0
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        counter = counter + 1
        print(name, contents)


#   a.intersection(b)
inter = drinks['martini'] & drinks['black russian']
print('intersection', inter)

#   a.union(b)
union = drinks['martini'] | drinks['black russian']
print('union', union)

#   a.difference(b)
diff = drinks['martini'] - drinks['black russian']
print('difference', diff)

#   a.symmetric_difference(b)   대칭차집합
sym_def = drinks['martini'] ^ drinks['black russian']
print('sym_def', sym_def)


