from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from flask import render_template
from sqlalchemy.orm.exc import NoResultFound

from libs.orm import db
from libs.utils import save_avatar, check_password, login_required
from user.models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/register')
def register():
    if request.method == 'POST':
        avatar = request.form.get('avatar').strip()  # 头像，保存它的url
        username = request.form.get('username').strip()
        password = request.form.get('password').strip() # 为了存储加密后的密码，所以长一点
        gender = request.form.get('gender').strip()
        city = request.form.get('city').strip()
        phone = request.form.get('phone').strip()

        user = User(username = username, password = password, gender = gender, city = city, phone = phone)

        # 保存头像
        avatar_file = request.files.get('avatar')
        if avatar_file:
            user.avatar = save_avatar(avatar_file)

        try:
            # 保存到数据库
            db.session.add(user)
            db.session.commit()
            return redirect('/user/login')
        except InterruptedError:
            db.session.rollback()
            return render_template('register.html', err = '您的昵称已被占用')
    else:
        return render_template('register.html')



@user_bp.route('/login', methods = ('POST', 'GET'))
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip() # 为了存储加密后的密码，所以长一点

        # 获取用户
        try:
            user = User.query.filter_by(username=username).one()
        except NoResultFound:
            return render_template('login.html',err='该用户不存在')

        # 检查密码
        if check_password(password, user.password):
            # 在session中记录用户的登录状态
            session['uid'] = user.id
            session['nickname'] = user.username
            return redirect('/user/info')
        else:
            return render_template('login.html', err = '密码错误')
    else:
        return render_template('login.html')


@user_bp.route('/info')
@login_required
def info():
    '''查看用户信息'''
    return 'info.html'


@user_bp.route('/logout')
def logout():
    '''退出功能'''
    session.clear()
    return redirect('/')
