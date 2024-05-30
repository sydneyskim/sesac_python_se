from factory import GeneratorFactory, PrinterFactory

# 메인함수
if __name__ == "__main__":
    valid_choice = ['User', 'Store', 'Item', 'Order', 'OrderItem']
    
    while True:
        choice = input("출력할 데이터 유형을 입력해주세요(User, Store, Item, Order, OrderItem 중 택1: ")
        if choice in valid_choice:
            break
        else:
            print("입력값은 User, Store, Item, Order, OrderItem 중 하나여야 합니다.")
        
    while True:
        try:
            num_data = int(input("생성할 데이터 갯수를 입력해주세요: "))
            if num_data > 0:
                break
            else: 
                print("유효한 숫자를 입력해주세요.")
        except ValueError as e:
            print(e)
            
    generator_factory = GeneratorFactory()
    printer_factory = PrinterFactory()
        
    generators = generator_factory.get_generator(choice, num_data)
        
    if choice == "User":
        generators.generate_users()
    elif choice == "Store":
        generators.generate_cafes()
    elif choice == "Item":
        generators.generate_items()
    elif choice == "Order":
        generators.generate_orders()
    elif choice == "OrderItem":
        generators.generate_orderitems()

    my_printer = printer_factory.get_printer(choice)
    
    if int(num_data) > 0:
        print_type = input("출력을 원하는 형태를 입력해주세요: ")
        if print_type == 'screen':
            my_printer.print_to_screen(generators.data)
        elif print_type == 'file':
            my_printer.print_to_file(generators.data)
        else:
            print('screen 혹은 file을 입력하세요.')