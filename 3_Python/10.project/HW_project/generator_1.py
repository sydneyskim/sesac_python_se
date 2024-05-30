# 미션1
import random

# M1. 10명의 사람의 이름을 랜덤으로 생성하시오. (영문 이름 샘플 10개 참조해서)
surname = ['김', '이', '박', '최', '정']
middlename = ['수', '민', '태', '여', '승']
lastname = ['원', '림', '미', '은', '희']

cities = ['서울시', '수원시', '부산시']
towns_seoul = ['영등포구', '노원구', '동대문구', '마포구', '서대문구']
towns_suwon = ['장안구', '팔달구', '영통구', '권선구']
towns_busan = ['북구', '장안구', '동구', '서구', '해운대구' ]

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    return name

# M1-2. 성별, 생년월일, 나이를 랜덤으로 생성하시오. (나이 주의 = 생년월일 기반 계산)
#성별
def generate_gender():
    return random.choice(['Male', 'Female'])

# 생년월일 랜덤생성 , 나이 계산
year_start = 1924
year_end = 2014
def generate_birthdate():
    year = random.randint(year_start, year_end)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    # 올해년도에서 생년 빼기.. + 1 햔국식 나이..
    age = 2024 - year + 1
    birthdate = f"{year}-{month:02d}-{day}"
    
    return birthdate, age

# M1-3. 주소를 랜덤으로 생성하시오.
def generate_address():
    address_city = random.choice(cities)
    if address_city == "서울시":
        address_town = random.choice(towns_seoul)
    elif address_city == "수원시":
        address_town = random.choice(towns_suwon)
    elif address_city == "부산시":
        address_town = random.choice(towns_busan)
    
    address = address_city + address_town

    return address

data = []

for _ in range(10):
    name = generate_name()
    birthdate,age = generate_birthdate()
    gender = generate_gender()
    address = generate_address()
    data.append((name, birthdate, gender, age, address))
    
for d in data:
    print(d)






    