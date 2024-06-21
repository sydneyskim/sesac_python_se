from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/user', method=["GET"])
def get_user():
    return "<h1>정보 제공</h1>"

@app.route('/user', method=["POST"])
def post_user():
    return "<h1>요청에 의한 데이터 생성</h1>"

@app.route('/user', method=["DELETE"])
def delete_user():
    return "<h1>요청에 의한 데이터 삭제</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)