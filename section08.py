# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1-클래스 사용
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233

# 사용2-클래스
from pkg.fibonacci import *

# 사용3-클래스
from pkg.fibonacci import Fibonacci as fb
fb.fib(300) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 

# 사용4-함수
import pkg.calculations as c
print(c.add(10, 100)) # 110

# 사용5-함수
from pkg.calculations import div as d
print(d(10, 2)) # 5.0