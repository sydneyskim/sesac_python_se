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
    
    return result # 결과 반환

### Users ###
# user 전체 가져오기
def get_users(page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users LIMIT ? OFFSET ?"
    return get_query(query, (per_page, offset))

# user 전체 count
def get_total_users():
    query = "SELECT COUNT(*) as count FROM users"
    result = get_query(query)
    return result[0]['count'] if result else 0

# user 이름 검색결과
def get_user_by_name(name, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Name LIKE ? LIMIT ? OFFSET ?"
    return get_query(query, ('%' + name + '%', per_page, offset))

# user 이름 검색결과 count
def get_total_user_by_name(name, page, per_page):
    query = "SELECT COUNT(*) as count FROM users WHERE Name LIKE ?"
    result = get_query(query, ('%' + name + '%',))
    return result[0]['count'] if result else 0

# user 성별 검색결과
def get_user_by_gender(gender, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Gender = ? LIMIT ? OFFSET ?"
    return get_query(query, (gender, per_page, offset))

# user 성별 검색결과 count
def get_total_user_by_gender(gender):
    query = "SELECT COUNT(*) as count FROM users WHERE Gender = ?"
    result = get_query(query, (gender,))
    return result[0]['count'] if result else 0

# user 이름&성별 검색결과
def get_user_by_name_and_gender(name, gender, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM users WHERE Name LIKE ? AND Gender = ? LIMIT ? OFFSET ?"
    return get_query(query, ('%' + name + '%', gender, per_page, offset))

# user 이름&성별 검색결과 count
def get_total_user_by_name_and_gender(name, gender):
    query = "SELECT COUNT(*) as count FROM users WHERE Name LIKE ? AND Gender = ?"
    result = get_query(query, ('%' + name + '%', gender))
    return result[0]['count'] if result else 0

### Orders ###
# order 전체 가져오기
def get_orders(page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM orders LIMIT ? OFFSET ?"
    return get_query(query, (per_page, offset))
# order 전체 count
def get_total_orders():
    query = "SELECT COUNT(*) as count FROM orders"
    result = get_query(query)
    return result[0]['count'] if result else 0

### OrderItems ###
# orderItem 전체 가져오기
def get_orderItems(page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM orderItems LIMIT ? OFFSET ?"
    return get_query(query, (per_page, offset))

# orderItem 전체 count
def get_total_orderItems():
    query = "SELECT COUNT(*) as count FROM orderItems"
    result = get_query(query)
    return result[0]['count'] if result else 0

### Items ###
# item 전체 가져오기
def get_items(page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM items LIMIT ? OFFSET ?"
    return get_query(query, (per_page, offset))

# item 전체 count
def get_total_items():
    query = "SELECT COUNT(*) as count FROM items"
    result = get_query(query)
    return result[0]['count'] if result else 0

### Stores ###
# store 전체 가져오기
def get_stores(page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM stores LIMIT ? OFFSET ?"
    return get_query(query, (per_page, offset))

# store 전체 count
def get_total_stores():
    query = "SELECT COUNT(*) as count FROM stores"
    result = get_query(query)
    return result[0]['count'] if result else 0