import random
import csv
from generators.AddressGenerator import AddressGenerator
from generators.BirthdateGenerator import BirthdateGenerator
from generators.GenderGenerator import GenderGenerator
from generators.NameGenerator import NameGenerator
from generators.IdGenerator import IdGenerator
from generators.CafeGenerator import CafeNameGenerator
from generators.MenuGenerator import MenuGenerator
from generators.DateTimeGenerator import DateTimeGenerator


# 생성기 모음
# 사용자 생성기 클래스
class UserGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.bith_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.addr_gen = AddressGenerator()
    
    # 출력
    def generate_users(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate, age = self.bith_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.addr_gen.generate_address()
            
            a_user = (id, name, birthdate, gender, age, address)
            self.data.append(a_user)

# 카페 생성기 클래스
class StoreGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.cafe_gen = CafeNameGenerator()
        self.addr_gen = AddressGenerator()
        
    # 출력
    def generate_cafes(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            cafe, cafe_address = self.cafe_gen.generate_cafe()
            address = self.addr_gen.generate_address()
            
            a_cafe = (id, cafe_address, cafe, address)
            self.data.append(a_cafe)

# 아이템 생성기 클래스
class ItemGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.menu_gen = MenuGenerator()
        
    # 출력
    def generate_items(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            category, item, item_price = self.menu_gen.generate_item()
            
            a_item = (id, item, category, item_price)
            self.data.append(a_item)

# 주문 생성기 클래스
class OrderGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.time_gen = DateTimeGenerator()
        # store_id
        with open('output/cafe.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_storeid = [s[0] for s in cvsreader][1:] # 각 줄인 s의 0번째를 list에 저장 (첫줄(헤더)제외)
            self.storeid = [s.strip() for s in list_storeid] # list 순회하며 앞뒤공백 제거과정
        # user_id
        with open('output/user.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_userid = [u[0] for u in cvsreader][1:] # 각 줄인 u의 0번째를 list에 저장 (첫줄(헤더)제외)
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
            
# 주문아이템 생성기 클래스
class OrderItemGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        # order_id
        with open('output/cafe.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_orderid = [o[0] for o in cvsreader][1:] # 각 줄인 o의 첫번째를 list에 저장 (첫줄(헤더)제외)
            self.orderid = [o.strip() for o in list_orderid] # list 순회하며 앞뒤공백 제거과정
        # item_id
        with open('output/user.csv', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_itemid = [i[0] for i in cvsreader][1:] # 각 줄인 i의 첫번째를 list에 저장 (첫줄(헤더)제외)
            self.itemid = [i.strip() for i in list_itemid] # list 순회하며 앞뒤공백 제거과정
        
        
    # 출력
    def generate_orderitems(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            orderid = random.choice(self.orderid)
            itemid = random.choice(self.itemid)
            
            a_orderitem = (id, orderid, itemid)
            self.data.append(a_orderitem)