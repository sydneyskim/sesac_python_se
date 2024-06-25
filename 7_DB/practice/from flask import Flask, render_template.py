from flask import Flask, render_template, request, session, redirect, url_for, flash  # Flask와 관련된 여러 기능을 가져옴
from datetime import timedelta  # 시간 관련 기능을 가져옴
import database as db  # 'database'라는 모듈을 'db'로 가져옴

app = Flask(__name__)  # Flask 앱을 만듦
app.secret_key = 'hello1234'  # 세션 암호화를 위한 비밀 키 설정
app.permanent_session_lifetime = timedelta(minutes=5)  # 세션 지속 시간을 5분으로 설정

@app.route('/')  # 루트 경로에 대한 처리
def home():
    return render_template('index.html')  # 'index.html' 템플릿을 렌더링하여 반환

@app.route('/login', methods=['GET', 'POST'])  # '/login' 경로에 대한 GET과 POST 요청 처리
def login():
    if request.method == 'POST':  # 요청이 POST인 경우
        # 로그인 처리 구현
        username = request.form["username"]  # 폼에서 'username' 값을 가져옴
        password = request.form["password"]  # 폼에서 'password' 값을 가져옴

        # 사용자 데이터를 외부 DB에서 가져오기
        # query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user_data = db.get_query("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))  # 사용자 정보를 DB에서 조회
        print(f"조회된 사용자: ", user_data)

        if len(user_data) == 1:  # 사용자가 한 명 존재하고,
            session["user"] = username  # 세션에 사용자 이름을 저장
            session.permanent = True  # 세션을 영구적으로 설정
            print("패스워드 맞음!!")
            flash("로그인에 성공하였습니다.")  # 성공 메시지 표시
            return redirect(url_for("home"))  # 홈 페이지로 리디렉션
        else:
            print('패스워드 틀림!!')
            flash("아이디/패스워드가 일치하지 않습니다.")  # 실패 메시지 표시
            # 메세지가 있으면 전달하고, 없으면 그냥 재 로그인
            return redirect(url_for("login"))  # 로그인 페이지로 리디렉션
    else:  # GET 요청인 경우
        # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:  # 세션에 사용자가 이미 존재하면
            print("이전에 로그인 했음!!")
            return redirect(url_for("home"))  # 홈 페이지로 리디렉션

    return render_template('login.html')  # 로그인 폼 렌더링

@app.route('/user', methods=['GET', 'POST'])  # '/user' 경로에 대한 GET과 POST 요청 처리
def user():
    if "user" in session:  # 세션에 사용자가 존재하면
        user = session['user']

        if request.method == 'POST':  # 요청이 POST인 경우
            action = request.form["action"]  # 폼에서 'action' 값을 가져옴
            if action == "update_email":
                email = request.form["email"]  # 폼에서 'email' 값을 가져옴
                if email:
                    db.execute_query("UPDATE users SET email = ? WHERE username = ?", (email, user))  # 이메일을 DB에서 업데이트
                    flash("이메일이 변경되었습니다.")
                else:
                    flash("이메일을 입력해주세요.")
            elif action == "update_password":
                password = request.form["password"]  # 폼에서 'password' 값을 가져옴
                if password:
                    db.execute_query("UPDATE users SET password = ? WHERE username = ?", (password, user))  # 비밀번호를 DB에서 업데이트
                    flash("비밀번호가 변경되었습니다.")
                else:
                    flash("비밀번호를 입력해주세요.")
            elif action == "delete":
                db.execute_query("DELETE FROM users WHERE username = ?", (user,))  # 사용자를 DB에서 삭제
                session.pop("user", None)  # 세션에서 사용자 제거
                flash("계정이 삭제되었습니다.")
                return redirect(url_for("login"))  # 로그인 페이지로 리디렉션
        
        return render_template('user.html', user=user)  # 'user.html' 템플릿을 렌더링하여 사용자 정보를 표시
    else:
        flash("로그인이 필요합니다.")  # 로그인 필요 메시지 표시
        return redirect(url_for("login"))  # 로그인 페이지로 리디렉션

@app.route('/view')  # '/view' 경로에 대한 처리
def view():
    # users = [] # 미션1. DB 쿼리해서 모든 사용자 목록을 받아온다
    users = db.get_query("SELECT * FROM users", ())  # DB에서 모든 사용자 정보를 조회
    return render_template("view.html", users=users)  # 'view.html' 템플릿을 렌더링하여 사용자 목록을 표시

@app.route('/signin', methods=['GET', 'POST'])  # '/signin' 경로에 대한 GET과 POST 요청 처리
def signin():
    if request.method == "POST":  # 요청이 POST인 경우
        username = request.form["username"]  # 폼에서 'username' 값을 가져옴
        password = request.form["password"]  # 폼에서 'password' 값을 가져옴
        
        db.execute_query("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))  # DB에 사용자 정보를 삽입
        print('회원가입 완료.')
        flash('회원가입이 완료되었습니다.')  # 성공 메시지 표시
        
        return redirect(url_for('home'))  # 홈 페이지로 리디렉션
    return render_template('signin.html')  # 'signin.html' 템플릿을 렌더링하여 회원가입 폼을 표시

@app.route('/logout')  # '/logout' 경로에 대한 처리
def logout():
    session.pop("user", None)  # 세션에서 사용자 제거
    flash("로그아웃에 성공하였습니다.")  # 성공 메시지 표시
    return redirect(url_for("login"))  # 로그인 페이지로 리디렉션

@app.route('/board', methods=['GET', 'POST'])  # '/board' 경로에 대한 GET과 POST 요청 처리
def board():
    if "user" in session:  # 세션에 사용자가 존재하면
        if request.method == 'POST':  # 요청이 POST인 경우
            title = request.form["title"]  # 폼에서 'title' 값을 가져옴
            content = request.form["content"]  # 폼에서 'content' 값을 가져옴
            user = session["user"]
            user_data = db.get_query("SELECT id FROM users WHERE username = ?", (user,))
            if user_data:
                user_id = user_data[0]["id"]
                db.execute_query("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, user_id))  # 게시물 정보를 DB에 삽입
                flash("게시물이 작성되었습니다.")  # 성공 메시지 표시
                return redirect(url_for("board"))  # 게시판 페이지로 리디렉션

        posts = db.get_query("SELECT p.id, p.title, p.content, u.username, p.created_at FROM posts p JOIN users u ON p.user_id = u.id", ())  # DB에서 게시물 정보를 조회
        return render_template("board.html", posts=posts)  # 'board.html' 템플릿을 렌더링하여 게시물 목록을 표시
    else:
        flash("로그인이 필요합니다.")  # 로그인 필요 메시지 표시
        return redirect(url_for("login"))  # 로그인 페이지로 리디렉션
    
if __name__ == "__main__":
    db.init_db()   # 시스템 부팅 시에 DB 초기화
    print('DB 초기화 완료')
    app.run(debug=True)  # 플라스크 앱 실행
