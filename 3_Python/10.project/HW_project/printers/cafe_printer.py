import csv

class CafePrinter:
    def print_to_screen(self, cafe):
        for c in cafe:
            print(c)

    def print_to_file(self, cafe):
        with open('output/cafe.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_list = ['Id','Name','Type','Address']
            writer.writerow(header_list)
            for c in cafe:
                writer.writerow(c)
            