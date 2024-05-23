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
print(f"찾은 사용자1: {found}")

# 미션1. 이름 + 나이로
def find_user2(name=None, age=None):
    found_user = []
    for u in users:
        if u.get("name").lower() == name.lower() and u.get("age") == age:
            found_user.append(u)
    return found_user

found = find_user2("alice", 25)
print(f"찾은 사용자2: {found}")

# 미션2. 이름 and/or 나이로 사람 찾기
# 둘중 하나만 있거나 둘 다 없으면?

def find_user3(name=None, age=None):
    found_user= []

    if name is None and age is None:
        return None
    
    for u in users:
        if name is not None and age is not None:
                if u["name"].lower() == name.lower() and u["age"] == age:
                    return u
        elif name is not None:
            if u["name"].lower() == name.lower():
                return u
        elif age is not None:
            if u["age"] == age:
                return u  
    return None

# found = find_user3("")
# found = find_user3("alice")
# found = find_user3("alice", 25)
# found = find_user3("sydney")
found = find_user3(None, 30)

print(f"찾은 사용자3: {found}")


def find_user4(search):
    result = []

    for u in users:
        if(search.get('age') is None or u.get('age') == search.get('age')) and \
           (search.get('min_age') is None or u.get('age') >= search.get('min_age')) and \
           (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):
            
            result.append(u)

    return result
search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice", "age": 40}
search_criteria3 = {"name": "Alice", "min_age": 40}
search_criteria4 = {"name": "Alice", "min_age": 50}
search_criteria5 = {"name": "Alice", "min_age": 60}

print(find_user4(search_criteria2))