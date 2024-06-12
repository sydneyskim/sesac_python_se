import csv
from flask import Flask, render_template, request
import math

app = Flask(__name__)

csv_data = []
headers = []

def load_csv_data(filename):
    global headers # 바깥 scope (글로벌 variable) 의 내용을 변경하려고 할때 선언해야함
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = [fieldname.strip() for fieldname in csv_reader.fieldnames]
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)
            
@app.route('/')
@app.route('/<int:page>')
def index(page=1): # 1페이지 기본값
    per_page = 20
    
    start_index = (page - 1) * per_page
    end_index = page * per_page
    
    total_pages = math.ceil(len(csv_data)/per_page)
    
    current_page = csv_data[start_index:end_index]
    return render_template("index2.html", headers = headers, users = current_page, total_pages = total_pages)
 
if __name__ == '__main__':
    load_csv_data('./user.csv')
    app.run(debug=True)
