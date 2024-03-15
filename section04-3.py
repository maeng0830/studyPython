# 리스트(순서o, 중복o, 수정o, 삭제o)
## 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

## 인덱싱
print(d[3]) # Banana
print(d[-2]) # Banana
print(d[0] + d[1])
print(e[2][1]) # Banana
print(e[-1][-2]) # Banana

## 슬라이싱
print(d[0:3]) # [10, 100, 'Pen']
print(e[2][1:3]) # ['Banana', 'Orange']

## 연산
print(c + d) # [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']
print(c * 3) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

## 리스트 수정, 삭제
c[1:3] = [100, 1000, 10000] # 1 ~ 3 이전의 값들(인덱스 1, 2)을 새로운 값들로 대체
print(c) # [1, 100, 1000, 10000, 4]

c[1] = ['a', 'b', 'c'] # 1번 인덱스의 값을 새로운 리스트로 대체
print(c) # [1, ['a', 'b', 'c'], 1000, 10000, 4]

del c[1]
print(c) # [1, 1000, 10000, 4]
del c[-1]
print(c) # [1, 1000, 10000]

## 리스트 함수
print()
y = [5, 2, 3, 1, 4]
y.append(6) 
print(y) # [5, 2, 3, 1, 4, 6]
y.sort()
print(y) # [1, 2, 3, 4, 5, 6]
y.reverse()
print(y) # [6, 5, 4, 3, 2, 1]
y.insert(2, 7) # 2번 인덱스에 데이터 삽입. 기존의 2번 인덱스 ~ 끝 인덱스 값들은 뒤로 밀림.
print(y) # [6, 5, 7, 4, 3, 2, 1]
y.remove(2) # remove는 파라미터를 인덱스가 아닌 값으로 인식
y.remove(7)
print(y) # [6, 5, 4, 3, 1]
y.pop() # 마지막 원소 꺼내기
print(y) # [6, 5, 4, 3]
ex = [88, 77]
y.extend(ex)
print(y) # [6, 5, 4, 3, 88, 77]
y.append(ex)
print(y) # [6, 5, 4, 3, 88, 77, [88, 77]]

# 튜플(순서o, 중복o, 수정x, 삭제x)
print()
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2]) # 3
print(c[3]) # 4
print(d[2][1]) # b

print(d[2:]) # (('a', 'b', 'c'),)
print(d[2][0:2]) # ('a', 'b')
print(c + d) # (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))
print(c * 3) # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

## 튜플 함수
z = (5, 2, 1, 3, 1)
print(z)
print(3 in z) # True
print(z.index(5)) # 0
print(z.count(1)) # 2