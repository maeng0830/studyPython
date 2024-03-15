# 데이터베이스 연동
import sqlite3
import datetime
print('sqlite3.version: ' , sqlite3.version)
print('sqlite3.sqite_version: ', sqlite3.sqlite_version)

## DB파일 조회(없으면 생성)
conn = sqlite3.connect('C:/study/studyPython/python_basic/resource/database.db')

## 커서 바인딩
c = conn.cursor()

## 데이터 조회(전체)
c.execute("SELECT * FROM users")

## 커서 위치 변경
# print('One -> \n', c.fetchone())

## 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

## 전체 로우 선택
# print('All -> \n', c.fetchall())

print()

## 순회
### 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

### 순회2
# for row in c.fetchall():
#     print('retrieve1 > ', row)

### 순회3
for row in c.execute('SELECT * FROm users ORDER BY id desc'):
    print('retrieve1 > ', row)

print()

## where Retrive
### WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

### WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

### WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

### WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

### WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

### WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    with open('C:/study/studyPython/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')