"""
python에서 실수는 float 타입이며, 소수점있는 숫자들이 실수(float)으로 인식된다.
"""

x = 10
y = 10.0
print(type(x), type(y))  # <class 'int'> <class 'float'>

"""
실수와 실수의 사칙연산, 실수와 정수의 사칙연산은 실수를 반환한다.
정수와 정수의 사칙연산도 실수를 반환하는 경우가 있다.
"""
a = 10.0
b = 2.0
c = 2
d = 3
print(a / b, a / c, c / 3, sep=' | ')  # 5.0 | 5.0 | 0.6666666666666666

"""
python의 float 클래스에는 특별한 값을 가진 상수들이 있다.
inf는 양의 무한대, -inf는 음의 무한대를 의미한다.
"""
x = float('inf')
y = float('-inf')
print(x, type(x))  # inf <class 'float'>
print(y, type(y))  # -inf <class 'float'>
