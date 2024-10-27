"""
상속은 한 클래스의 특성(field, method)을 다른 클래스가 가져오는 것을 의미한다.
    -자식클래스는 부모클래스의 모든 속성과 메소드를 상속 받는다.
    -자식클래스는 부모클래스의 메소드를 오버라이딩 하거나, 부모클래스는 갖고 있지 않은 필드 및 메서드를 정의할 수 있다.
"""
class Car:
    maxSpeed = 300
    maxPeople = 5

    def move(self):
        print('출발')

    def stop(self):
        print('정지')


class HybridCar(Car):
    battery = 1000
    batteryKm = 300

class ElectricCar(Car):
    battery = 2000
    batteryKm = 600


hybrid_car = HybridCar()
electric_car = ElectricCar()

print(hybrid_car.maxSpeed)  # 600
print(electric_car.maxSpeed)  # 600
print(hybrid_car.battery, hybrid_car.batteryKm)  # 1000 300
print(electric_car.battery, electric_car.batteryKm)  # 2000 600
print('###########################################################')


"""
자식클래스의 생성자에서 super().__init__()를 통해 부모클래스의 생성자를 호출하여 부모클래스의 속성을 초기화할 필요는 없다.
하지만 super().__init__()을 통해 부모클래스의 생성자를 호출하여 속성을 초기화하는 것이 권장된다.
    -단순 속성 초기화 뿐만 아니라, 부모클래스 생성자 내부에 특정한 로직이 존재할 수 있다.
"""

"""
자바와 파이썬의 차이점
    -자바는 자식클래스의 생성자에서 super()를 통해 명시적으로 부모클래스의 생성자를 호출하지 않으면, 부모클래스의 기본생성자(매개변수가 없는 생성자)를 자동으로 호출한다.
    -파이썬은 super().__init__()을 통해 명시적으로 부모클래스의 생성자를 호출하지 않으면, 부모클래스의 생성자는 호출되지 않는다.
"""
class Character:
    max_level = 20

    def __init__(self, name, hp, mp, ad, ap, **kwargs):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.ad = ad
        self.ap = ap
        self.level = 1
        self.status = 'LIVE'

    def move(self, x, y):
        print(f'{self.name} moved to {x}, {y}')

    def ad_attack(self, target):
        print(f'{self.name} ad_attacking {target.name}')
        target.hp -= self.ad
        print(f"{target.name}'s hp is {target.hp}")
        if target.hp <= 0:
            target.status = 'DEAD'
            print(f'{target.name} is dead')

    def ap_attack(self, target):
        print(f'{self.name} ap_attacking {target.name}')
        target.hp -= self.ap
        print(f"{target.name}'s hp is {target.hp}")
        if target.hp <= 0:
            target.status = 'DEAD'
            print(f'{target.name} is dead')


class Champion(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exp = 0

    def get_exp(self, exp):
        self.exp += exp
        print(f'{self.name} get exp({exp})')

        if self.exp >= 100:
            print(f'{self.name} level up!!')
            self.exp = 0
            self.level += 1



"""
파이썬의 super().__init__()은 MRO(Method Resolution Order)에 따라 상속 계층에 속한 클래스들의 super().__init__()을 순차적으로 호출한다.
단 이것은 상속 계층에 속한 클래스들이 자신의 __init__() 내부에서 super().__init__()을 통해 다음 순서 클래스의 생성자를 호출할 때만 가능하다.

다중상속의 경우, 자식클래스를 선언할 때 부모클래스의 명시 순서에 따라 생성자가 먼저 호출될 부모클래스가 결정된다.
아래의 예에서는 Hero 객체를 생성할 때, Unique -> Champion -> Character의 순서대로 상송 계층 클래스들의 생성자가 호출된다.

MRO는 비단 상속 계층에서의 생성자 호출 순서 뿐만 아니라, 상속 받은 여러 개의 동일한 메소드(이름, 파라미터가 동일한) 중 어떤 메소드를 호출할 지를 결정하는데 기준이 된다.
"""
class Unique:
    def __init__(self, hero_stat, **kwargs):
        self.hero_stat = hero_stat
        super().__init__(**kwargs)

    def get_exp(self, exp):
        self.exp += exp * 2
        print(f'{self.name} get exp({exp * 2})')

        if self.exp >= 100:
            print(f'{self.name} level up!!')
            self.exp = 0
            self.level += 2


class Hero(Unique, Champion):
    def __init__(self, name, hp, mp, ad, ap, hero_stat):
        super().__init__(name=name, hp=hp, mp=mp, ad=ad, ap=ap, hero_stat=hero_stat)


hero = Hero('holy_knight', 100, 100, 100, 100, 100)
print(f'{hero.name} has hp: {hero.hp}, mp: {hero.mp}, ad: {hero.ad}, ap: {hero.ap}, hero_stat: {hero.hero_stat}')
hero.get_exp(20)