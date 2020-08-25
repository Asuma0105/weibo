from libs.orm import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(265), default='/static/img/default/png') # 头像，保存它的url
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128), nullable=False)  # 为了存储加密后的密码，所以长一点
    gender = db.Column(db.Enum('male', 'female', 'unknow'), default='unknow')
    city = db.Column(db.String(10), default='中国')
    phone = db.Column(db.String(16))