import sqlite3

def init_db():
    # 테이블 생성 코드 추가
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS movielist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rank INTEGER,
                    title TEXT,
                    audience INTEGER,
                    link TEXT)''')
    
    conn.commit()
    
    return conn, cur

def save_to_db(conn, cur, rank, title, audience, link):
    # 영화별 db에 삽입
    cur.execute('''INSERT INTO movies (rank, title, audience, link) 
                   VALUES (?, ?, ?, ?)''', (rank, title, audience, link))
    conn.commit()
    
def query_movie():
    # 영화 목록 모두다 출력하기
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies')
    rows = cur.fetchall()
    for row in rows:
        print(f'순위: {row[1]}, 영화제목: {row[2]}, 관객수: {row[3]}')
    
def close_db(conn):
    # db 연결 종료 함수
    conn.close()
