from libs.orm import db

class Article(db.Model):
    __tablename__='article'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False) # 发表者id
    article = db.Column(db.String(300))
    created = db.Column(db.DateTime, nullable=False) # 发表微博时间
    changed = db.Column(db.DateTime, nullable=False) # 修改微博时间