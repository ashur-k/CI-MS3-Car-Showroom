from flask import app, Blueprint, render_template, redirect, url_for, request, flash, session
from passlib.hash import pbkdf2_sha256
from database import mongo
from bson.objectid import ObjectId


login = Blueprint("login", __name__, static_folder="static", template_folder="templates")


@login.route("/home")
@login.route("/admin_login")
def admin_login():
    if 'username' in session:
        return redirect(url_for('admin.admin_homepage'))
    return render_template('admin_login.html')


@login.route('/login', methods=['POST', 'GET'])
def logging_in():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})
    password_entered = request.form['password']
    if login_user:
        if pbkdf2_sha256.verify(password_entered, login_user['user_pwd']):
            session['username'] = request.form['username']
            return redirect(url_for('admin.admin_homepage'))
        flash('Invalid username/password provided')
        return redirect(url_for('login.admin_login'))

    else:
        flash('Invalid username/password provided')
        return redirect(url_for('login.admin_login'))


@login.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
       
        existing_user = mongo.db.users.find_one({'name': request.form['username']})

        if existing_user is None:
            hash = pbkdf2_sha256.hash(request.form['user_pwd'])
            mongo.db.users.insert({'name': request.form['username'], 'user_pwd': hash, 'user_email': request.form['user_email'], 'user_role': request.form['user_role']})
            flash('User name {} has been created.'.format(request.form['username']))
            return redirect(url_for('login.register'))

        flash('User name {} already exists in database.'.format(request.form['username']))
    return render_template('register_user.html', admin_cars_make=mongo.db.car_make.find())


@login.route('/signout')
def signout():
    session.clear()
    return redirect(url_for('login.admin_login'))
