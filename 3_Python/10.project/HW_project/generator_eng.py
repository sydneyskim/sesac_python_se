import random

# M1. 10명의 사람의 이름을 랜덤으로 생성하시오. (영문 이름 샘플 10개 참조해서)
names = ['James', 'John', 'Jane', 'Sam', 'Tommy', 'Andrew', 'Peter', 'Ryan', 'Chloe', 'Andrea']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_name():
    return random.choice(names)

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
    return random.choice(cities)

data = []

for _ in range(10):
    name = generate_name()
    birthdate,age = generate_birthdate()
    gender = generate_gender()
    address = generate_address()
    data.append((name, birthdate, gender, age, address))
    
for d in data:
    print(d)






    