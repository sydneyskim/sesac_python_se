import csv

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