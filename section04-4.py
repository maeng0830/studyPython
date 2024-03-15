# 딕셔너리(순서x, 키 중복x, 수정o, 삭제o)

## 선언
a = {'name': 'kim', 'phone': '010-7777-7777', 'birth': 87024}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(a['name']) # kim
print(a.get('name')) # kim
print(a.get('address')) # None
print(b.get(0)) # Hello Python
print(c.get('arr')[1:3]) # [2, 3]

## 추가
a['address'] = 'Seoul'
print(a) # {'name': 'kim', 'phone': '010-7777-7777', 'birth': 87024, 'address': 'Seoul'}
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a) # {'name': 'kim', 'phone': '010-7777-7777', 'birth': 87024, 'address': 'Seoul', 'rank': [1, 3, 4], 'rank2': (1, 2, 3)}

## keys, values, items
print(a.keys()) # dict_keys(['name', 'phone', 'birth', 'address', 'rank', 'rank2'])
print(list(a.keys())) # ['name', 'phone', 'birth', 'address', 'rank', 'rank2']

print(a.values()) # dict_values(['kim', '010-7777-7777', 87024, 'Seoul', [1, 3, 4], (1, 2, 3)])

print(a.items()) # dict_items([('name', 'kim'), ('phone', '010-7777-7777'), ('birth', 87024), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))])
print(list(a.items())) # [('name', 'kim'), ('phone', '010-7777-7777'), ('birth', 87024), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))]

# 집합(순서X, 중복x) -> 다른 자료구조로 변환해서 자주 사용함
print()
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a)) # <class 'set'>
print(c) # {1, 4, 5, 6}

t = tuple(b)
print(t) # (1, 2, 3, 4)
l = list(b)
print(l) # [1, 2, 3, 4]

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8 ,9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합
print(s1.union(s2)) # 합집합
print(s1 | s2) # 합집합
print(s1.difference(s2)) # 차집합
print(s1 - s2) # 차집합

s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3) # {7, 8, 10, 15, 18}
s3.remove(15)
print(s3) # {7, 8, 10, 18}