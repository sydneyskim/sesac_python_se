from generators.AddressGenerator import AddressGenerator
from generators.BirthdateGenerator import BirthdateGenerator
from generators.GenderGenerator import GenderGenerator
from generators.NameGenerator import NameGenerator
from generators.IdGenerator import IdGenerator

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