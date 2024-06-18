import sqlite3

# DB에 연결하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

# 데이터 조회
cur.execute('SELECT * FROM users')

# 데이터 가져오기
rows = cur.fetchall()
#print(rows)

# 결과 포맷팅
for row in rows:
    print('이름:', row[1])
    
# 연결 닫기
conn.close()