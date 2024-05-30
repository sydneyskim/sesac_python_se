from generators.AddressGenerator import AddressGenerator
from generators.IdGenerator import IdGenerator
from generators.CafeGenerator import CafeNameGenerator

# 카페 생성기 클래스
class StoreGenerator:
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
