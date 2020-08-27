from libs.orm import db


class User(db.Model):
    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # 为了存储加密后的密码，所以长一点
    city = db.Column(db.String(10), default='中国')
    phone = db.Column(db.String(16))