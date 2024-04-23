"""
논리 연산자는 여러 조건을 평가하여 하나의 boolean 값을 반환한다.
"""

"""
and는 논리 곱 연산자이다.
"""
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

"""
or는 논리 합 연산자이다.
"""
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

"""
not은 조건에 대한 평가의 반대 값을 반환한다.
"""
print(not True)
print(not False)

########################################################################################################################

"""
논리 연산자는 연산의 결과가 확정된 시점의 값을 반환한다.
논리 연산의 결과가 확정된 시점에서 평가를 중단하는 것을 단락평가라고 한다.
"""

"""
and
"""
a = 'hello'
b = ''
print(a and b)  # ''

a = 'hello'
b = 'world'
print(a and b)  # 'world'

a = ''
b = 'world'
print(a and b)  # ''

def test1():
    print("test1() 호출")
    return False

def test2():
    print("test2() 호출")
    return True

print(test1() and test2())  # test2() 호출 안됨.
# test1() 호출
# False

lst = []
if lst and lst[0] > 3:
    print("리스트의 첫 번쨰 원소는 3보다 큽니다.")  # 에러가 발생하지 않음

"""
or
"""
a = 'hello'
b = ''
print(a or b)  # 'hello'

a = 'hello'
b = 'world'
print(a or b)  # 'hello'

a = ''
b = 'world'
print(a or b)  # 'world'

username = ''
print(username or '이름을 정하지 않았습니다.')  # 이름을 정하지 않았습니다.
username = '홍길동'
print(username or '이름을 정하지 않았습니다.')  # '홍길동'

########################################################################################################################
"""
논리연산자의 우선순위는 not > and > or 이다.
"""
a = True
b = False
c = False
print(a or b and c)  # True

a = True
b = False
c = False
d = True
print(a and b or c and d)  # False

a = True
b = False
c = False
d = True
print(a and not b or c and d)  # True