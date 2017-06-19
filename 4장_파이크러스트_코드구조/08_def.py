def do_nothing():
    pass

do_nothing()

def make_a_sound():
    print('quak')

make_a_sound()


clojure = 1004

def call_clojure():
    print('헐 클로져가 되다니? ', clojure)

call_clojure()




def agree():
    return True


if agree():
    print('함수는 True를 반환했다. True는 캐피털라이즈드 되어있다.')


def echo(anything):
    return anything + '>>>' + anything

print(echo('c888'))



def commentary(color):
    if color == 'red':
        return '빨가면 사과'
    elif color == 'green':
        return '녹색이면 슈렉'
    elif color == 'bee purple':
        return '이게 뭔 색이여?'
    else:
        return '설정해놓은 색이 없습니다.'

print(commentary('red'))




def is_none(thing):
    if thing is None:
        print("It's None", thing)
    elif thing:
        print("It's true", thing)
    else:
        print("It's False")


is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())