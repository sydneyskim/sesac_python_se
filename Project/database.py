import sqlite3

DATABASE = './crmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE) # 데이터 베이스 연결 생성
    conn.row_factory = sqlite3.Row # 행을 sqlite3.Row 객체 타입으로 반환하도록 설정
    return conn # 연결 객체 반환

def get_query(query, params=()):
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

def get_users(page, per_page):
    offset = (page - 1) * per_page
    query = """
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY ROWID) as row_num FROM users
    ) WHERE row_num > 1 LIMIT ? OFFSET ?
    """
    return get_query(query, (per_page, offset))

def get_user_by_name(name, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Name LIKE ? LIMIT ? OFFSET ?"
    return get_query(query, ('%' + name + '%', per_page, offset))

def get_user_by_gender(gender, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Gender = ? LIMIT ? OFFSET ?"
    return get_query(query, (gender, per_page, offset))

def get_user_by_name_and_gender(name, gender, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Name LIKE ? AND Gender = ? LIMIT ? OFFSET ?"
    return get_query(query, ('%' + name + '%', gender, per_page, offset))

def get_orders(page, per_page):
    offset = (page - 1) * per_page
    query = """
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY ROWID) as row_num FROM orders
    ) WHERE row_num > 1 LIMIT ? OFFSET ?
    """
    return get_query(query, (per_page, offset))

def get_orderItems(page, per_page):
    offset = (page - 1) * per_page
    query = """
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY ROWID) as row_num FROM orderitems
    ) WHERE row_num > 1 LIMIT ? OFFSET ?
    """
    return get_query(query, (per_page, offset))

def get_items(page, per_page):
    offset = (page - 1) * per_page
    query = """
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY ROWID) as row_num FROM items
    ) WHERE row_num > 1 LIMIT ? OFFSET ?
    """
    return get_query(query, (per_page, offset))

def get_stores(page, per_page):
    offset = (page - 1) * per_page
    query = """
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY ROWID) as row_num FROM stores
    ) WHERE row_num > 1 LIMIT ? OFFSET ?
    """
    return get_query(query, (per_page, offset))