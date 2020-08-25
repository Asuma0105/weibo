from hashlib import sha256, md5
import os

from flask import session, redirect


def make_password(password):
    '''产生一个安全密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')


    # 计算哈希值
    hash_value = sha256(password).hexdigest()

    # 产生随机盐，长度32字节
    salt = os.urandom(16).hex()
    # 加盐，产生安全密码
    safe_password = salt + hash_value
    return safe_password

def check_password(password, safe_password):
    '''检查密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')

        # 计算哈希值
        hash_value = sha256(password).hexdigest()

        return hash_value == safe_password[32:]

def save_avatar(avatar_file):
    '''保存头像文件'''
    # 读取文件的二进制数据
    file_bin_data = avatar_file.stream.read()

    # 指针归零
    avatar_file.stream.seek(0)

    # 计算文件md5值
    filename = md5(file_bin_data).hexdigest()

    # 获取项目文件夹的绝对路径
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 文件绝对路径
    filepath = os.path.join(base_dir, 'static', 'upload', filename)

    # 保存文件
    avatar_file.save(filepath)

    # 文件的URL
    avatar_url = f'/static/upload/{filename}'

    return avatar_url

def login_required(view_func):
    def check_session(*args, **kwargs):
        uid = session.get('uid')
        if not uid:
            return redirect('/user/login')
        else:
            return view_func(*args, *kwargs)
    return check_session()