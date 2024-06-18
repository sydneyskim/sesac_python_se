import db_crud as db

# 데이터 메인 함수
def main():
    # 테이블 생성 함수
    db.create_table()
    
    # 데이터 삽입 함수
    db.insert_user('Alice', 30)
    db.insert_user('Bob', 35)
    db.insert_user('Charlie', 40)
    
    # 데이터 조회 함수
    print(' --데이터 조회-- ')
    users = db.fetch_user()
    for users in users:
        print(users)
    print(' --데이터 조회 끝-- ')
    
    # 데이터 업데이트 함수
    db.update_user('Alice', 25)
    
    print(' --앨리스 나이 변경 이후 조회-- ')
    users = db.fetch_user()
    for users in users:
        print(users)
    print(' --앨리스 나이 변경 이후 조회 끝-- ')
    
    # 데이터 삭제 함수
    db.delete_user('Charlie')
    
    print(' --찰리 삭제 이후 조회-- ')
    users = db.fetch_user()
    for users in users:
        print(users)
    print(' --찰리 삭제 이후 조회 끝-- ')
    
if __name__ == "__main__":
    main()