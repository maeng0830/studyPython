"""
파이썬의 식별 연산자로는 is, is not이 있다.
"""

"""
is는 두 변수가 같은 주소를 참조하고 있는지 확인하는 연산자이다.
==는 참조 값이 아닌, 값을 비교한다는 점에서 is와 차이가 있다.
"""

"""
문자열 비교
파이썬은 동일한 문자열이 할당된 변수는 동일한 주소를 참조하게 된다. 그러나 반드시 그런 것은 아니며, 문자열의 길이가 길어지거나 자주 사용하는 문자열이 아니면 다른 주소를 참조할 수도 있다.
"""
coffe_employee = 'brand'
orange_employee = 'brand'
print(coffe_employee is orange_employee)  # True
print(coffe_employee == orange_employee)  # True

"""
객체 비교
파이썬은 값이 동일하더라도, 새로 객체가 생성될 경우 다른 주소를 참조하게 된다. 즉 개별적인 객체를 참조하게 되는 것이다.
"""
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True
print(a is b)  # False
print(a == c)  # True
print(a is c)  # True
print(b == c)  # True
print(b is c)  # False

print(id(a), id(b), id(c))  # 2455360950656 2455360952512 2455360950656
