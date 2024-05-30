from User import DataGenerator
from Store import StoreGenerator
from Item import ItemGenerator
from Order import OrderGenerator
from OrderItem import OrderItemGenerator
from printers.user_printer import DataPrinter
from printers.cafe_printer import CafePrinter
from printers.item_printer import ItemPrinter
from printers.order_printer import OrderPrinter
from printers.orderitem_printer import OrderItemPrinter

# 메인함수
if __name__ == "__main__":
    choice = input("출력할 데이터 유형을 입력해주세요(User, Store, Item, Order, OrderItem 중 택1: ")
    if choice == "User":
        num_data = input("생성할 데이터 갯수를 입력해주세요: ")
        
        users = DataGenerator(int(num_data))
        users.generate_users()
        
        my_printer = DataPrinter()
        
        if int(num_data) > 0:
            print_type = input("출력을 원하는 형태를 입력해주세요: ")
            if print_type == 'screen':
                my_printer.print_to_screen(users.data)
            elif print_type == 'file':
                my_printer.print_to_file(users.data)
            else:
                print('screen 혹은 file을 입력하세요.')
    
    elif choice == "Store":
        num_cafe = input("생성할 데이터 갯수를 입력해주세요: ")
    
        cafes = StoreGenerator(int(num_cafe))
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
                print('screen 혹은 file을 입력하세요.')
        
    elif choice == "Item":  
        num_item =input("생성할 데이터 갯수를 입력해주세요: ")
        
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
                print('screen 혹은 file을 입력하세요.')
                
    elif choice == "Order":  
        num_order =input("생성할 데이터 갯수를 입력해주세요: ")
            
        orders = OrderGenerator(int(num_order))
        orders.generate_orders()
        
        # 데이터 출력 화면 or 파일
        my_printer = OrderPrinter()
        
        if int(num_order) > 0:
            print_type = input("출력을 원하는 형태를 입력해주세요: ")
            if print_type == 'screen':
                my_printer.print_to_screen(orders.data)
            elif print_type == 'file':
                my_printer.print_to_file(orders.data)
            else:
                print('screen 혹은 file을 입력하세요.')
                
    elif choice == "OrderItem":  
        num_orderitem =input("생성할 데이터 갯수를 입력해주세요: ")
        
        orderitems = OrderItemGenerator(int(num_orderitem))
        orderitems.generate_OrderItem()
        
        # 데이터 출력 화면 or 파일
        my_printer = OrderItemPrinter()
        
        if int(num_orderitem) > 0:
            print_type = input("출력을 원하는 형태를 입력해주세요: ")
            if print_type == 'screen':
                my_printer.print_to_screen(orderitems.data)
            elif print_type == 'file':
                my_printer.print_to_file(orderitems.data)
            else:
                print('screen 혹은 file을 입력하세요.')
                
    else :
        print("유효한 값이 아닙니다.")