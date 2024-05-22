users = [ # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
    {"name": "Dave", "age": 35, "location": "Jeju", "car": "K5"},
    {"name": "June", "age": 35, "location": "Jeju", "car": "K5"}
]

name = input("찾는 사용자의 이름을 입력하세요: ")

def find_user(name ):
    found_user = []
    for u in users:
        if u['name'].lower() == name.lower():

            found_user.append(u)
    return found_user

found = find_user(name)
print(f"찾은 사용자: {found}")

# 미션1. 이름 + 나이로
def find_user2(name=None, age=None):
    found_user = []
    for u in users:
        if u.get("name").lower() == name.lower() and u.get("age") == age:
            found_user.append(u)
    return found_user

found = find_user2("alice", 25)
print(f"찾은 사용자: {found}")

# 미션2. 이름 and/or 나이로 사람 찾기
# 둘중 하나만 있거나 둘 다 없으면?

def find_user3(search)
    resulnt = []

    for u in users:
        if(search.get('age'))