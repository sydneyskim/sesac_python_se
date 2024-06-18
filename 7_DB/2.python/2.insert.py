import sqlite3

# DB에 연결하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

# 테이블에 데이터가 있는지 확인하기 위한 쿼리문
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(count)
print(f'현재 데이터 갯수: {count}')

if count == 0:
    # 커서를 통해서 명령어 보내기
    cur.execute('INSERT INTO users (name, age) VALUES ("Alice", 30)')

    cur.execute('INSERT INTO users (name, age) VALUES (?,?)', ('Bob',25))

    # 커밋
    conn.commit()
else:
    # 연결 닫기
    conn.close()
    
print(f'현재 데이터 갯수: {count}')