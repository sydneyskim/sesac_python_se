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
            for d in data:
                writer.writerow(d)