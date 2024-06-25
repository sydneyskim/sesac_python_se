import sqlite3

DATABASE = './crmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE) # 데이터 베이스 연결 생성
    conn.row_factory = sqlite3.Row # 행을 sqlite3.Row 객체 타입으로 반환하도록 설정
    return conn # 연결 객체 반환

def get_query(query, params):
    conn = get_db_connection() # 데이터 베이스 연결 생성
    cur = conn.cursor() # 커서 객체 생성
    cur.execute(query, params) # 쿼리 실행
    result = cur.fetchall() # 모든 결과 가져오기
    result = [dict(row) for row in result]
    conn.close() # 연결 닫기
    
    # 첫 번째 행이 헤더라면 제외
    if result and result[0].get('Id') == 'Id':
        result = result[1:]
    
    return result # 결과 반환

# def execute_query(query, params):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute(query, params)
#     conn.commit() # 변경 사항 커밋
#     conn.close()
    
def get_users():
    return get_query("SELECT * FROM users", ())

def get_user_by_name(name):
    return get_query("SELECT * FROM users WHERE Name LIKE ?", ('%' + name + '%',))