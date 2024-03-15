# 파이썬 예외처리의 이해

# 예외 종류
# 문법적 에러가 없지만, 코드 실행(런타임) 시점에 발생하는 예외 처리도 중요
# linter: 코드 스타일, 문법 체크

# SyntaxError: 잘못된 문법
# print('test)
# if True
#     pass
# x => y

# NameError: 참조변수 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError: 0 나누기 에러
# print(10/0)

# IndexError: 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])

# KeyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby']) # KeyError
print(dic.get('hobby')) # None

# AttributeError: 모듈, 클래스에 있는 잘못된 속성, 메소드 사용
import time
print(time.time())
# print(time.month()) # month()는 없는 함수 -> AttributeError

# ValuError: 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open('test.txt', 'r')

# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y)
# print(x + z)

# 항상 예외가 발생하지 않을 것이라고 가정하고 먼저 코딩
# 이 후 런타임 시 예외가 발생하면 예외 처리(EAFP 코딩 스타일)

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드
# except: 에러명1이 발생했을 때 실행
# except: 에러명2이 발생했을 때 실행
# else: 에러가 발생하지 않았을 경우 실행
# finally" 예외가 발생하든, 발생하지 않든 실행

# 예제1
print()
name = ['kim', 'lee', 'park']

try:
    z = 'kim' # 'cho' -> Error
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else!')

# 예제2 - 어떤 예외가 발생할지 모르는 경우
print()
try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')

# 예제3 - finally
print()
try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('fianlly ok!')

# 예외4 - 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
print()
# try:
#     z = 'cho'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# finally:
#     print('Ok Finally!!!')

# print('예외를 잡지 않아서, 이후의 코드는 실행 안됨')

# 예제5 - finally
print()
try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as e:
    print(e) # 'cho' is not in list
    print('Not found it! - Occurred ValuError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('fianlly ok!')

# 예제6 - raise
print()
try:
    a = 'jim'
    if a == 'kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as e:
    print(e)
else:
    print('Ok!')