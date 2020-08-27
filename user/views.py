from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from flask import render_template
from sqlalchemy.orm.exc import NoResultFound

from libs.orm import db
from libs.utils import save_avatar, check_password, login_required, make_password
from user.models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        city = request.form.get('city')
        phone = request.form.get('phone')

        user = User(username=username, password=make_password(password), city=city, phone=phone)

        db.session.add(user)
        db.session.commit()
        # 如果用户名冲突的话 需要处理 此处没有处理
        return render_template('login.html')
    else:
        return render_template('register.html')


@user_bp.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 查询数据库
        try:
            user = User.query.filter_by(username=username).one()
            if check_password(password, user.password):
                session['uid'] = user.id
                session['username'] = user.username
                return redirect('/user/info')
            else:
                return render_template('login.html', err='密码错误')
        except:
            return render_template('login.html', err='该用户不存在')
    else:
        return render_template('login.html')


@user_bp.route('/info')
def info():
    '''查看用户信息'''
    uid = session['uid']
    user = User.query.get(uid)
    return render_template('info.html', user=user, uid=uid)


@user_bp.route('/logout')
def logout():
    '''退出功能'''
    session.clear()
    return redirect('/user/login')
