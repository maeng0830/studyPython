class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("음수는 불가능합니다.")

        self._age = value


"""
@property는 클래스의 메서드를 필드처럼 접근할 수 있게 해준다.
"""
personA = Person("John", "Doe")
print(personA.full_name)  # John Doe

"""
@property와 조합하여, setter를 사용할 수 있다.
setter는 필드의 값을 할당할 때 필요한 로직을 구현하는데 사용된다.
@property가 적용된 메소드명.setter로 사용할 수 있다.
"""
personB = Person("James", "Joe")
personB.age = 32
print(personB.age)  # 32

########################################################################################################################
"""
덕 타이핑은 클래스 및 객체가 제공하는 변수, 메소트에 따라 타입이 결정된다는 개념이다.
"""
def crying(obj):
    obj.crying()


class Cat:
    @staticmethod
    def crying():
        print('야옹')


class Dog:
    @staticmethod
    def crying():
        print('멍멍')


crying(Dog)  # 멍멍
crying(Cat)  # 야옹



