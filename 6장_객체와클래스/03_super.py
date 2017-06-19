class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    # 자식 클래스에서 __init__()을 호출하게 되면 부모의 __init__은 실행되지 않으므로 이렇게 명시적으로 실행시켜줘야 한다.
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        # self.name 은 상속이 아닌게 된다.

bob = EmailPerson('봡', 'bob@naver.com')

print(bob.email)
print(bob.name)