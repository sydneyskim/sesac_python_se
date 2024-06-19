from flask import Flask
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = "thisissecretkey"
app.permanent_session_lifetime = timedelta(minute = 5)

# 사용자 DB
DATABASE = 'user.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # 행을 sqlite3.Row라는 객체 타입으로 반환
                                   # 이걸 설정하면 각 Row의 결과는 Dict 유형으로 반환됨
    return conn

def init_db():
    with app.app_context():
        conn =