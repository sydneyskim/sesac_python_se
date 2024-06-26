from flask import Flask, render_template, request
from database import get_user_by_name, get_users, get_user_by_gender, get_user_by_name_and_gender

app = Flask(__name__)
app.secret_key = "thisissydneysproject"
# app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/crm/users/')
def crm_users():
    name = request.args.get('name')
    gender = request.args.get('gender')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page
    
    if name and gender:
        users = get_user_by_name_and_gender(name, gender, offset=offset, limit=per_page)
        total_count = len(get_user_by_name_and_gender(name, gender, offset=0, limit=10000)) 
    elif name:
        users = get_user_by_name(name, offset=offset, limit=per_page)
        total_count = len(get_user_by_name(name, offset=0, limit=10000)) 
    elif gender:
        users = get_user_by_gender(gender, offset=offset, limit=per_page)
        total_count = len(get_user_by_gender(gender, offset=0, limit=10000)) 
    else:
        users = get_users(offset=offset, limit=per_page)
        total_count = len(get_users(offset=0, limit=10000)) # 전체 사용자의 수를 구함
    
    total_pages = (total_count + per_page - 1) // per_page # 전체 페이지 수 계산
    
    return render_template('users.html', users=users, page=page, per_page=per_page, total_pages=total_pages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
