from flask import Flask, render_template, request
import csv
import math

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)
            
@app.route('/')
@app.route('/<int:page>')
def index(page=1): # 1페이지 기본값
    per_page = 20
    
    start_index = (page - 1) * per_page
    end_index = page * per_page
    
    headers = csv_data[0]
    
    total_pages = math.ceil(len(csv_data)/per_page)
    
    current_page = csv_data[start_index:end_index]
    
    return render_template("index1.html", headers = headers, users = current_page, total_pages = total_pages)
  
if __name__ == '__main__':
    load_csv_data('./user.csv')
    app.run(debug=True)
    # print(csv_data)

# 1. 이 파일에 플라스크 기본 틀을 추가한다. 

# 2. /에 접속시 이 사용자의 데이터를 보여준다.
