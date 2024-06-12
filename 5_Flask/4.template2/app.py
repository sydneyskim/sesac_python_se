from flask import Flask, render_template, request

app = Flask(__name__) # 초기화

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Alice', 'age': 50, 'phone': '888-999-1010'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'charlie', 'age': 35, 'phone': '345-345-3456'},
]


@app.route('/') # route로 왔을 때 아래의 함수를 부르기
def main():
    return render_template("index.html", users=users)

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    print(f"검색한 이름: {search_name}, 검색한 나이: {search_age}")
    
    filtered_user = users
    
    if search_name:
        filtered_user= [u for u in filtered_user if search_name.lower() in u['name'].lower()]
    if search_age:
        filtered_user= [u for u in filtered_user if int(search_age) == u['age']]
    
    return render_template('index.html', users=filtered_user)
        

if __name__ == "__main__": 
    app.run(debug=True)
    
    
    
    