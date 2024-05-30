from generators.IdGenerator import IdGenerator
from generators.DateTimeGenerator import DateTimeGenerator
import User
import Store


class OrderGenerator:
    numbers = 1
    data = []
    
    # 초기화
    def __init__(self, numbers, user_data, store_data):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.time_gen = DateTimeGenerator()
        self.user_id = User.IdGenerator()
        self.store_id = Store.IdGenerator()
        
    # 출력
    def generate_orders(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            time = self.time_gen.generate_datetime()
            storeid = self.store_id.generate_id()
            userid = self.user_id.generate_id()
            
            a_order = (id, time, storeid, userid)
            self.data.append(a_order)
            