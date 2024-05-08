"""
def: 함수를 선언하는 키워드이다.
function_name: 함수의 식별자이며, 함수를 호출할 때 사용된다.
parameter: 함수에 입력될 매개변수이다.
logic: 함수가 호출되면 함수 내부에서 수행될 코드이다.
return: logic이 수행된 후, 함수가 반환할 값이다.
pass: 함수 내부에 어떤 로직도, 반환 값도 없는 경우 pass를 함수 내부에 명시해야한다.
"""
import random


def function_name(x, y):
    z = x + y
    return z

result = function_name(1, 2)
print(result)  # 3

"""
파라미터와 반환 값이 없는 함수
"""
def simple_function():
    print("simple_function")

simple_function()  # simple_function

"""
파라미터가 없고, 반환 값이 있는 함수
"""
def get_ten():
    return 10

print(get_ten())  # 10

"""
파라미터가 있고, 반환 값이 없는 함수
"""
def greeting(name):
    print(f'hello {name}!')

greeting('kmk')  # hello kmk!

"""
파라미터와 반환 값이 있는 함수
"""
def calculator_add(x, y):
    return x + y

print(calculator_add(1, 2))  # 3

"""
비어있는 함수
"""
def empty_function():
    pass

print(empty_function())  # None

