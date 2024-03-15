# 클래스 - 상속, 다중상속

# 예제1
class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.tp = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method"'

class Bmw(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self):
        return "Your Car Name: %s" %(self.car_name)
    
class Benz(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self):
        return "Your Car Name: %s" %(self.car_name)
    
    def show(self): # 오버라이딩
        return 'Car Info: %s %s %s' %(self.car_name, self.tp, self.color)

## 일반 사용
model1 = Bmw('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.tp) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__) # {'tp': 'sedan', 'color': 'red', 'car_name': '520d'}

## Method Overriding
model2 = Benz('220d', 'suv', 'black')
print(model2.show()) # Car Info: 220d suv black

## Inheritance Info
print(Bmw.mro()) # [<class '__main__.Bmw'>, <class '__main__.Car'>, <class 'object'>]
print(Benz.mro()) # [<class '__main__.Benz'>, <class '__main__.Car'>, <class 'object'>]


# 예제2 - 다중 상속
class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro()) # [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]