# 클래스 - self, 클래스, 인스턴스 변수

## 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name: ", self.name)
    
user1 = UserInfo('kim')
user1.user_info_p()
user2 = UserInfo('park')
user2.user_info_p()

print(id(user1)) # 1896452053424
print(id(user2)) # 1896452053536
print(user1.__dict__) # {'name': 'kim'}
print(user2.__dict__) # {'name': 'park'}

## 예제2 - self의 이해
class SelfTest:
    def function1(): # 클래스 함수
        print('function1 called!')
    def function2(self): # 인스턴스 함수
        print('function2 called!')

self_test = SelfTest()
SelfTest.function1() # function1 called!
self_test.function2() # function2 called!

## 예제3 - 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name): # 생성자
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self): # 인스턴스 제거 시 호출
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('Lee')

print(user1.__dict__) #인스턴스 네임스페이스
print(user2.__dict__) # 인스턴스 네임스페이스
print(user3.__dict__) # 인스턴스 네임스페이스
print(WareHouse.__dict__) # 클래스 네임스페이스 <= 클래스변수(공유)

print(user1.name) # kim
print(user2.name) # park
print(user3.name) # Lee
print(user1.stock_num) # 3
print(user2.stock_num) # 3
print(user3.stock_num) # 3

del user1
print(WareHouse.stock_num) # 2