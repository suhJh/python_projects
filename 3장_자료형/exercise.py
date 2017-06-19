

years = list()
years.append(1980)
years.append(1981)
years.append(1982)
years.append(1983)
years.append(1984)
print('3-1: ', years)
print('3-2: ', years[2])
print('3-3: ', years[-1])


things = ["mozzarella", "cinderella", "salmonella"]
print('3-4 :', things)

for stuff in things:
    print('3-5', stuff.capitalize())
    print('3-6', stuff.upper())

surprise = ['Groucho', "Chico", "Harpo"]

print('3-9: ', surprise[-1].lower().swapcase().capitalize())



e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

print('3-10: ', e2f['walrus'])
print('3-11: ', e2f.items())
print('3-12: ', e2f.keys())
print('3-13: ', e2f.values())

life = {
    'animals': {
        'cats': {'Henry', 'Grumpy', 'Lucy'},
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

print('3-15: ', life)
print('3-15: ', life['animals']['cats'])
