from generators.IdGenerator import IdGenerator
import Order
import Item

class OrderItemGenerator:
    numbers = 1
    data = []
    
    # 초기화
    def __init__(self, numbers, order_data, item_data):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.order_id = Order.IdGenerator()
        self.item_id = Item.IdGenerator()
        
    # 출력
    def generate_OrderItem(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            orderid = self.order_id.generate_id()
            itemid = self.item_id.generate_id()
            
            a_orderitem = (id, orderid, itemid)
            self.data.append(a_orderitem)