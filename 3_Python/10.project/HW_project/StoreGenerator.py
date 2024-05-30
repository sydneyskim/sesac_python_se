from generators.AddressGenerator import AddressGenerator
from generators.IdGenerator import IdGenerator
from generators.CafeGenerator import CafeNameGenerator
from printers.cafe_printer import CafePrinter
import sys

# 카페 생성기 클래스
class CafeGenerator:
    numbers = 1
    cafe = []
    
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.cafe_gen = CafeNameGenerator()
        self.addr_gen = AddressGenerator()
        
    # 출력
    def generate_cafes(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            cafe, cafe_address = self.cafe_gen.generate_cafe()
            address = self.addr_gen.generate_address()
            
            a_cafe = (id, cafe_address, cafe, address )
            self.cafe.append(a_cafe)
            
# 메인함수
if __name__ == "__main__":
    if(len(sys.argv)) == 1:
        num_cafe = input("생성할 데이터 갯수를 입력해주세요: ")
    
    # 데이터 형태 생성
    cafes = CafeGenerator(int(num_cafe))
    cafes.generate_cafes()
    
    # 데이터 출력 화면 or 파일
    my_printer = CafePrinter()
        
    if int(num_cafe) > 0:
        print_type = input("출력을 원하는 형태를 입력해주세요: ")
        if print_type == 'screen':
            my_printer.print_to_screen(cafes.cafe)
        elif print_type == "file":
            my_printer.print_to_file(cafes.cafe)
        else:
            print('screen 혹은 file을 입력하세요')