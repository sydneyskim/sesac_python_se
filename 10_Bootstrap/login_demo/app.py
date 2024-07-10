from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'hello1234'

DATABASE = 'user.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
            )
        ''')
    
    db.commit()
    cursor.close()
    db.close()

def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, hashed_password))
        db.commit()
        print(f"User {username} created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error creating user {username}: {e}")
    
    cursor.close()
    db.close()

def query_db(query, args=(), isOne=False):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return (result[0] if result else None) if isOne else result

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = query_db('SELECT * FROM users WHERE username=?', (username,), isOne=True)
        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user[2]):
            print('사용자 로그인 성공')
            flash('로그인 성공', 'success')
            return redirect(url_for('dashboard'))
        else:
            print('사용자 로그인 실패')
            flash('로그인 실패', 'danger')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    init_database()

    users = [
        ('user1', 'pass1'),
        ('user2', 'pass2')
    ]
    
    for username, password in users:
        create_user(username, password)
        
    app.run(debug=True)
