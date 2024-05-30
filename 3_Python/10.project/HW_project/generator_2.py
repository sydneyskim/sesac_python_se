# 미션 2, 3
import random
import csv
from itertools import chain

# 이름 생성기 클래스
class NameGenerator:
    surnames = []
    givennames = []
   # 이름 기본값 설정
    def __init__(self):
        #성
        with open('surname.txt', 'r', encoding='utf-8') as file: #파일열기
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_surname = [sn for sn in cvsreader] # 각 줄인 sn을 list에 저장
            surname_list = list(chain(*list_surname)) # chain(*) 붙이기, 평탄화
            self.surnames = [n.strip() for n in surname_list] # list 순회하며 앞뒤공백 제거과정
        #이름
        with open('givenname.txt', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file)
            list_givenname = [gn for gn in cvsreader]
            givenname_list = list(chain(*list_givenname))
            self.givennames = [n.strip() for n in givenname_list]
    # 랜덤 이름 생성
    def generate_name(self):
        surname = random.choice(self.surnames)
        givenname = random.choice(self.givennames)
        fullname = surname + givenname
        return fullname

# 성별 생성기 클래스
class GenderGenerator:
    # 랜덤 성별 생성
    def generate_gender(sef):
        return random.choice(['Male', 'Female'])
# 생년월일 생성기 클래스
class BirthdateGenerator:
    year_start = 1924
    year_end = 2014
    
    # 생년월일 랜덤생성 , 나이 계산
    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        # 올해년도에서 생년 빼기.. + 1 햔국식 나이.. 
        age = 2024 - year + 1
        birthdate = f"{year}-{month:02d}-{day}"
        
        return birthdate, age

# 주소 생성기 클래스
class AddressGenerator:
    city = []
    town = []
    
    # 주소 기본값 설정
    def __init__(self):
        # 시
        with open('cities.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_city = [c for c in csvreader]
            cities_list = list(chain(*csv_list_city))
            self.city = [c.strip() for c in cities_list]
        # 서울시 구
        with open('towns_seoul.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_setown = [set for set in csvreader]
            setowns_list = list(chain(*csv_list_setown))
            self.setown = [set.strip() for set in setowns_list]
        # 수원시 구 
        with open('towns_suwon.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_sutown = [sut for sut in csvreader]
            sutowns_list = list(chain(*csv_list_sutown))
            self.sutown = [sut.strip() for sut in sutowns_list]
        # 부산시 구
        with open('towns_busan.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_butown = [but for but in csvreader]
            butowns_list = list(chain(*csv_list_butown))
            self.butown = [but.strip() for but in butowns_list]
    # 랜덤 주소 생성     
    def generate_address(self):
        city = random.choice(self.city)
        seoul_town = random.choice(self.setown)
        suwon_town = random.choice(self.sutown)
        busan_town = random.choice(self.butown)
        # 도시별로 구 선택
        if city == '서울시':
            address = city + seoul_town
        elif city == '수원시':
            address = city + suwon_town
        elif city == '부산시':
            address = city + busan_town
        return address
            
# 데이터 생성기 클래스
class DataGenerator:
    numbers = 1
    data = []
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.name_gen = NameGenerator()
        self.bith_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.addr_gen = AddressGenerator()
    
    # 출력
    def generate_users(self):
        for _ in range(self.numbers):
            name = self.name_gen.generate_name()
            birthdate, age = self.bith_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.addr_gen.generate_address()
            
            a_user = (name, birthdate, gender, age, address)
            self.data.append(a_user)
            
# 메인함수
if __name__ == "__main__":
    # 10명의 사용자 데이터 생성
    users = DataGenerator(10) # 클래스의 인스턴스를 생성하고 변수 users에 저장
    users.generate_users() # 메서드 호출, 생성된 데이터는 self.data 리스트에 저장됨
    
    # #생성된 사용자 데이터 출력
    # for d in users.data:
    #     print(d)
    
    # 출력결과 csv 파일로 출력하기
    with open('mission3_output.csv', 'w') as file:
        writer = csv.writer(file)
        for d in users.data:
            writer.writerow(d)