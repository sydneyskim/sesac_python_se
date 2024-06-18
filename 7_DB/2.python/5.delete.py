import sqlite3

# DB에 연결하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

cur.execute('DELETE FROM users WHERE name = ?', ('Bob',)) # ,를 찍는 것은 튜플임을 알리기 위한 문법임

conn.commit()
conn.close()
