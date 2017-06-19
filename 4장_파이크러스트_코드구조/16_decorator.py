def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b

#print(add_ints(3, 5))

# 수동할당
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)




def  square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints2(a, b):
    return a + b

add_ints2(3, 5)

