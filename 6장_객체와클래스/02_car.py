class Car():
    def exclaim(self):
        return "I am a Car"

class Yugo(Car):    # 상속의 방법
    def exclaim(self):
        return "it will override of Car's exclaim"
    def need_a_push(self):
        return "A little help here?"

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())
print(give_me_a_yugo.need_a_push())