"""
일급함수(first_class_function)은 함수를 객체로 취급하는 것을 의미한다.
1. 함수를 변수에 할당할 수 있다.
2. 함수를 자료구조에 저장할 수 있다.
3. 함수를 인자로 사용하거나, 함수의 반환 값으로 사용할 수 있다.
"""


def greet(name):
    return f"Hello {name}"


say_hello = greet
print(say_hello("John"))  # Hello John
##################################################


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


cal = [add, multiply]
print(cal[0](2, 3), cal[1](2, 3))  # 5 6
###################################################


def action(func, target):
    return func(target)


def greet(target):
    return f"Hello {target}"


print(action(greet, "John"))  # Hello John


"""
고차함수(high_order_function)는 함수를 파라미터로 갖거나, 함수를 반환하는 함수를 말한다.
"""


def calculator(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


print(calculator(add, 3, 4), calculator(multiply, 3, 4))  # 7 12
#####################################################################


def calculate_handler(calculate_type):
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    if calculate_type == 'add':
        return add
    elif calculate_type == 'sub':
        return sub
    elif calculate_type == 'mul':
        return mul
    elif calculate_type == 'div':
        return div


calculate_add = calculate_handler('add')
print(calculate_add(5, 6))  # 11



