import sqlite3
import os
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, g
from flask import flash, session, make_response
from werkzeug.utils import secure_filename

from apps import app
from apps.db import Database
from apps.forms import RegistForm, LoginForm, PwdForm
from apps.tools import creat_folder, secure_filename_with_timestamp


@app.before_request
def connect_db():
    g.db = sqlite3.connect(app.config['DATABASE'])

@app.teardown_request
def close_db(exception):
    if 'db' in g:
        g.db.close()

# 登陆检查
def login_check(func):
    @wraps(func)
    def check(*args, **kwargs):
        if 'user_name' not in session:
            return redirect(url_for('user_login', next=request.url))
        return func(*args, **kwargs)
    return check
        
@app.route('/')
def index():
    print(Database(g.db).sql_select_total())
    resp = make_response(render_template('index.html'))
    return resp

@app.route('/login/', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if request.method == 'POST':
        user_name = form.data['user_name']
        user_pwd = form.data['user_pwd']

        db = Database(g.db).sql_select(user_name)
        if db is not None and db[-1] == user_pwd:
            session['user_name'] = user_name
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误')
            return render_template('user_login2.html', form=form)
    return render_template('user_login2.html', form=form)

@app.route('/regist/', methods=['GET', 'POST'])
def user_regist():
    form = RegistForm()
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_pwd = request.form['user_pwd']
        
        db = Database(g.db)
        db_l = db.sql_select(user_name)
        if db_l is not None:
            flash('用户名已存在')
            return render_template('user_regist2.html', form=form) 
        else:
            db.sql_insert(user_name, user_pwd)
            flash('注册成功, 请登陆')
            return redirect(url_for('user_login', name=user_name))

    return render_template('user_regist2.html', form=form)
    
@app.route('/exit/', methods=['GET', 'POST'])
@login_check
def user_exit():
    session.pop('user_name', None)
    return redirect(url_for('index'))

@app.route('/center/', methods=['GET'])
@login_check
def user_center():
    return render_template('user_center.html')

@app.route('/center/info', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filename = secure_filename_with_timestamp(filename)
        print(filename)
        user_path = os.path.join(app.config['UPLOADS_FOLDER'], session['user_name'])
        creat_folder(user_path)
        file.save(os.path.join(user_path, filename))
        return redirect('/')
    return render_template('user_info.html')

@app.route('/center/pwd', methods=['GET', 'POST'])
@login_check
def user_pwd():
    form = PwdForm()
    if form.validate_on_submit():
        old_pwd = form.data['old_pwd']
        new_pwd = form.data['new_pwd']

        user = Database(g.db).sql_select(session.get('user_name'))
        if str(old_pwd) == user[-1]:
            db = Database(g.db)
            db.sql_update(user[1], new_pwd)
            session.pop('user_name', None)
            flash('修改密码成功')
            return redirect(url_for('user_login'))
        else:
            flash('旧密码输入错误')
            return render_template('user_pwd2.html', form=form)

    return render_template('user_pwd2.html', form=form)

@app.route('/center/del')
@login_check
def user_del():
    return render_template('user_del.html')

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-somthing'] = 'Milllu'
    return resp