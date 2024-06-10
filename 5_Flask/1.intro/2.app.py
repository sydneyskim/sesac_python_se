from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/user/<name>') # 기본값은 string으로 처리함
def user(name):
    return f"<h1>Hello, {name}님!<h1>"

@app.route('/user/<int:age>')
def userage(age):
    return f"<h1>Age: {age}<h1>"

@app.route('/user/<float:weight>')
def userweight(weight):
    return f"<h1>Weight: {weight}<h1>"

@app.route('/user/<name>/<int:age>')
def usernameage(name, age):
    return f"<h1>Hello, {name}님! Age는 {age} <h1>"

@app.route('/user/<name>/<int:age>/<float:weight>')
def usernameageweight(name, age, weight):
    return f"<h1>Hello, {name}님! Age는 {age} Weight는 {weight}<h1>"

if __name__ == "__main__":
    app.run(debug=True)