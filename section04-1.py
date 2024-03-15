# 데이터 타입
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
V_set = {7, 8, 9}

print(type(v_tuple))
print(type(V_set))
print(type(v_float))

# 숫자
i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999
big_int2 = 77777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.
f4 = '문자열'

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)
print(f4)

result = f3 + i2
print(result, type(result))

## 형변환: int, float, complex ...
a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))

## 단항연산자
y = 100
y += 100
print(y)

## 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8) # 100을 8로 나눠서 n에 몫, m에 나머지

import math

print(math.ceil(5.1)) # 파라미터보다 가장 큰 정수
print(math.floor(6.5)) # 파라미터보다 가장 작은 정수
