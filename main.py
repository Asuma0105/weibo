from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from libs.orm import db
from user.views import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://xlx:a7264760@localhost:3306/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 注册蓝图
app.register_blueprint(user_bp)

if __name__=='__main__':
    manager.run()