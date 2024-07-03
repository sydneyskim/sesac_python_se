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
def get_total_user_by_name(name):
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

# user 상세
def get_userdetail(user_id):
    query = "SELECT * FROM users WHERE Id = ?"
    return get_query(query, (user_id,))

def get_userorderdetail(user_id):
    query = '''
        SELECT 
            o.Id AS OrderId,
            o.OrderAt AS PurchasedDate,
            s.Id AS PurchasedLocation,
            o.UserId AS UserId
        FROM 
            orders o
        JOIN 
            stores s ON o.StoreId = s.Id 
        WHERE UserId = ?;
    '''
    return get_query(query, (user_id,))

# 유저별 자주 방문한 매장
def get_top5_stores(user_id):
    query = '''
        SELECT 
            o.UserId AS UserID,
            o.StoreId AS StoreID,
            s.Name AS StoreName,
            COUNT(o.Id) AS VisitCount
        FROM 
            orders o
        JOIN 
            stores s ON o.StoreId = s.Id
        WHERE 
            o.UserId = ?
        GROUP BY 
            o.UserId, o.StoreId
        ORDER BY 
            VisitCount DESC
        LIMIT 5;
    '''
    return get_query(query, (user_id,))

# 유저별 자주 주문한 상품
def get_top5_items(user_id):
    query = '''
        SELECT 
            o.UserId AS UserID,
            i.Name AS ItemName,
            COUNT(oi.ItemId) AS OrderCount
        FROM 
            orders o
        JOIN 
            orderitems oi ON o.Id = oi.OrderId
        JOIN 
            items i ON oi.ItemId = i.Id
        WHERE 
            o.UserId = ?
        GROUP BY 
            o.UserId, i.Name
        ORDER BY 
            OrderCount DESC
        LIMIT 5;
    '''
    return get_query(query, (user_id,))

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

# Order 날짜 검색결과
def get_order_by_date(date, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM orders WHERE OrderAt LIKE ? LIMIT ? OFFSET ?"
    return get_query(query, ('%' + date + '%', per_page, offset))

# Order 날짜 검색결과 count
def get_total_order_by_date(date):
    query = "SELECT COUNT(*) as count FROM orders WHERE OrderAt LIKE ?"
    result = get_query(query, (date,))
    return result[0]['count'] if result else 0

# order 날짜 검색 결과 count
def get_total_orders():
    query = "SELECT COUNT(*) as count FROM orders"
    result = get_query(query)
    return result[0]['count'] if result else 0

# order 상세(orderitem)
def get_orderitemdetail(order_id):
    query = '''
        SELECT 
            oi.Id AS OrderItemId,
            oi.OrderId AS OrderId,
            oi.ItemId AS ItemId,
            i.Name AS ItemName
        FROM 
            orderitems oi
        JOIN 
            items i ON oi.ItemId = i.Id
        WHERE OrderId = ?;
    '''
    return get_query(query, (order_id,))

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

# orderItem 상세
# order 상세
def get_orderdetail(order_id):
    query = '''
        SELECT 
            "Id" AS OrderId,
            "OrderAt" AS OrderedAt,
            "StoreId" AS StoreId,
            "UserId" AS UserId
        FROM "orders"
        WHERE "Id" = ?;
    '''
    return get_query(query, (order_id,))

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

# item 종류 검색결과
def get_item_by_type(type, page, per_page):
    offset = (page - 1) * per_page
    query = "SELECT * FROM items WHERE Type = ? LIMIT ? OFFSET ?"
    return get_query(query, (type, per_page, offset))

# item 종류 검색결과 count
def get_total_item_by_type(type):
    query = "SELECT COUNT(*) as count FROM items WHERE Type = ?"
    result = get_query(query, (type,))
    return result[0]['count'] if result else 0

# item 상세
def get_itemdetail(item_id):
    query = '''
        SELECT 
            "Name" AS Name , 
            "UnitPrice" AS UnitPrice
        FROM "items"
        WHERE "Id" = ?;
    '''
    return get_query(query, (item_id,))
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

# store 카페명 검색결과
def get_store_by_name(name, page, per_page):
    offset = (page -1) * per_page
    query = "SELECT * FROM stores WHERE Name LIKE ? LIMIT ? OFFSET ? "
    return get_query(query, ('%' + name + '%', per_page, offset))

# store 이름 검색결과 count
def get_total_store_by_name(name):
    query = "SELECT COUNT(*) as count FROM stores WHERE Name LIKE ?"
    result = get_query(query, ('%' + name + '%',))
    return result[0]['count'] if result else 0

# store 상세
def get_storedetail(store_id):
    query = '''
        SELECT 
            "Name" AS Name , 
            "Type" As Type ,
            "Address" AS Address
        FROM "stores"
        WHERE "Id" = ?;
    '''
    return get_query(query, (store_id,))

# 상점별 월간 매출
def get_monthlyrevenue(store_id):
    query = '''
        SELECT 
            o.StoreId AS StoreID,
            strftime('%Y-%m', o.OrderAt) AS OrderMonth,
            SUM(i.UnitPrice) AS TotalRevenue,
            COUNT(o.Id) AS OrderCount
        FROM 
            orders o
        JOIN 
            orderitems oi ON o.Id = oi.OrderId
        JOIN 
            items i ON oi.ItemId = i.Id
        WHERE 
            o.StoreId = ?
        GROUP BY 
            o.StoreId, strftime('%Y-%m', o.OrderAt)
        ORDER BY 
            o.StoreId, OrderMonth;
    '''
    return get_query(query, (store_id,))

# 아이템별 월간 매출
def get_item_monthlyrevenue(item_id):
    query = '''
        SELECT 
            i.Id AS ItemID,
            strftime('%Y-%m', o.OrderAt) AS OrderMonth,
            SUM(i.UnitPrice) AS TotalRevenue,
            COUNT(oi.Id) AS OrderCount
        FROM 
            orders o
        JOIN 
            orderitems oi ON o.Id = oi.OrderId
        JOIN 
            items i ON oi.ItemId = i.Id
        WHERE 
            i.Id = ?
        GROUP BY 
            i.Id, strftime('%Y-%m', o.OrderAt)
        ORDER BY 
            i.Id, OrderMonth;
    '''
    return get_query(query, (item_id,))

# 단골고객 (1번 이상 방문 조건)
def get_regular_customers(store_id):
    query = '''
        SELECT 
            o.StoreId AS StoreId,
            o.UserId AS UserId,
            u.Name AS Name,
            COUNT(o.Id) AS VisitCount
        FROM 
            orders o
        JOIN 
            users u ON o.UserId = u.Id
        WHERE 
            o.StoreId = ?
        GROUP BY 
            o.StoreId, o.UserId
        HAVING 
            VisitCount > 1
        ORDER BY 
            VisitCount DESC;
    '''
    return get_query(query, (store_id,))
