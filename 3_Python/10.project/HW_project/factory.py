from generators.generator import UserGenerator , StoreGenerator, ItemGenerator, OrderGenerator, OrderItemGenerator
from printers import printer

class GeneratorFactory:
    def get_generator(self, generator_type, num_data):
        if generator_type == "User":

            return UserGenerator(int(num_data))
        
        elif generator_type == "Store":
            
            return StoreGenerator(int(num_data))
        
        elif generator_type == "Item":
            
            return ItemGenerator(int(num_data))
        
        elif generator_type == "Order":
            user_gen = UserGenerator(int(num_data))
            user_gen.generate_users() # 사용자 데이터를 먼저 생성
            
            store_gen = StoreGenerator(int(num_data))
            store_gen.generate_cafes() # 가게 데이터를 먼저 생성
            
            # return OrderGenerator(int(num_data), user_gen.data, store_gen.data)
            return OrderGenerator(int(num_data))
        
        elif generator_type == "OrderItem":
            user_gen = UserGenerator(int(num_data))
            user_gen.generate_users()  # 사용자 데이터를 먼저 생성
            
            store_gen = StoreGenerator(int(num_data))
            store_gen.generate_cafes()  # 가게 데이터를 먼저 생성
    
            order_gen = OrderGenerator(int(num_data), user_gen.data, store_gen.data)
            order_gen.generate_orders()  # 주문 데이터를 먼저 생성
            
            item_gen = ItemGenerator(int(num_data))
            item_gen.generate_items()  # 아이템 데이터를 먼저 생성
            
            # return OrderItemGenerator(int(num_data), order_gen.data, item_gen.data)
            return OrderItemGenerator(int(num_data))
        else:
            raise ValueError("유효한 값이 아닙니다.")

class PrinterFactory:
    def get_printer(self, generator_type):
        if generator_type == "User":
            
            return printer.DataPrinter()
        
        elif generator_type == "Store":
            
            return printer.CafePrinter()
        
        elif generator_type == "Item":
            
            return printer.ItemPrinter()
        
        elif generator_type == "Order":
            
            return printer.OrderPrinter()
        
        elif generator_type == "OrderItem":
            
            return printer.OrderItemPrinter()
        
        else:
            raise ValueError("유효한 값이 아닙니다.")