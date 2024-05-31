import csv

class DataPrinter:
    # 화면에 표시
    def print_to_screen(self, data):
        for d in data:
            print(d)
    
    # csv 파일로 저장 
    def print_to_file(self, data):
        with open('output/user.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','Name','Birthdate','Gender','Age','Address']
            writer.writerow(header_list)
            for d in data:
                writer.writerow(d)

class CafePrinter:
    def print_to_screen(self, data):
        for d in data:
            print(d)

    def print_to_file(self, data):
        with open('output/cafe.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','Name','Type','Address']
            writer.writerow(header_list)
            for d in data:
                writer.writerow(d)
                
class ItemPrinter:
    def print_to_screen(self, data):
        for d in data:
            print(d)
    
    def print_to_file(self, data):
        with open('output/item.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            # header_list = ['Id','Name','Type','UnitPrice']
            # writer.writerow(header_list)
            for d in data:
                writer.writerow(d)
class OrderPrinter:
    def print_to_screen(self, data):
        for d in data:
            print(d)
            
    def print_to_file(self, data):
        with open('output/order.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','OrderAt','StoreId','UserId']
            writer.writerow(header_list)
            for d in data:
                writer.writerow(d)
                
class OrderItemPrinter:
    def print_to_screen(self, data):
        for d in data:
            print(d)
            
    def print_to_file(self, data):
        with open('output/orderitem.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','OrderId','ItemId']
            writer.writerow(header_list)
            for d in data:
                writer.writerow(d)           
