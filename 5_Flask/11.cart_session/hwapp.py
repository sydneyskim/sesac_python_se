from flask import Flask, session, render_template, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'abcd1234'
app.permanent_session_lifetime = timedelta(minutes=5) # 5분후에 만료시키고자 함

# 상품 DB
items = {
    'item1': {'name': 'Americano', 'price': 4500, 'image': 'item1.jpg'},
    'item2': {'name': 'Cafe Latte', 'price': 5000, 'image': 'item2.jpg'},
    'item3': {'name': 'Frapuccino', 'price': , 'image': 'item3.jpg'},
}

@app.route('/')
def index():
    return render_template('hwindex.html', items=items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    print (f'상품담기: {item_name}')
    # 상품을 세션안의 cart라는 변수에 담기
    if 'cart' not in session:
        session['cart'] = {}
        session.permanent = True
        
    # 카트 안에 물건을 담기
    if item_name in session['cart']: # 이전에 담은적 있는 상품인지 확인
        session['cart'][item_name] += 1 # 이미 담겨진 상품이면 갯수를 1 증가
    else: # 이전에 담은적이 없으면
        item_info = items.get(item_name) # 해당 상품을 DB에서 조회
        if item_info: # 해당 상품이 DB에 있는 경우
            session['cart'][item_name] = 1 # 신규 상품으로 1 추가
            
    # 세션 정보가 변경된 것을 알려주기
    session.modified = True
    return redirect(url_for('index'))

@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    print(f'상품 지우기: {item_name}')
    # 상품 지우는 코드 작성하기
    if 'cart' in session and item_name in session['cart']: # 장바구니도 만들어져있고, 우리가 지우려고 하는 상품도 있는지 확인
        session['cart'].pop(item_name)
        session.modified = True
    
    return redirect(url_for('view_cart'))

@app.route('/clear_cart')
def clear_cart():
    print(f'카트 비우기')
    # 카트 통째로 비우기 세션내의 ('cart')삭제하면 됨
    if 'cart' in session:
        session.pop('cart')
        session.modified = True
        
    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    cart_items = {}
    total_price = 0
    
    # 카트의 담긴 상품과 수량과 가격 조회하기
    for item_name, quantity in session.get('cart', {}).items(): # 세션 안의 cart라는 변수의 dict 깨체들 가ㅕㅈ오기
        item = items.get(item_name) # 첫번째 항목의 아이템을 DB에서 조회하기
        if item:
            # 프론트에서 표현하기 위한 key, value 들을 모아서 담기, 그리고 total_price에 합산 가격 담기
            cart_items[item_name] = {'name':item['name'], 'quantity':quantity, 'price': item['price'], 'image': item['image']}
            total_price += item['price'] * quantity
    return render_template('hwcart.html', cart_items=cart_items, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True)