import sqlite3

# 사용자 DB
DATABASE= 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE) # 데이터베이스 연결 생성
    conn.row_factory = sqlite3.Row # 행을 sqlite3.Row 객체 타입으로 반환하도록 설정
    return conn # 연결 객체 반환

def get_query(query, params):
    conn = get_db_connection() # 데이터베이스 연결 생성
    cur = conn.cursor() # 커서 객체 생성
    cur.execute(query, params) # 쿼리 실행
    result = cur.fetchall() # 모든 결과 가져오기
    conn.close() # 연결 닫기
    return result # 결과 반환

def execute_query(query, params):
    conn = get_db_connection() # 데이터베이스 연결 생성
    cur = conn.cursor() # 커서 객체 생성    
    cur.execute(query, params) # 쿼리 실행
    conn.commit() # 변경 사항 커밋
    conn.close() # 연결 닫기
    
def init_db():
    conn = get_db_connection() # 데이터베이스 연결 생성
    cur = conn.cursor() # 커서 객체 생성
    
    # 사용자 테이블 생성
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT)
    ''')
    
    # 기본 사용자 추가
    cur.execute("SELECT COUNT(*) as count from users")
    count = cur.fetchone()["count"]
    if count == 0:
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user1', 'password1'))
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user2', 'password2'))
        conn.commit()
        
    # 데이터 조회
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    print('-' * 30)
    for row in rows:
        print(row['id'], row['username'], row['password'])
    print('-' * 30)
    
    # 게시판 테이블 생성
    cur.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id))
    ''')
    
    # 기본 게시글 추가
    cur.execute("SELECT COUNT(*) FROM posts")
    count = cur.fetchall()["count"]
    if count == 0:
        cur.execute('INSERT INTO posts (title, content, user_id) VALUES(?,?,?)', ("first post", "first post's content", 1))
        cur.execute('INSERT INTO posts (title, content, user_id) VALUES(?,?,?)', ("second post", "second post's content", 2))
        
    # 게시글 데이터 조회
    cur.execute('SELECT * FROM posts')
    row = cur.fetchall()
    print('-' * 30)
    for row in rows:
        print(row['id'], row['title'], row['content'], row['user_id'], row['created_at'])
    print('-' * 30)
    
    conn.close()