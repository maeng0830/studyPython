"""
set은 순서가 없으며, 중복을 허용하지 않는 자료형이다.

- set은 중복 원소를 허용하지 않는다.
- set은 원소의 순서가 없다.
- set은 가변적이기 때문에 원소의 추가 및 삭제가 가능하다. 하지만 불변 데이터만 원소로 가질 수 있다(list X, tuple o)
- 해싱을 통해 빠른 검색이 가능하다.
"""

"""
set의 생성
"""
x = {1, 2, 3}
y = {'apple', 'banana', 'cherry'}
print(x)  # {1, 2, 3}
print(y)  # {'apple', 'banana', 'cherry'}

z = set([1, 2, 3, 4])
print(z)  # {1, 2, 3, 4}

string_set = set('apple coffee')
print(string_set)  # {'e', 'l', ' ', 'a', 'c', 'f', 'o', 'p'}

"""
set은 중복을 허용하지 않으며, 인덱싱이 불가능하다.
"""
a = {1, 2, 3, 3, 4, 5, 5, 6, 7}
print(a)  # {1, 2, 3, 4, 5, 6, 7}
# print(a[0])  # TypeError

"""
set의 연산
"""
set1 = {1, 2, 3, 4, 4, 5, 7}
set2 = {5, 6, 7, 8, 9, 10}

# 합집합 -> set들의 모든 원소를 포함하는 set을 반환한다.
union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 교집합 -> set들이 공통으로 갖는 원소를 포함하는 set을 반환한다.
interaction_set = set1 & set2
print(interaction_set)  # {5, 7}

# 차집합 -> 첫 번째 set의 원소 중 두 번째 set에 포함되어 있지 않은 원소만 포함하는 set을 반환한다.
difference_set = set1 - set2
print(difference_set)  # {1, 2, 3, 4}

"""
set의 메소드
"""
set1 = {1, 2, 3, 4}
# add() -> 원소를 추가한다.
set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}

# copy() -> 얕은 복사된 set을 반환한다.
copied_set1 = set1.copy()
print(id(set1), id(copied_set1))  # 2188677353920 2188677357280
print(copied_set1)  # {1, 2, 3, 4, 5}

# remove() -> 특정 원소를 제거한다. 원소가 없으면 KeyError가 발생한다.
set1.remove(5)
print(set1)  # {1, 2, 3, 4}
# set1.remove(5)  # KeyError

# discard() -> 특정 원소를 제거한다. 원소가 없어도 에러를 발생시키지 않는다.
set1.discard(4)
print(set1)  # {1, 2, 3}
set1.discard(4)
print(set1)  # {1, 2, 3}
