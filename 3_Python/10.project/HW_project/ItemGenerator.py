from generators.IdGenerator import IdGenerator
from generators.MenuGenerator import MenuGenerator
from printers.item_printer import ItemPrinter
import sys

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
            
# 메인함수
if __name__ == "__main__":
    if(len(sys.argv)) == 1:
        num_item = input("생성할 데이터 갯수를 입력해주세요: ")
            
    # 데이터 형태 생성
    items = ItemGenerator(int(num_item))
    items.generate_items()     
    
    # 데이터 출력 화면 or 파일
    my_printer = ItemPrinter()
    
    if int(num_item) > 0:
        print_type = input("출력을 원하는 형태를 입력해주세요: ")
        if print_type == 'screen':
            my_printer.print_to_screen(items.item)
        elif print_type == 'file':
            my_printer.print_to_file(items.item)
        else:
            print('screen 혹은 file을 입력하세요')