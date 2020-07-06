from flask import app, Blueprint, render_template, redirect, url_for, request, flash, session
from passlib.hash import pbkdf2_sha256
from database import mongo
from bson.objectid import ObjectId


login = Blueprint ("login", __name__, static_folder="static", template_folder="templates")


@login.route("/home")
@login.route("/")
def home():
    return render_template('admin_login.html')


@login.route('/login', methods=['POST', 'GET'])
def logging_in():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})
    password_entered = request.form['password']
    if login_user:
        if pbkdf2_sha256.verify(password_entered, login_user['user_pwd']):
            session['username'] = request.form['username']
            return redirect (url_for('admin'))
        flash('Invalid password provided')
        return redirect(url_for('login.home'))

    else:
        flash(u'Invalid password provided', 'error')
        return redirect(url_for('login.home'))


@login.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user_email = users.find_one({'email': request.form['user_email']})

        if existing_user_email is None:
            hash = pbkdf2_sha256.hash(request.form['user_pwd'])
            users.insert({'name': request.form['username'], 'user_pwd': hash, 'user_email': request.form['user_email'], 'user_role': request.form['user_role']})

            flash('User has been created')
            return redirect(url_for('login.register'))

        flash('User name already exist')
    return render_template('register_user.html')


@login.route('/signout')
def signout():
    session.clear()
    return redirect('/login')