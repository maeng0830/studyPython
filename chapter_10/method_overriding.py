"""
메서드 오버라이딩은 상위 클래스에서 정의된 메소드를 하위 클래스에서 재정의 하는 것을 의미한다.
"""


class Animal:
    def sound(self):
        print("악!")


class Dog(Animal):
    def sound(self):
        print("왈왈!")


class Cat(Animal):
    def sound(self):
        print("냐옹!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()  # 악!
dog.sound()  # 왈왈!
cat.sound()  # 냐옹!

"""
super()를 통해 상위 클래스의 메소드에 접근할 수 있다.
"""
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

student = Student("John", 1)
print(student.name, student.student_id)  # John 1
