class Duck():
    def __init__(self, input_name):
        # __를 붙이면 private으로 바뀐다.
        self.__name = input_name
    @property    
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name



fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'changed name'
print(fowl.name)


print(fowl._Duck__name) # 에러라고 표시는 하지만 실제로 에러는 안난다. 접근이 불가능한 것은 아니다.
