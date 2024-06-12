from flask import Blueprint, render_template

user_app = Blueprint('user', __name__)

@user_app.route('/') #여기서의 / 는 blueprint를 등록한 app 에서 정의한 prefix의 하위 디렉토리
def home():
    return render_template('user/index.html')
