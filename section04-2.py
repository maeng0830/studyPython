# 문자열

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

## Raw String
raw_s1 = r'C:\Programs\Test\Bin' # r을 적용하면 이스케이프를 문자로 인식
print(raw_s1)

## 멀티라인
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

## 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'Niceman'
print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4) # True
print('f' in str_o4) # False
print('z' not in str_o4) # True

## 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

## 문자열 함수
# a = 'niceman'
# b = 'orange'

# print(a.islower()) # True
# print(a.endswith('e')) # False
# print(b.endswith('e')) # True
# print(a.capitalize()) # Niceman
# print(a.replace('nice', 'good'))
# print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']

## 문자열 슬라이싱
a = 'niceman'
b = 'orange'

print(a[0:3]) # 0부터 3 이전까지
print(a[0:4])
print(a[0:len(a)])
print(a[:4]) # 처음부터 4 이전까지
print(a[:]) # 처음부터 끝까지

