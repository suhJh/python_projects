class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    # name = property(get_name, set_name) -> @decorator로 정의 가능하다.


fowl = Duck('Howard')
print(fowl.name)


class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property    
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)   # def라고 해서 함수인 것은 아니다. 속성처럼 참조한다.

c.radius = 7
print(c.radius)
print(c.diameter)   # 현재 property의 값을 참조하여 계산된 값을 반환한다.
c.diameter = 20     # 에러: 세터가 없으므로.. 리드온리에 가깝다.