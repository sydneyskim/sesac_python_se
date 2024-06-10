from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<html><body><h1>나의 헤딩</h1><p>여기는 나의 문장</p></body></html>"

@app.route("/user/<name>") # <name> 변수임 -> 이 변수명과 함수의 인자를 매칭해서 내부에서 처리
def user(name):
    username = name
    return f"""
    <html><body><h1>사용자페이지: {username} 님 안녕하세요.</h1>
    <p>여기는 {username}님 소개 내용</p></body></html>"""

@app.route("/admin")
def admin():
    return "<html><body><h1>나의 헤딩</h1><p>여기는 나의 문장</p></body></html>"


if __name__ == "__main__":
    app.run(debug=True) # 디버그 모드는 개발환경에서만 사용해야함... 배포하는 production에서는 debug는 항상 off여야함