
def formatting(func):
    def new_function(*args, **kwargs):
        print('*************', func.__name__, '**********')
        result = func(*args, **kwargs)
        print('******************************************')
        return result



short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a aposition between 0 and ', len(short_list)-1, ' but got', position)



while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad Index: ', position)
    except Exception as other:
        print('Something eles broke: ', other)
else:
    print('break가 눌러지지 않았습니다.')

