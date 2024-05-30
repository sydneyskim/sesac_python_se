import random
import csv
from itertools import chain

class CafeNameGenerator:
    cafes = []
    locations = []
    
    # 카페 기본값 설정
    def __init__(self):
        # 카페 프랜차이즈
        with open('datas/cafes.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_cafe = [c for c in csvreader]
            cafes_list = list(chain(*csv_list_cafe))
            self.cafe = [c.strip() for c in cafes_list]
        # 카페 점 명
        with open('datas/locations.txt', 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_location = [l for l in csvreader]
            locations_list = list(chain(*csv_list_location))
            self.locations = [l.strip() for l in locations_list]
            
    # 랜덤 카페명 설정
    def generate_cafe(self):
        cafe = random.choice(self.cafe)
        location = random.choice(self.locations)
        num = random.randint(1, 100)
        cafe_address = f"{cafe} {location}{num}호점"
        return cafe, cafe_address    