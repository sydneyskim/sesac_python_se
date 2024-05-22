users = [ # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
    {"name": "Dave", "age": 35, "location": "Jeju", "car": "K5"},
    {"name": "June", "age": 35, "location": "Jeju", "car": "K5"}
]

# users = ["Alice", "Bob", "Charlie"]  # 스트링 리스트

# user1{name} -> XXX 할 수 없음
# user1{'name'} -> 가장 일반적인 방식
# user1.get('name') -> 함수를 통해서 가져오는 방식
# user1.name -> 객체의 멤버를 가져오는 방식

# name = input("찾는 사용자의 이름을 입력하시오.: ")

def find_user(name):
    #사용자를 찾는것이 목적
    found_user = []
    for u in users:
        # print(u['name])
        if u['name'].lower() == name.lower():
            # print(u)
            found_user.append(u)
    return found_user # 함수의 출력
        #print("찾는 사용자가 없습니다")

found = find_user('alice')
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

# name = input("찾는 사용자의 이름을 입력하시오: ")
# age = input("찾는 나이를 입력하시오: ")

# def find_user(name="None", age="없음"): #기본값 할당 name=None, age=None -> 진짜 없는 값
#     found_user = []
#     # 아무것도 없는 케이스
#     if name is None and age is None:
#         return users

#     for u in users:
#         # print(f'가져온 것: {u["name"]}, {u["age"]}, 입력받은 것: "{name}", "{age}"')
#         # 둘 다 입력값이 있음
#         if name is not None and age is not None:
#             if u["name"].lower() == name.lower() and u["age"] == age:
#                 return u
#         # 이름만 있음
#         elif name is not None:
#             if u["name"].lower() == name.lower():
#                 return u
#         #나이만 있음
#         elif age is not None:
#             if u["age"] == age:
#                 return u
#     return None

# found = find_user(name, age)
# print(f"찾은 사용자: {found}")



def find_user2(search): # 딕셔너리로 받았음..
    result = []

    for u in users:
        # 조건문 적절하게 넣기...
        if (search.get('age') is None or u.get('age') == search.get('age')) and \
           (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):

            result.append(u)

    return result

search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice", "age": 40}
search_criteria3 = {"location": "Jeju", "car": "BMW"}

print(find_user2(search_criteria2))


# min_age 구현하기
def find_user3(search): # 딕셔너리로 받았음..
    result = []

    for u in users:
        # 조건문 적절하게 넣기...
        if (search.get('age') is None or u.get('age') == search.get('age')) and \
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

print(find_user3(search_criteria2))

def find_user4(search):
    result = []

    for u in users:
        if match_criteria(u, search):
            result.append(u)
    
    return result

# 이 user라는 사용자가 이 조건(criteria)애 만족하느냐??
# 그래서, 조건에 만족하면 True 반환, 만족하지 않으면 False를 반납
def match_criteria(user, criteria):
    for key, value in criteria.items(): # 딕셔너리 안에 있는 k,v 쌍을 하나씩 추출하는 함수 -> items()
        if key == "age":
            # 나이에 대해 비교
            if user["age"] != value:
                return False
        if key == "name":
            # 이름에 대해 비교
            if user["name"] != value:
                return False
        if key == "location":
            # 지역에 대해 비교
            if user["location"] != value:
                return False
        if key == "car":
            # 차에 대해 비교
            if user["car"] != value:
                return False
            
    return True


print(find_user4(search_criteria2))
