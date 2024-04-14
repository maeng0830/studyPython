"""
입력 받은 문자는 문자열로 처리된다.
age의 값으로 10이 입력될 경우, print(age + age)는 '1010'을 출력한다.
"""
age = input('나이를 입력해주세요.')
print(age + age)  # 1010

"""
print()는 ,를 통해 여러 개의 값을 동시에 출력할 수 있다.
,를 통해 구분된 값들은 사이에 공백을 가진다.
"""
print("hello", "world!")  # hello world!

"""
sep 옵션을 사용하면 값들 사이의 구분자를 지정해줄 수 있다.
end 옵션을 사용하면 출력문의 마지막에 추가할 문자를 지정할 수 있다.
"""
print("제 전화번호는 010', '0000', '0000', sep='-', end='입니다.")  # 제 전화번호는 010-0000-0000입니다.

"""
다양한 방법으로 문자열 포맷을 지정할 수 있다.
"""
# 형식 문자열
name = '홍길동'
age = 33
height = 170.1234
print('나의 이름은 %s입니다. 나이는 %03d이고, 신장은 %01.2f입니다.' % (name, age, height))  # 나의 이름은 홍길동입니다. 나이는 033이고, 신장은 170.12입니다.

# str.format(...)
print('나의 이름은 {}이고, 나이는 {}입니다.'.format(name, age))  # 나의 이름은 홍길동이고, 나이는 33입니다.
print('나의 이름은 {1}이고, 나이는 {0}입니다.'.format(age, name))  # 나의 이름은 홍길동이고, 나이는 33입니다.
print(f'나의 이름은 {name}이고, 나이는 {age}입니다. 그리고 신장은 {height:.2f}입니다.'.format(name=name, age=age, height=height))  # 나의 이름은 홍길동이고, 나이는 33입니다. 그리고 신장은 170.12입니다.

# f-string
print(f'나의 이름은 {name}이고, 나이는 {age}입니다. 그리고 신장은 {height:.2f}입니다.')  # 나의 이름은 홍길동이고, 나이는 33입니다. 그리고 신장은 170.12입니다.

# 정렬
print('Python is [{:15}]'.format('good'))  # 기본 왼쪽 정렬                     Python is [good           ]
print('Python is [{:<15}]'.format('good'))  # 왼쪽 정렬                        Python is [good           ]
print('Python is [{:>15}]'.format('good'))  # 오른쪽 정렬                      Python is [           good]
print('Python is [{:^15}]'.format('good'))  # 가운데 정렬                      Python is [     good      ]
print('Python is [{:-^15}]'.format('good'))  # '-'로 채운 가운데 정렬           Python is [-----good------]
print('당신의 나이는 [{:15}]세'.format(age))  # 숫자의 기본 오른쪽 정렬           당신의 나이는 [             33]세
print('당신의 나이는 [{:<15}]세'.format(age))  # 숫자의 왼쪽 정렬                당신의 나이는 [33             ]세
print('당신의 나이는 [{:>15}]세'.format(age))  # 숫자의 오른쪽 정렬              당신의 나이는 [             33]세
print('당신의 나이는 [{:^15}]세'.format(age))  # 숫자의 가운데 정렬              당신의 나이는 [      33       ]세

print(f'Python is [{'good':15}]')  # 기본 왼쪽 정렬
print(f'Python is [{'good':<15}]')  # 왼쪽 정렬
print(f'Python is [{'good':>15}]')  # 오른쪽 정렬
print(f'Python is [{'good':^15}]')  # 가운데 정렬
print(f'Python is [{'good':-^15}]')  # '-'로 채운 가운데 정렬
print(f'당신의 나이는 [{age:15}]세')  # 숫자의 기본 오른쪽 정렬
print(f'당신의 나이는 [{age:<15}]세')  # 숫자의 왼쪽 정렬
print(f'당신의 나이는 [{age:>15}]세')  # 숫자의 오른쪽 정렬
print(f'당신의 나이는 [{age:^15}]세')  # 숫자의 가운데 정렬
