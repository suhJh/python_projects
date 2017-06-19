def my_deco(func):
    def decored_func(*args, **kwargs):
        print('\n\n\n************** ', func.__name__, ' **************')
        result = func(*args, **kwargs)
        print('*******************************************\n\n\n')
        return result
    return decored_func

def my_printer(func):
    def target_func(*args, **kwargs):
        print(func(*args, **kwargs))
    return target_func

guess_me = 7
@my_deco
@my_printer
def is_higher_than_7(a):
    if a > guess_me:
        return 'too high'
    elif a < guess_me:
        return 'too low'
    else:
        return 'just right'

is_higher_than_7(guess_me)

start = 1

while True:
    is_higher_than_7(start)
    if start == 7:
        break
    start = start + 1
else:
    print('no break operated')


#4-3
for it in [3, 2, 1, 0]:
    print(it)

#4-4
jjaksu = [number for number in range(10) if number % 2 == 0 and number != 0]
print(jjaksu)

#4-5
squares = {number: number ** 2 for number in range(10)}
print(squares)

#4-6
holsu = {number for number in range(10) if number%2 != 0}
print(holsu)

#4-7
for thing in ('GOT %s' % number for number in range(10)):
    print(thing)

#4-8
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

#4-9
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)