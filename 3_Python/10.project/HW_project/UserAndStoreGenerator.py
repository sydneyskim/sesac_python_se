from generators.AddressGenerator import AddressGenerator
from generators.BirthdateGenerator import BirthdateGenerator
from generators.GenderGenerator import GenderGenerator
from generators.NameGenerator import NameGenerator
from generators.IdGenerator import IdGenerator
from generators.CafeGenerator import CafeNameGenerator
from printers.user_printer import DataPrinter
from printers.cafe_printer import CafePrinter
import sys

# 데이터 생성기 클래스
class BothGenerator:
    numbers = 1
    data = []
    cafe = []
    
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.addr_gen = AddressGenerator()
        self.cafe_gen = CafeNameGenerator()
    
    # 출력
    def generate_Both(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate, age = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.addr_gen.generate_address()
            cafe, cafe_address = self.cafe_gen.generate_cafe()
        
            a_user = (id, name, birthdate, gender, age, address)
            self.data.append(a_user)
            a_cafe = (id, cafe_address, cafe, address)
            self.cafe.append(a_cafe)
            
            
# 메인함수
if __name__ == "__main__":
    choice = input("출력할 데이터 유형을 입력해주세요(User 혹은 Store)")
    if choice == "User":
        num_data = input("생성할 데이터 갯수를 입력해주세요: ")
        
        users = BothGenerator(int(num_data))
        users.generate_Both()
        
        user_printer = DataPrinter()
        
        if int(num_data) > 0:
            print_type = input("출력을 원하는 형태를 입력해주세요: ")
            if print_type == 'screen':
                user_printer.print_to_screen(users.data)
            elif print_type == 'file':
                user_printer.print_to_file(users.data)
            else:
                print('screen 혹은 file을 입력하세요')
    elif choice == "Store":
        num_cafe = input("생성할 데이터 갯수를 입력해주세요: ")
    
        cafes = BothGenerator(int(num_cafe))
        cafes.generate_Both()
    
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
    else :
        print("유효한 값이 아닙니다.")