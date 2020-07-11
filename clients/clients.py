from flask import app, Blueprint, render_template, redirect, url_for, request, flash, session
from passlib.hash import pbkdf2_sha256
from database import mongo
from bson.objectid import ObjectId

client_blueprint = Blueprint("client_blueprint", __name__, static_folder="static", template_folder="templates")


@client_blueprint.route('/')
@client_blueprint.route('/clients/<client_id>')
def clients(client_id):
    client_info = mongo.db.client_info.find_one({'_id': ObjectId(client_id)})

    return render_template('clients.html', admin_cars_make=mongo.db.car_make.find(), client_info=client_info)


@client_blueprint.route('/add_appiontments_records', methods=['POST', 'GET'])
def add_appiontments_records():
    existing_bookings = \
        mongo.db.appiontments_records.find_one({'client_id': request.form['client_id']})
    if existing_bookings:
        client_id = request.form['client_id']
        flash(u'Appiontment with this client has already been made.', 'appiontment')
        return redirect(url_for('admin.admin_homepage'))
    mongo.db.appiontments_records.insert_one(request.form.to_dict())
    flash(u'Appiontment details are successfully updated', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))



@client_blueprint.route('/delete_client/<client_id>', methods=['POST', 'GET'])
def delete_client(client_id):
    print(client_id)
    mongo.db.client_info.remove({'_id': ObjectId(client_id)})

    flash(u'Client is successfully deleted from database.', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))


@client_blueprint.route('/test', methods=['POST', 'GET'])
def test():
    client_info = mongo.db.client_info.find()
    return render_template('test.html', client_info = client_info)