# 자료구조 배우는 중
# 1. 리스트
a = 5
b = [10, 20, 30, 40, 50]
a2 = [5]

print(a)
print(b)
print(b[0])
print(b[4])
# print(b[5])
# 5번 인덱스가 없으므로 에러

print(len(b)) # 길이는 우리가 일반적으로 사용하는 그 길이
              # 인덱스는 0 ~ 길이 -1

print(b[1:3]) # 인덱스 1부터 3 전까지.... 

fruit = ['apple', '사과', 'grape', '포도']
print(fruit)

print(fruit[1:3])

members = [3, 'desk', 2, -1, 'chair'] #python의 특징, 타입이 다른 것들 혼용 가능
print(members)

b.remove(20)
print(b)

fruit.remove('apple')
print(fruit)

b.append(20)
print(b) #append는 맨 뒤에 추가됨

b.insert(0,20) #insert(인덱스, 넣을 값) 두개를 넣어야 함
print(b)

# a.insert(0, 10) #TypeError
print(a)
a2.insert(0, 10)
print(a2)

# ------------------------------
# 2. 튜플(tuple) - 리스트와 동일하지만, 변경이 불가능한 리스트를 생성하는 것 - 이뮤터블(immutable)
c = (1,2,3,4,5)
print(c)

# c.remove(2) 삭제 불가
# c.append(2) 뒤에 삽입 불가
# c.insert(0.2) 인덱스에 삽입 불가

print(c[3], c[4])
print(c[2:]) #인덱스 2부터 끝까지
print(b[2:])
print(c[:2]) #인덱스 0부터 2"전"까지
print(b[:2])

# ------------------------------
# 3. 딕셔너리 (dict, dictionary) 라는 데이터타입 - key, value

user1 = {
    "name":"park",
    "age":10,
    "city":"seoul"
}

print(user1)
print(user1["name"])
print(user1["age"])
print(user1["city"])
# print(user1["email"]) # KeyError 발생.. 없는 키 참조

user1["email"] = "hello@gmail.com" # 딕셔너리에 email값 추가
print(user1)

user1["email"] = '' # 딕셔너리 email 값 변경
print(user1)

del user1["email"] # 딕셔너리 email 항목 지우기
print(user1)