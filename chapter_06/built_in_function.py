"""
Built-in Functions(내장함수)는 파이썬에 기본적으로 포함되어있는 함수들을 말한다.
"""

"""
all()은 iterable 객체를 인수로 받아, iterable 객체의 모든 요소가 True일 때 True를 반환한다.
any()는 iterable 객체를 인수로 받아, iterable 객체의 요소 중 하나라도 True일 때, True를 반환한다.
"""
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False
print(any([False, False, False]))  # False
print(any([False, True, False]))  # True

"""
chr()는 정수를 인수로 받아, 인수를 유니코드로 인식하여 해당하는 문자를 반환한다.
ord()는 문자를 정수로 받아, 인수에 해당하는 유니코드를 반환한다.
"""
print(chr(65))  # 'A'
print(chr(97))  # 'a'
print(ord('A'))  # 65
print(ord('a'))  # 97

"""
map()은 iterable 객체와 특정한 로직(함수)를 인자로 받고, iterable 객체의 각 요소에 로직(함수)를 적용한 결과를 map의 형태로 반환한다.
map 객체는 list, tuple, set 등의 객체로 변환할 수 있으며 dict로 변환하기 위해서는 요소가 (key, value) 형태여야 한다.
"""
def f1(value):
    if not isinstance(value, int):
        value = int(value)
    return value + 1

print(map(f1, [1, 2, 3, 4]))  # <map object at 0x00000140E8218CA0>
print(list(map(f1, [1, 2, 3, 4])))  # [2, 3, 4, 5]
print(list(map(f1, (1, 2, 3, 4))))  # [2, 3, 4, 5]
print(list(map(f1, '1234')))  # [2, 3, 4, 5]
print(list(map(f1, {"1": 11, "2": 12, "3": 13, "4": 14})))  # [2, 3, 4, 5], 기본적으로 dict를 map에 적용할 경우 key를 반복한다.
print(list(map(f1, {"1": 11, "2": 12, "3": 13, "4": 14}.values())))  # [12, 13, 14, 15]

"""
filter()는 iterable 객체와 특정한 조건을 인자로 받고, iterable 객체의 각 요소 중 조건에 대해 True인 요소만 선택하여 filter 형태로 반환한다. 
filter 객체는 list, tuple, set 등의 객체로 변환할 수 있으며 dict로 변환하기 위해서는 요소가 (key, value) 형태여야 한다.
"""
print(filter(lambda x: x % 2 == 0, range(20)))  # <filter object at 0x000001C43D5996F0>
print(list(filter(lambda x: x % 2 != 0, range(20))))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


"""
range()는 순회할 수 있는 range 객체를 반환한다.
range 객체는 list로 변환할 수 있다.
"""
result = range(1, 10, 2)  # range(시작숫자, 종료숫자, 간격)
print(result)  # range(1, 10, 2)
print(list(result))  # [1, 3, 5, 7, 9]

result = range(10)  # start의 기본 값은 0, 간격의 기본 값은 1 이다.
print(result)  # range(0, 10)
print(list(result))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(result[3])  # 3
print(result[3:7])  # range(3, 7)
print(list(result[3:7]))  # [3, 4, 5, 6]

"""
enumerate()는 iterable 객체의 인덱스와 값을 함께 반환한다.
enumerate 객체는 list, tuple, dict로 변환될 수 있다.
    - list, tuple로 변환할 경우, iterable 객체의 각 요소는 (index, value) 형태가 된다.
    - dict로 변환할 경우, iterable 객체의 각 요소는 index: value 형태가 된다.
"""
result = ['A', 'B', 'C', 'D']
enumerate_result = enumerate(result)
print(list(enumerate_result))  # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]

result = ('A', 'B', 'C', 'D')
enumerate_result = enumerate(result)
print(list(enumerate_result))  # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]

result = {
    "1": 'A',
    "2": 'B',
    "3": 'C',
    "4": 'D',
}
enumerate_result = enumerate(result)
print(list(enumerate_result))  # [(0, '1'), (1, '2'), (2, '3'), (3, '4')]
enumerate_result = enumerate(result)
print(dict(enumerate_result))  # {0: '1', 1: '2', 2: '3', 3: '4'}
enumerate_result = enumerate(result)
print(tuple(enumerate_result))  # ((0, '1'), (1, '2'), (2, '3'), (3, '4'))

enumerate_result = enumerate(result.values())
print(list(enumerate_result))  # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]
enumerate_result = enumerate(result.values())
print(dict(enumerate_result))  # {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
enumerate_result = enumerate(result.values())
print(tuple(enumerate_result))  # ((0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'))
