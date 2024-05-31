import csv

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