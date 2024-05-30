from generators.IdGenerator import IdGenerator
from generators.MenuGenerator import MenuGenerator

class ItemGenerator:
    numbers = 1
    item = []
    
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.menu_gen = MenuGenerator()
        
    # 출력
    def generate_items(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            category, item, item_price = self.menu_gen.generate_item()
            
            a_item = (id, item, category, item_price)
            self.item.append(a_item)
