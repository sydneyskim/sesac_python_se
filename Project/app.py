from flask import Flask, render_template, request
from database import get_user_by_name, get_users

app = Flask(__name__)
app.secret_key = "thisissydneysproject"
# app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/crm/users/')
def crm_users():
    name = request.args.get('name')
    if name:
        users = get_user_by_name(name)
    else:
        users = get_users()
        
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
