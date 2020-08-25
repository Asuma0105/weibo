from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from flask import render_template

from user.models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/register')
def register():
    return 'register.html'


@user_bp.route('/login')
def login():
    return 'login.html'


@user_bp.route('/info')
def info():
    return 'info.html'


@user_bp.route('/logout')
def logout():
    return 'login.html'
