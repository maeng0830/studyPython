# 데이터베이스 연동
import sqlite3
import datetime
print('sqlite3.version: ' , sqlite3.version)
print('sqlite3.sqite_version: ', sqlite3.sqlite_version)
## 테이블 생성 및 삽입

### 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime: ', nowDatetime)

### DB 생성 & Auto Commit
conn = sqlite3.connect('C:/study/studyPython/python_basic/resource/database.db', isolation_level=None)

### Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

### 테이블 생성(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

### 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', \
          'kim.com', ?)", (nowDatetime, ))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", 
          (2, 'park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime, ))

### Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

### 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows") # users db deleted :  5 rows

conn.close