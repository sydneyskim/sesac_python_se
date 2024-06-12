from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/admin')
def admin():
    # 사용 예: if 로그인 안한 사용자면 홈으로 돌려보내기
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)