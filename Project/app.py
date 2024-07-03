from flask import Flask, render_template, request, redirect, url_for
from database import (get_users, get_total_users, get_user_by_name, get_user_by_gender, 
                      get_user_by_name_and_gender, get_total_user_by_name, get_total_user_by_gender,
                      get_total_user_by_name_and_gender, get_orders, get_total_orders, get_orderItems, 
                      get_total_orderItems, get_items, get_total_items, get_stores, get_total_stores, 
                      get_userdetail, get_userorderdetail, get_orderitemdetail, get_order_by_date, 
                      get_total_order_by_date, get_orderdetail, get_itemdetail, get_storedetail, get_monthlyrevenue,
                      get_item_monthlyrevenue, get_top5_stores, get_top5_items, get_regular_customers,
                      get_store_by_name, get_total_store_by_name, get_item_by_type, get_total_item_by_type )
import math

app = Flask(__name__)

app.secret_key = "thisissydneysproject"

@app.route('/')
def crm_main():
    return redirect(url_for('crm_users'))


### user ###
# user 목록   
@app.route('/crm/users/', methods=['GET'])
def crm_users():
    name = request.args.get('name')
    gender = request.args.get('gender')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if name and gender:
        users = get_user_by_name_and_gender(name, gender, page, per_page)
        total_users = get_total_user_by_name_and_gender(name, gender)
        total_pages = math.ceil(total_users / per_page)
    elif name:
        users = get_user_by_name(name, page, per_page)
        total_users = get_total_user_by_name(name)
        total_pages = math.ceil(total_users / per_page)
    elif gender:
        users = get_user_by_gender(gender, page, per_page)
        total_users = get_total_user_by_gender(gender)
        total_pages = math.ceil(total_users / per_page)
    else:
        users = get_users(page, per_page)
        total_users = get_total_users()
        total_pages = math.ceil(total_users / per_page)
    
    return render_template('users.html', users=users, name=name, gender=gender, page=page, per_page=per_page, total_pages=total_pages)

# user 상세
@app.route('/crm/userdetail/')
def crm_userdetail():
    user_id = request.args.get('userid')
    user_detail = get_userdetail(user_id)
    user_order_detail = get_userorderdetail(user_id)
    top5_stores = get_top5_stores(user_id)
    top5_items = get_top5_items(user_id)

    return render_template('userdetail.html', user_detail=user_detail[0], user_order_detail=user_order_detail, top5_stores=top5_stores, top5_items=top5_items)

### order ###
# order 목록  
@app.route('/crm/orders/')
def crm_orders():
    date = request.args.get('date')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if date:
        total_orders = get_total_order_by_date(date)
        total_pages = math.ceil(total_orders / per_page)
        orders = get_order_by_date(date, page, per_page)
    else:
        total_orders = get_total_orders()
        total_pages = math.ceil(total_orders / per_page)
        orders = get_orders(page, per_page)
    
    return render_template('orders.html', orders=orders, date=date, page=page, per_page=per_page, total_pages=total_pages)

# order -> orderitem 상세
@app.route('/crm/orderitemdetail/')
def crm_orderitemdetail():
    order_id = request.args.get('orderid')
    order_detail = get_orderitemdetail(order_id)
    orderitem_detail = get_orderdetail(order_id)

    return render_template('orderitemdetail.html', order_detail=order_detail)

### order item ###
# order item 목록 
@app.route('/crm/orderItems/')
def crm_orderItems():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    total_orderItems = get_total_orderItems()
    total_pages = math.ceil(total_orderItems / per_page)

    orderItems = get_orderItems(page, per_page)
    return render_template('orderItems.html', orderItems=orderItems, page=page, per_page=per_page, total_pages=total_pages)

# orderitem -> order 상세
@app.route('/crm/orderdetail/')
def crm_orderdetail():
    order_id = request.args.get('orderid')
    orderitem_detail = get_orderdetail(order_id)
    
    return render_template('orderdetail.html', orderitem_detail=orderitem_detail)

# orderitem -> item 상세
@app.route('/crm/itemdetail/')
def crm_itemdetail():
    item_id = request.args.get('itemid')
    orderitem_detail = get_itemdetail(item_id)
    item_monthly_revenue = get_item_monthlyrevenue(item_id)
    
    return render_template('itemdetail.html', orderitem_detail=orderitem_detail, item_monthly_revenue=item_monthly_revenue)

### item ###
# item 목록 
@app.route('/crm/items/')
def crm_items():
    type = request.args.get('type')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if type:
        items = get_item_by_type(type, page, per_page)
        total_items = get_total_item_by_type(type)
        total_pages = math.ceil(total_items / per_page)
    else:
        items = get_items(page, per_page)
        total_items = get_total_items()
        total_pages = math.ceil(total_items / per_page)
    
    return render_template('items.html',type=type, items=items, page=page, per_page=per_page, total_pages=total_pages)

### store ###
# store 목록 
@app.route('/crm/stores/')
def crm_stores():
    name = request.args.get('name')
    address = request.args.get('address')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if name:
        stores = get_store_by_name(name, page, per_page)
        total_stores = get_total_store_by_name(name)
        total_pages = math.ceil(total_stores / per_page)
    else:
        stores = get_stores(page, per_page)
        total_stores = get_total_stores()
        total_pages = math.ceil(total_stores / per_page)
    
    return render_template('stores.html', stores=stores, name=name, address=address, page=page, per_page=per_page, total_pages=total_pages)

# store 상세
@app.route('/crm/storedetail/')
def crm_storedetail():
    store_id = request.args.get('storeid')
    store_detail = get_storedetail(store_id)
    store_monthly_revenue = get_monthlyrevenue(store_id)
    regular_customers = get_regular_customers(store_id)
    
    return render_template('storedetail.html', store_detail=store_detail, store_monthly_revenue=store_monthly_revenue, regular_customers=regular_customers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
