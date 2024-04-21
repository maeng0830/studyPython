"""
python에서 문자열이 할당된 변수는 str 타입을 가진다.
"""

x = 'hello'
y = 'python'

long_str = '''안녕하세요.
저는 땡땡땡입니다.
잘지내봐요.
'''
print(long_str)
# 안녕하세요.
# 저는 땡땡땡입니다.
# 잘지내봐요.

long_str2 = """안녕하세요.
저는 땡땡땡입니다.
잘지내봐요.
"""
print(long_str2)
# 안녕하세요.
# 저는 땡땡땡입니다.
# 잘지내봐요.

"""
문자열은 덧셈과 곱셈 연산이 가능하다.
"""
add_str = x + y
print(add_str)  # hellopython
multiply_str = x * 3
print(multiply_str)  # hellohellohello

"""
문자열을 구성하는 각 문자는 인덱스를 통해 접근할 수 있다.
정방향으로 접근할 경우 0, 1, ... , n
역방향으로 접근할 경우 -n, ... -2, -1
"""
indexStr = '0123456789'
print('indexStr[0] = ', indexStr[0])  # indexStr[0] =  0
print('indexStr[-1] = ', indexStr[-1]) # indexStr[-1] =  9

"""
문자열 슬라이싱은 문자열의 일부분만 추출해내는 작업을 의미한다.
슬라이싱 명령어는 문자열[start:stop:step] 이다. 
stop 인덱스는 추출될 문자열에 포함되지 않는다.
start 값을 생략하면 0, stop 값을 생략하면 마지막 인덱스+1, step 값을 생략하면 1이다.
"""
slicingStr = '0123456789'
print('slicingStr[6] =', slicingStr[6])  # 6, 하나의 값만 사용할 경우, 그 값은 stop의 값으로 인식된다.
print('slicingStr[:] =', slicingStr[:])  # slicingStr[:] =  0123456789
print('slicingStr[::-1] =', slicingStr[::-1])  # slicingStr[::-1] = 9876543210
print('slicingStr[::2] =', slicingStr[::2])  # slicingStr[::2] = 02468

slicingEx1 = 'asd.png'
print('slicingEx1[:-4] =', slicingEx1[:-4])  # slicingEx1[:-4] = asd
print('slicingEx1[-3:] =', slicingEx1[-3:])  # slicingEx1[-3:] = png

sentence = '   Hello, World!   '
result = sentence\
    .strip()\
    .lower()\
    .replace('world', 'python')
print(result)  # hello, python!