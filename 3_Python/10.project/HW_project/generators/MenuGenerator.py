import random
import json

class MenuGenerator:
    items = []
    
    def __init__(self):
        with open('datas/item.json', 'r', encoding='utf-8') as file:
            self.menu = json.load(file)
        
    def generate_item(self):    
        # coffee, juice, cake 값 중 랜덤
        category = random.choice(list(self.menu.keys()))
        # 카테고리 내 메뉴 선택
        item_name = random.choice(list(self.menu[category].keys()))
        # 선택된 메뉴의 가격가져오기
        item_price = self.menu[category][item_name]
        item = f"{item_name} {category}"
        return category, item, item_price