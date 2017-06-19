animal = 'fruitbat'
def print_global():
    print('inside print_global: ', animal)
    # animal = 'wombat'
    # print('after the change: ', animal) # 전역변수의 값을 함수에서 바꾸려고하면 에러가 난다.

print_global()
print('at the top level: ', animal)


def change_and_print_global():
    global animal
    animal = 'wormbat'
    print('inside change_and_print_global: ', animal)

print_global()
change_and_print_global()
print_global()



def check_local_and_global(g1=1, g2=2):
    def some_new_function(l1=3, l2=4):
        print('globals: ', globals())
        print('locals', locals())
    return some_new_function

check_it = check_local_and_global(245, 1453)
check_it(1577356, 13123)