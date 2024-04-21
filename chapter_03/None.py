"""
python에서 아무런 값도 할당되지 않는 변수는 None 타입을 가진다.
None 변수에 할당할 수 있는 값은 None이 유일하다.
"""
a = None
print(a)  # None

"""
None 타입은 사칙연산이 불가능하다.
"""
# None + 5
# None + None
# None = 10

"""
메모리에 저장된 None은 하나이다.
따라서 None이 할당된 변수는 항상 같은 주소를 참조한다.
"""
x = None
y = None
print(id(x), id(y))  # 140718282976400 140718282976400

"""
변수가 None인지 확인하는 방법은
== 보다는 is None이 권장된다.
"""
print(x == None)  # True
print(x is None)  # True







