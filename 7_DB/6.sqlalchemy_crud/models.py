from flask_sqlalchemy import SQLAlchemy

# flask - SQLAlchemy 를 연결
#          일단 비워둠
db = SQLAlchemy()

# 클래스를 통해서 db테이블을 설계/설정할 수 있음
class User(db.Model):
    __tablename__ = 'users' # 옵셔널 한 것,, 테이블명이 클래스명과 다를 때 설정
    id = db.Column(db.Integer, primary_key=True) # PRIMARY KEY
    name = db.Column(db.String(20), nullable=False) # VARCHAR(20), NOT NULL
    age = db.Column(db.Integer,nullable=False)
    
    def __repr__(self): # 나의 객체를 누군가 print 할 때, 표현해주고 싶은 함수를 구현하면 됨
        return f'<사용자: {self.id}, {self.name}, {self.age}>'
        