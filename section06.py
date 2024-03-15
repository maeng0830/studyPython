# 함수
## 예제 1
def hello(world):
    print("Hello", world)

hello("Python!")

## 예제 2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

## 예제 3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val1, val2, val3) # <class 'int'> 10000 20000 30000

## 예제 4(리스트 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt) # [10000, 20000, 30000]

## 예제 5(*args, **kwargs)
### *는 파라미터 개수가 정해지지 않은 형태. *는 튜플 형태로 넘어온다.
def args_func(*args):
    for t in args:
        print(t)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

### **는 파라미터 개수가 정해지지 않은 형태. **는 딕셔너리 형태로 넘어온다.
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
kwargs_func(name1='kim', name2='park', name3='lee')

### 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) # 10 20 () {}
example_mul(10, 20, 'kim', 'park', arge1=24, age2=35) # 10 20 ('kim', 'park') {'arge1': 24, 'age2': 35}

## 예제6 - 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(1000)

## 예제7 - hint(문법이 아닌, 개발자의 편의성을 위함)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

func_mul3(10)

## 예제8 - 람다식
### 일반적 함수 -> 객체가 생성됨
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10

print(mul_10) # <function mul_10 at 0x000001C7286062F0>
print(var_func) # <function mul_10 at 0x000001C7286062F0>
print(type(mul_10), type(var_func)) # <class 'function'> <class 'function'>

### 람다 함수 -> 객체 생성X
lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10(10)) # 100

### 함수를 파라미터로 사용
def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, var_func) # 10000
func_final(10, 10, lambda_mul_10) # 10000
func_final(10, 10, lambda num: num * 10) # 10000