import sqlite3

# DB에 연결하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

cur.execute('''
    UPDATE users SET age = ? WHERE name = ?
''', (35, 'Alice'))

conn.commit()
conn.close()