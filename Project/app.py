from flask import Flask, render_template, request
from database import get_users, get_total_users, get_user_by_name, get_user_by_gender, get_user_by_name_and_gender, get_total_user_by_name, get_total_user_by_gender, get_total_user_by_name_and_gender, get_orders, get_total_orders, get_orderItems, get_total_orderItems, get_items, get_total_items, get_stores, get_total_stores
import math
app = Flask(__name__)

app.secret_key = "thisissydneysproject"
# app.permanent_session_lifetime = timedelta(minutes=10)

# @app.route('/')
# def home():
#     return app.send_static_file('index.html')
    
@app.route('/crm/users/', methods=['GET'])
def crm_users():
    name = request.args.get('name')
    gender = request.args.get('gender')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if name and gender:
        users = get_user_by_name_and_gender(name, gender, page, per_page)
        total_users = get_total_user_by_name_and_gender(name, gender, page, per_page)
        total_pages = math.ceil(total_users / per_page)
    elif name:
        users = get_user_by_name(name, page, per_page)
        total_users = get_total_user_by_name(name, page, per_page)
        total_pages = math.ceil(total_users / per_page)
    elif gender:
        users = get_user_by_gender(gender, page, per_page)
        total_users = get_total_user_by_gender(gender, page, per_page)
        total_pages = math.ceil(total_users / per_page)
    else:
        users = get_users(page, per_page)
        total_users = get_total_users()
        total_pages = math.ceil(total_users / per_page)
    
    return render_template('users.html', users=users, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/crm/orders/')
def crm_orders():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    total_orders = get_total_orders()
    total_pages = math.ceil(total_orders / per_page)
    
    orders = get_orders(page, per_page)
    
    return render_template('orders.html', orders=orders, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/crm/orderItems/')
def crm_orderItems():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    total_orderItems = get_total_orderItems()
    total_pages = math.ceil(total_orderItems / per_page)

    orderItems = get_orderItems(page, per_page)
    return render_template('orderItems.html', orderItems=orderItems, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/crm/items/')
def crm_items():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    total_items = get_total_items()
    total_pages = math.ceil(total_items / per_page)
    
    items = get_items(page, per_page)
    return render_template('items.html', items=items, page=page, per_page=per_page, total_pages=total_pages)

@app.route('/crm/stores/')
def crm_stores():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    total_stores = get_total_stores()
    total_pages = math.ceil(total_stores / per_page)
    
    stores = get_stores(page, per_page)
    return render_template('stores.html', stores=stores, page=page, per_page=per_page, total_pages=total_pages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
