from flask import Flask, request, render_template, session, flash, redirect, url_for
from datetime import timedelta
import database as db

app = Flask(__name__) # Flask 앱을 만듦
app.secret_key = "thisissecretkey" # 세션 암호화를 위한 비밀 키 설정
app.permanent_session_lifetime = timedelta(minute = 5) # 세션 지속 시간을 5분으로 설정

@app.route('/')
def home():
    return render_template('index.html') # 'index.html' 템플릿을 렌더링하여 반환

@app.route('/login', method=['GET','POST']) # '/login' 경로에 대한 GET과 POST 요청 처리
def login():
    if request.method == "POST": # 요청이 POST인 경우
         # 로그인 처리 구현
        username = request.form["username"] # 폼에서 'username' 값을 가져옴
        ppassword = request.form["password"]  #폼에서 'password' 값을 가져옴
        
         # 사용자 데이터를 외부 DB에서 가져오기
        user_data = db.get_query("SELECT * FROM users WHERE username = ? AND password = ?")
        print(f'조회돤 사용자:', user_data)
        
        if len(user_data) == 1: # 사용자가 한 명 존재하고,
            session["user"] == username # 세션에 사용자 이름을 저장
            session.permanent = True # 세션을 영구적으로 설정
            print("올바른 패스워드입니다.")
            flash("로그인에 성공했습니다.") # 성공 메세지 flash
            return redirect(url_for("home")) # 로그인 페이지로 리디렉션 
        else:
            print("올바르지 않은 패스워드입니다.")
            flash("로그인에 실패했습니다.")
            return redirect(url_for("login"))
    else: # GET 요청일 경우
        # GET 요청이라 로그인 폼 보여주기
        if "user" in session: # 세션에 사용자가 이미 존재하면
            print("이미 로그인 된 사용자입니다.")
            return redirect(url_for("home"))
    
    return render_template('login.html') # 로그인 폼 렌더링

@app.route('/user', methods=['GET', 'POST']) # '/user' 경로에 대한 GET과 POST 요청 처리
def user():
    if "user" in session: # 세션에 사용자가 존재하면
        user = session["user"]
        
        if request.method == "POST": # 요청이 POST인 경우
            action = request.form["action"] # 폼에서 'action' 값을 가져옴
            if action == "update_email":
                email = request.form["email"] # 폼에서 'email' 값을 가져옴
                if email:
                    db.execute_query("UPDATE users SET email = ? WHERE username = ?", (email, user))
                    flash("이메일이 변경되었습니다.")
                else:
                    flash("이메일을 입력해주세요")
            elif action == "update_password":
                password = request.form["password"] # 폼에서 'password' 값을 가져옴
                