# 반복문

v1 = 1

while v1 < 11:
    print("v1 is: ", v1)
    v1 += 1

for v2 in range(10): # 0 ~ 9
    print("v2 is: ", v2)

for v3 in range(1, 10): # 1 ~ 9
    print("v3 is: ", v3)

## 1 ~ 100 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print(sum1) # 5050

## 시퀀스(순서가 있는) 자료형 반복
### 문자열, 리스트, 튜플, 집합, 사전
### iterable 리턴 함수: range, reversed, enumerate, filter, map, zip
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]
for v in names:
    print("You are: ", v)

word = "dreams"
for s in word:
    print("Word: ", s)

my_info = {
    'name': 'kim',
    'age': 33,
    'city': 'seoul'
}
for key in my_info:
    print("my_info", key)
for key in my_info.keys():
    print("my_info", key)
for value in my_info.values():
    print("my_info", value)
for k, v in my_info.items():
    print("my_info", k, v)

## break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found: 33!")
        break
    else:
        print("not found: 33!")

## for - else 구문: 반복문이 끝까지 반복된 경우, 마지막 반복 후에 else 블럭 실행
for num in numbers:
    if num == 37:
        print("found: 37!")
        break
    else:
        print("not found: 37!")
else:
    print("NOT FOUND....")


## continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입: ", type(v))