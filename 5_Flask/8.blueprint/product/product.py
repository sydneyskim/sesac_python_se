from flask import Blueprint, render_template

product_app = Blueprint('product', __name__)

@product_app.route('/') #여기서의 / 는 blueprint를 등록한 app 에서 정의한 prefix의 하위 디렉토리
def home():
    return render_template('product/index.html')

@product_app.route('/fruit')
def fruit():
    return render_template('product/fruit.html')

@product_app.route('/drink')
def drink():
    return render_template('product/drink.html')