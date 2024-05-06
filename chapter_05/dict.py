"""
딕셔너리는 키와 밸류 쌍으로 데이터를 저장하는 자료구조이다.
시퀀스 자료형이 아니기 때문에 인덱싱과 슬라이싱은 불가능하다. 하지만 순서는 존재한다.

- 딕셔너리의 키는 고유해야한다. 키가 중복될 경우 기존 값을 덮어씌운다.
- 딕셔너리의 키는 해싱이 가능한(불변한) 타입이어야한다. 문자열, 숫자, 튜플 등이 사용될 수 있다.
- 딕셔너리는 해싱에 기반하기 때문에 검색에 효율적이다.
"""

"""
딕셔너리의 생성
"""
person = {'name': 'kmk', 'city': 'seoul', 'job': 'developer'}
print(person)  # {'name': 'kmk', 'city': 'seoul', 'job': 'developer'}
person2 = dict([('name', 'kmk'), ('city', 'seoul'), ('job', 'developer')])
print(person2)  # {'name': 'kmk', 'city': 'seoul', 'job': 'developer'}
person3 = dict(name='kmk', city='seoul', job='developer')
print(person3)  # {'name': 'kmk', 'city': 'seoul', 'job': 'developer'}

keys = ['name', 'city', 'job']
values = ['kmk', 'seoul', 'developer']
person4 = dict(zip(keys, values))
print(person4)  # {'name': 'kmk', 'city': 'seoul', 'job': 'developer'}

"""
딕셔너리의 수정
"""
person = {'name': 'kmk', 'city': 'seoul'}
print(person)  # {'name': 'kmk', 'city': 'seoul'}
person['age'] = 10  # 새로운 데이터 추가
print(person)  # {'name': 'kmk', 'city': 'seoul', 'age': 10}
person['city'] = 'paju'  # 기존 밸류 변경
print(person)  # {'name': 'kmk', 'city': 'paju', 'age': 10}

"""
딕셔너리의 메소드
"""
days = dict(월요일='Mon', 화요일='Tue', 수요일='Wed', 목요일='Tur', 금요일='Fri', 토요일='Sat', 일요일='Sun')

# copy() -> 얕은 복사 객체를 반환한다.
days2 = days.copy()
print(id(days), id(days2))  # 2309132123520 2309129039680

# get() -> 없는 키로 접근해도 에러가 발생하지 않는다.
# days['묵요일']  # KeyError: '묵요일'
value = days.get('묵요일')
print(value)  # None
value = days.get('묵요일', 'key를 확인해주세요.')
print(value)  # key를 확인해주세요.

# items() -> key:value의 데이터를 추출한다. 시퀀스 자료형이 아닌 dict_items 객체이며, 리스트로 형변환 가능하다.
days_items = days.items()
print(days_items)  # dict_items([('월요일', 'Mon'), ('화요일', 'Tue'), ('수요일', 'Wed'), ('목요일', 'Tur'), ('금요일', 'Fri'), ('토요일', 'Sat'), ('일요일', 'Sun')])
print(list(days_items))  # [('월요일', 'Mon'), ('화요일', 'Tue'), ('수요일', 'Wed'), ('목요일', 'Tur'), ('금요일', 'Fri'), ('토요일', 'Sat'), ('일요일', 'Sun')]

# keys() -> key 데이터를 추출한다. 시퀀스 자료형이 아닌 dict_keys 객체이며, 리스트로 형변환 가능하다.
days_keys = days.keys()
print(days_keys)  # dict_keys(['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'])
print(list(days_keys))  # ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

# values() -> value 데이터를 추출한다. 시퀀스 자료형이 아닌 dict_values 객체이며, 리스트로 형변환 가능하다.
days_values = days.values()
print(days_values)  # dict_values(['Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat', 'Sun'])
print(list(days_values))  # ['Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat', 'Sun']

# pop() -> 키를 통해 밸류를 반환한다. 해당 key:value 데이터는 딕셔너리에서 삭제된다.
days_pop = days.pop('월요일')
print(days_pop)  # Mon
print(days)  # {'화요일': 'Tue', '수요일': 'Wed', '목요일': 'Tur', '금요일': 'Fri', '토요일': 'Sat', '일요일': 'Sun'}

# popitem() -> 딕셔너리의 마지막 key:value 데이터를 반환한다. 튜플 형태로 반환되며, 해당 데이터는 딕셔너리에서 삭제된다.
days_popitem = days.popitem()
print(days_popitem)  # ('일요일', 'Sun')
print(days)  # {'화요일': 'Tue', '수요일': 'Wed', '목요일': 'Tur', '금요일': 'Fri', '토요일': 'Sat'}
