from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name': 'charlie', 'age': 35, 'phone': '345-345-345'},
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/user/<name>')
def search_user(name):
    user = None
    # 유저찾기 함수
    for u in users :
        if u['name'].lower() == name.lower():
            user = u
            break
    
    # 결과가 있을 때는, 지금처럼 응답과 200을 보내고
    if user:
        return jsonify(user), 200
    # 결과가 없을 때는, 응답값에 404를보낸다.
    else:
        return jsonify({'error':'user not ound'}), 404

if __name__ == "__main__": 
    app.run(debug=True)