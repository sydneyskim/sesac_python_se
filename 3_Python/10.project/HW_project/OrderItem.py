from generators.IdGenerator import IdGenerator
import csv
import random

# 주문아이템 생성기 클래스
class OrderItemGenerator:
    numbers = 1
    data = []
    
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        # order_id
        with open('output/cafe.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_orderid = [o[0] for o in cvsreader] # 각 줄인 o의 첫번째를 list에 저장
            self.orderid = [o.strip() for o in list_orderid] # list 순회하며 앞뒤공백 제거과정
        # item_id
        with open('output/user.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_itemid = [i[0] for i in cvsreader] # 각 줄인 i의 첫번째를 list에 저장
            self.itemid = [i.strip() for i in list_itemid] # list 순회하며 앞뒤공백 제거과정
        
    # 출력
    def generate_OrderItem(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            orderid = random.choice(self.orderid)
            itemid = random.choice(self.itemid)
            
            a_orderitem = (id, orderid, itemid)
            self.data.append(a_orderitem)