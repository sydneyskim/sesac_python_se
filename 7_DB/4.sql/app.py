from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import database as db

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 구현
        username = request.form["username"]
        password = request.form["password"]

        # 사용자 데이터를 외부 DB에서 가져오기
        # query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user_data = db.get_query("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        print(f"조회된 사용자: ", user_data)

        if len(user_data) == 1: # and user_data["password"] == password
            session["user"] = username
            session.permanent = True
            print("패스워드 맞음!!")
            flash("로그인에 성공하였습니다.")
            return redirect(url_for("home"))
        else:
            print('패스워드 틀림!!')
            flash("아이디/패스워드가 일치하지 않습니다.")
            # 메세지가 있으면 전달하고, 없으면 그냥 재 로그인
            return redirect(url_for("login"))
    else:
        # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:
            print("이전에 로그인 했음!!")
            return redirect(url_for("home"))

    return render_template('login.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if "user" in session:
        user = session['user']

        if request.method == 'POST':
            action = request.form["action"]
            if action == "update_email":
                email = request.form["email"]
                if email:
                    db.execute_query("UPDATE users SET email = ? WHERE username = ?", (email, user))
                    flash("이메일이 변경되었습니다.")
                else:
                    flash("이메일을 입력해주세요.")
            elif action == "update_password":
                password = request.form["password"]
                if password:
                    db.execute_query("UPDATE users SET password = ? WHERE username = ?", (password, user))
                    flash("비밀번호가 변경되었습니다.")
                else:
                    flash("비밀번호를 입력해주세요.")
            elif action == "delete":
                db.execute_query("DELETE FROM users WHERE username = ?", (user,))
                session.pop("user", None)
                flash("계정이 삭제되었습니다.")
                return redirect(url_for("login"))
        
        return render_template('user.html', user=user)
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for("login"))

@app.route('/view')
def view():
    # users = [] # 미션1. DB 쿼리해서 모든 사용자 목록을 받아온다
    users = db.get_query("SELECT * FROM users", ())
    return render_template("view.html", users=users)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        db.execute_query("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        print('회원가입 완료.')
        flash('회원가입이 완료되었습니다.')
        
        return redirect(url_for('home'))
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    flash("로그아웃에 성공하였습니다.")
    return redirect(url_for("login"))

@app.route('/board', methods=['GET', 'POST'])
def board():
    if "user" in session:
        if request.method == 'POST':
            title = request.form["title"]
            content = request.form["content"]
            user = session["user"]
            user_data = db.get_query("SELECT id FROM users WHERE username = ?", (user,))
            if user_data:
                user_id = user_data[0]["id"]
                db.execute_query("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, user_id))
                flash("게시물이 작성되었습니다.")
                return redirect(url_for("board"))

        posts = db.get_query("SELECT p.id, p.title, p.content, u.username, p.created_at FROM posts p JOIN users u ON p.user_id = u.id", ())
        return render_template("board.html", posts=posts)
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for("login"))
    
if __name__ == "__main__":
    db.init_db()   # 시스템 부팅(?) 시에 DB 초기화 하기...
    print('DB 초기화 완료')
    app.run(debug=True)  # 플라스크 앱 실행...