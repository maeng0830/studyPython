# 데이터베이스 연동
import sqlite3
import datetime
print('sqlite3.version: ' , sqlite3.version)
print('sqlite3.sqite_version: ', sqlite3.sqlite_version)

## DB파일 조회(없으면 생성)
conn = sqlite3.connect('C:/study/studyPython/python_basic/resource/database.db')

## 커서 바인딩
c = conn.cursor()

## 데이터 수정
### 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))

### 데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 3})

### 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

### 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

## 데이터 삭제
### 데이터 삭제1
c.execute("DELETE FROM users WHERE id = ?", (7,))

### 데이터 삭제2
c.execute("DELETE FROM users WHERE id = :id", {'id': 8})

### 데이터 삭제3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

### 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

### 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

conn.commit()

conn.close()