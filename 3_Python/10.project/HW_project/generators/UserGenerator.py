from generators.AddressGenerator import AddressGenerator
from generators.BirthdateGenerator import BirthdateGenerator
from generators.GenderGenerator import GenderGenerator
from generators.NameGenerator import NameGenerator
from generators.IdGenerator import IdGenerator
from printers.user_printer import DataPrinter
import sys


# 데이터 생성기 클래스
class DataGenerator:
    numbers = 1
    data = []
    # 초기화
    def __init__(self, numbers):
        self.numbers = numbers
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
            
# 메인함수
if __name__ == "__main__":
    if(len(sys.argv)) <= 1:
        num_data = input("생성을 원하는 데이터 갯수를 입력하세요: ")
    else:
        num_data = sys.argv[1]
        
    # 데이터 형태 생성
    users = DataGenerator(int(num_data)) # 클래스의 인스턴스를 생성하고 변수 users에 저장
    users.generate_users() # 메서드 호출, 생성된 데이터는 self.data 리스트에 저장됨
    
    # 데이터 출력 화면 or 파일
    my_printer = DataPrinter()
    
    # 파일명 갯수 타입 다 잘 입력했을 경우
    if len(sys.argv) == 3:
        if sys.argv[2] == 'screen':
            my_printer.print_to_screen(users.data)
        elif sys.argv[2] == 'file':
            my_printer.print_to_file(users.data)
        else:
            print("지원되지 않는 인자입니다.")
    # 입력값이 빠져있을 경우
    elif len(sys.argv) < 3:
        print_type = input("출력을 원하는 형태를 입력해주세요. (screen 혹은 file)")
        if print_type == 'screen':
            my_printer.print_to_screen(users.data)
        elif print_type == 'file':
            my_printer.print_to_file(users.data)
        else:
            print('screen 혹은 file을 입력하세요')
        