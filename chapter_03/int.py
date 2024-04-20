"""
python에서 정수는 int 타입이다.
소수점이 있으면 정수로 인식되지 않는다. 실수(float)로 인식된다.
"""

x1 = 10
y = -10
z = 0
x2 = 10.0

print(type(x1), type(y), type(z), type(x2))  # <class 'int'> <class 'int'> <class 'int'> <class 'float'>

"""
python에서 int는 기본적으로 10진수이지만,
2진수, 8진수, 16진수로 표현할 수 있다.
"""

# 2진수는 숫자 앞에 0b를 붙인다.
x = 0b110
print(x, type(x))  # 6 <class 'int'>

# 8진수는 숫자 앞에 0o를 붙인다.
x = 0o15
print(x, type(x))  # 13 <class 'int'>

# 16진수는 숫자 앞에 0x를 붙인다.
x = 0x1a
print(x, type(x))  # 26 <class 'int'>

# bin(), oct(), hex()를 통해 10진수를 2진수, 8진수, 16진수로 변환할 수 있다.
x = 26
print(bin(x), oct(x), hex(26))  # 0b11010 0o32 0x1a

"""
python은 메모리 효율을 위해 자주 사용하는 정수를 미리 메모리에 저장해두었다.
그 범위는 -5 ~ 256이다.
"""

# 미리 저장된 값를 참조하기 때문에 같은 참조 주소가 같다.
x = 256
y = 256
print(id(x), id(y))  # 140717559540120 140717559540120

# -5 ~ 256을 벗어나면 같은 값을 참조하더라도, 기본적으로 다른 주소를 참조한다.
# .py 파일로 만들어서 실행시키면, -5 ~ 256를 벗어나도 값이 재사용되어 같은 주소를 참조한다.
x = 257
y = 257
print(id(x), id(y))  # 2027120961456 2027120961456