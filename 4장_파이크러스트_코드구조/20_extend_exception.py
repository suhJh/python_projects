
class UppercaseException(Exception):
    pass


words = ['eeeenie', 'meenie', 'miny', 'MO']
for word in words:
    try:   
        if word.isupper():
            raise UppercaseException(word)
    except UppercaseException as exc:
        print('err발생')
        print(exc)
        
    