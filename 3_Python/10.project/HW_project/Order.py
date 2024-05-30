from generators.IdGenerator import IdGenerator
from generators.DateTimeGenerator import DateTimeGenerator
from itertools import chain
import csv
import random

# 주문 생성기 클래스
class OrderGenerator:
    numbers = 1
    data = []
    
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.time_gen = DateTimeGenerator()
        # store_id
        with open('output/cafe.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_storeid = [s[0] for s in cvsreader] # 각 줄인 sn을 list에 저장
            self.storeid = [s.strip() for s in list_storeid] # list 순회하며 앞뒤공백 제거과정
        # user_id
        with open('output/user.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_userid = [u[0] for u in cvsreader] # 각 줄인 sn을 list에 저장
            self.userid = [u.strip() for u in list_userid] # list 순회하며 앞뒤공백 제거과정
        
    # 출력
    def generate_orders(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            time = self.time_gen.generate_datetime()
            storeid = random.choice(self.storeid)
            userid = random.choice(self.userid)
            
            a_order = (id, time, storeid, userid)
            self.data.append(a_order)
            