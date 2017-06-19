def menu(wine, entree, dessert='기본디저트'):
    return {
        'wine': wine,
        'entree': entree,
        'dessert': dessert
    }

print(menu(entree='beef', dessert='젤리', wine='그냥 와인'))
print(menu('와인!', '엔트리!!'))



def print_args(*args):
    print('It is like a arguments in javascript: ', args)

print_args()
print_args('a', 1, 34, 3.2, 'C8', {'a':'b'}, ('Tu1', 'Tu2'), {1,2,3,4})


def print_more(required1, required2, *args):    # 관용적으로 args라고 사용한다.
    print('Need this one: ', required1)
    print('Need this one too: ', required2)
    print('All the rest: ', args)

print_more('필요한 것1', '필요한 것2', {'필요해?':'아니'}, 1, 2, 4)



def print_kwargs(**kwargs):     # 관용적으로 kwargs라고 쓴다.
    print('keyword arguments', kwargs)

print_kwargs(wine='와인', entree='엔트리', arg3="arg3")

