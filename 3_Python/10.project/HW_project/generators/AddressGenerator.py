import random
import csv
from itertools import chain

# 주소 생성기 클래스
class AddressGenerator:
    city = []
    town = []
    
    # 주소 기본값 설정
    def __init__(self):
        # 시
        with open('datas/cities.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_city = [c for c in csvreader]
            cities_list = list(chain(*csv_list_city))
            self.city = [c.strip() for c in cities_list]
        # 서울시 구
        with open('datas/towns_seoul.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_setown = [set for set in csvreader]
            setowns_list = list(chain(*csv_list_setown))
            self.setown = [set.strip() for set in setowns_list]
        # 수원시 구 
        with open('datas/towns_suwon.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_sutown = [sut for sut in csvreader]
            sutowns_list = list(chain(*csv_list_sutown))
            self.sutown = [sut.strip() for sut in sutowns_list]
        # 부산시 구
        with open('datas/towns_busan.txt', 'r', encoding='utf-8') as file:
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
        street1 = random.randint(1, 100)
        street2 = random.randint(1, 100)
        street = f"{street1}길 {street2}"
        # 도시별로 구 선택
        if city == '서울시':
            address = f"{city} {seoul_town} {street}"
        elif city == '수원시':
            address = f"{city} {suwon_town} {street}"
        elif city == '부산시':
            address = f"{city} {busan_town} {street}"
        return address
            