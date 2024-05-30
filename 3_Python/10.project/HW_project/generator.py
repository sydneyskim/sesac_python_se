from generators.AddressGenerator import AddressGenerator
from generators.BirthdateGenerator import BirthdateGenerator
from generators.GenderGenerator import GenderGenerator
from generators.NameGenerator import NameGenerator
from generators.IdGenerator import IdGenerator
from generators.CafeGenerator import CafeNameGenerator
from generators.MenuGenerator import MenuGenerator
from generators.DateTimeGenerator import DateTimeGenerator
import random

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
    def __init__(self, numbers, user_data, store_data):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.time_gen = DateTimeGenerator()
        self.user_data = user_data
        self.store_data = store_data

    # 출력
    def generate_orders(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            time = self.time_gen.generate_datetime()
            storeid = random.choice(self.store_data)[0]
            userid = random.choice(self.user_data)[0]
            
            a_order = (id, time, storeid, userid)
            self.data.append(a_order)
            
# 주문아이템 생성기 클래스
class OrderItemGenerator:
    def __init__(self, numbers, order_data, item_data):
        self.numbers = numbers
        self.data = []
        self.id_gen = IdGenerator()
        self.order_data = order_data
        self.item_data = item_data
        
    # 출력
    def generate_orderitems(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            orderid = random.choice(self.order_data)[0]
            itemid = random.choice(self.item_data)[0]
            
            a_orderitem = (id, orderid, itemid)
            self.data.append(a_orderitem)