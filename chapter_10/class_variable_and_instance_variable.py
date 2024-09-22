"""
-클래스 변수는 클래스 바로 하위에 정의되는 변수들이다.
-클래스 변수는 클래스가 로드될 때 생성된다.
-클래스 변수는 클래스명 또는 인스턴스명을 통해 참조할 수 있다.
-클래스 변수는 해당 클래스의 모든 인스턴스들이 공유한다.
    - 클래스를 통해 클래스 변수의 값을 변경할 경우, 모든 인스턴스의 변수 값이 바뀐다.
    - 또한 인스턴스를 통해 클래스 변수의 값을 변경할 경우, 클래스 변수와 동일한 이름의 인스턴스 변수를 생성하게 된다.
    - 단 클래스 변수가 객체를 참조할 때는, 단순히 객체의 값을 변경할 때가 아니라 새로운 객체를 할당할 때 클래스 변수와 동일한 인스턴스 변수를 생성하게 된다.

- 파이썬의 속성 접근 우선 순위
  1. 인스턴스 속성
  2. 클래스 속성
  3. 상속된 클래스 속성
"""

class Car:
    max_speed = 300
    max_people = 5
    option = ['camera', 'navigation']

modelx = Car()
modely = Car()

print(Car.max_speed)  # 300
print(modelx.max_speed)  # 300
print(modely.max_speed)  # 300

Car.max_speed = 400
print(Car.max_speed)  # 400
print(modelx.max_speed)  # 400
print(modely.max_speed)  # 400

modely.max_speed = 500
print(Car.max_speed)  # 400
print(modelx.max_speed)  # 400
print(modely.max_speed)  # 500

Car.max_speed = 600
print(Car.max_speed)  # 600
print(modelx.max_speed)  # 600
print(modely.max_speed)  # 500

############# 클래스 변수가 객체일 때 ################
Car.option.append('airbag')
print(Car.option)  # ['camera', 'navigation', 'airbag']
print(modelx.option)  # ['camera', 'navigation', 'airbag']
print(modely.option)  # ['camera', 'navigation', 'airbag']

modely.option.append('advanced_sound')
print(Car.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound']
print(modelx.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound']
print(modely.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound']

modely.option = ['advanced_package']
print(Car.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound']
print(modelx.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound']
print(modely.option)  # ['advanced_package']

Car.option.append('cruz')
print(Car.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound', 'cruz']
print(modelx.option)  # ['camera', 'navigation', 'airbag', 'advanced_sound', 'cruz']
print(modely.option)  # ['advanced_package']

"""
-인스턴스 변수는 클래스가 아닌 각각의 인스턴스에 개별적으로 할당된 변수를 의미힌다.
-인스턴스 변수는 인스턴스가 생성될 때 생성된다.
-인스턴스 변수는 self가 위치한 어디서나 선언이 가능하지만, 보통 __init__ 함수(생성자) 안에서 선언한다.
-인스턴스 변수는 인스턴스를 통해서만 접근할 수 있다.
"""

class Student:
    country = 'KOR'

    def __init__(self, gender, age, name):
        self.gender = gender
        self.age = age
        self.name = name

s1 = Student('male', '12', 'ho')
s2 = Student('female', '15', 'hu')

print(s1.gender, s1.age, s1.name)  # male 12 ho
print(s2.gender, s2.age, s2.name)  # female 15 hu