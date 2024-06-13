# 백과 프론트를 완전히 분리하는 과정..
# 확인할 때는 html파일을 브라우저로 열면된다.
# render_template 을 완전히 삭제하고 jsonify로 대체함!!!
from flask import Flask, session, request, jsonify, send_from_directory
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'this-is-secret'

# 사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw':'1234'},
    {'name': 'Bob', 'id': 'bob', 'pw':'12345'},
    {'name': 'Charlie', 'id': 'charlie', 'pw':'123456'},
]

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/profile')
def profile():
    return send_from_directory('static', 'profile.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    if request.method == 'POST':
        # 로그인 처리를 해야함
        # id = request.form['id'] # request.form.get('id', None)
        # password = request.form['password']
        
        # 데이터를 json으로 처리해서 받아야함
        data = request.json
        id = data.get('id')
        pw = data.get('pw')
        
        # 이 사용자가 목록에 있는지 검사
        # user = None
        # for u in users:
        #     if u['id'] == id and u['pw'] == password:
        #         user = u
        
    user = next(( u for u in users if u['id'] == id and u['pw'] == password), None) # None은 시작값... 위 네줄을 한줄로 줄인 것
        
    if user:
        session['user'] = user # 로그인한 사용자 정보를 session에 저장
        # return f'사용자 맞음/ 로그인한 사용자: {user['name']}'
        return jsonify({'status': 'success', 'message': '로그인에 성공하였습니다.'})
    else:
        # return render_template('index.html', error='사용자 없음')
        return jsonify({'status': 'error', 'message': '로그인에 실패하였습니다.'})
    # get요청일 때는 페이지를 보내줌
    # return render_template('index.html')

# 미션1. profile에도 get 하는데, post 할수도 있어야 함....
@app.route('/api/profile', methods=['GET', 'POST'])
def profile():
    user = session.get('user') # 위에서 세션에 저장한 것 다시 찾아오기 
    # user = {'name':'unknown', 'id':'idk', 'pw': 'idrk'} # (화면에 띄우기 위한 더미데이터)
    # return render_template('profile3.html', user=user)

# 미션2. if post 요청이 왔으면??
# 세션에서 user정보 가져와서, 이것을 우리의 user db에서 검색해서
# pw를 변경한다.    
    if request.method == 'POST':
        new_pw = request.form['new_password']
        # 나의 db 변경
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw
                
# 미션3. 사용자에게 성공 결과를 보내준다. 
        # return render_template('profile3.html', user=user, message = "비밀번호가 변경되었습니다.")
        return jsonify({'status':'ok', 'message':'비밀번호가 변경되었습니다.'})
    
    # return render_template('profile3.html', user=user)
    return jsonify({'status': 'success', 'user': user})

@app.route('/api/logout')
def logout():
    session.pop('user', None) # 세션에서 사용자 정보 삭제
    return jsonify({'status': 'success', 'message': '로그아웃에 성공하였습니다.'})
    # return redirect(url_for('home')) # 로그아웃 이후 홈으로..

if __name__ == "__main__":
    app.run(debug=True)