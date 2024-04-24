"""
파이썬에는 시퀀스 자료형에 특정 값이 포함되어있는지 판단할 수 있는 멤버 연산자가 존재한다.
in, not in
"""

"""
문자열, 리스트
"""
fruits = ['사과', '바나나', '딸기', '포도']
print('사과' in fruits)  # True
print('배' in fruits)  # False

a = 'hello world'
print('h' in a)  # True
print(' ' in a)  # True
print('hello' in a)  # True

"""
dict는 기본적으로 key의 포함 여부를 판단할 수 있으며,
메서드를 통해 value의 포함 여부를 판단할 수 있다.
"""
b = {'key1': 1, 'key2': 2}
print('key1' in b)  # True
print('key3' in b)  # False
print(1 in b)  # False

print(1 in b.values())  # True

"""
set은 집합이 아닌, 각각의 요소의 포함 여부만 판단할 수 있다.
"""
c = {10, 20, 30}
print(10 in c)  # True
print({10} in c)  # False
print({10, 20} in c)  # False
