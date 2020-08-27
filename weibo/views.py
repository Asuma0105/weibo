import datetime

from Tools.scripts.make_ctype import method
from flask import Blueprint, render_template, request, session, redirect

from libs.orm import db
from weibo.models import Article

article_bp = Blueprint(
    'article',
    __name__,
    url_prefix='/weibo',
    template_folder='./templates'
)


@article_bp.route('/show', methods=('POST', 'GET'))
def show():
    pass


@article_bp.route('/publish', methods=('POST', 'GET'))
def publish():
    if request.method == 'POST':
        content = request.form.get('content')
        if len(content) < 150:
            uid = session['uid']
            now = datetime.datetime.now()

            article = Article(article=content, uid=uid, created=now, changed=now)

            db.session.add(article)
            db.session.commit()
            return redirect('/weibo/read?wid=%s' % article.id)
        else:
            return render_template('publish.html', err='字数超出限制')
    else:
        return render_template('publish.html')


@article_bp.route('/change', methods=('POST', 'GET'))
def change():
    pass


@article_bp.route('/read', methods=('POST', 'GET'))
def read():
    wid = int(request.args.get('wid'))
    weibo = Article.query.get(wid)
    return render_template('read.html', article=weibo)
