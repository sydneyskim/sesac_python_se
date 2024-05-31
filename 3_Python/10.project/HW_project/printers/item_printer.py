import csv

class ItemPrinter:
    def print_to_screen(self, item):
        for i in item:
            print(i)
    
    def print_to_file(self, item):
        with open('output/item.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','Name','Type','UnitPrice']
            writer.writerow(header_list)
            for i in item:
                writer.writerow(i)