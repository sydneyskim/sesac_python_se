from flask import Flask, jsonify, request
from database import get_store_by_name, get_stores
app = Flask(__name__)

# Web 서버를 대신해주는 코드.. (지금은 웹서버가 없기 때문.. )
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/stores/')
def api_stores():
    
    name = request.args.get('name')
    if name:
        stores = get_store_by_name(name)
    else:
        stores = get_stores()
    return jsonify(stores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)