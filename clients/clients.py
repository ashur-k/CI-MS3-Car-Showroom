from flask import app, Blueprint, render_template, redirect, url_for, request, flash, session
from passlib.hash import pbkdf2_sha256
from database import mongo
from bson.objectid import ObjectId

client_blueprint = Blueprint("client_blueprint", __name__, static_folder="static", template_folder="templates")


@client_blueprint.route('/')
@client_blueprint.route('/clients/<client_id>')
def clients(client_id):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    client_info = mongo.db.client_info.find_one({'_id': ObjectId(client_id)})

    return render_template('clients.html', admin_cars_make=mongo.db.car_make.find(), client_info=client_info)


@client_blueprint.route('/add_appiontments_records', methods=['POST', 'GET'])
def add_appiontments_records():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    other_car_appiontments = mongo.db.client_info.find({'reg_num': request.form['reg_num']})
    

    if other_car_appiontments.count() > 0:
        for apt in other_car_appiontments:
            print(apt['full_name'])
            if apt['appiontment_time'] == request.form['appiontment_time'] and apt['appiontment_date'] == request.form['appiontment_date']:
                flash(u'There is already an appiontment booked on car with same date and time.', 'appiontment')
                print(apt)
                return redirect(url_for('admin.admin_homepage'))
            
        mongo.db.client_info.update({'_id': ObjectId(request.form['client_id'])}, request.form.to_dict())
        flash(u'Client appiontment has been made successfully.{} appiontments on the same car.'.format(other_car_appiontments.count()), 'appiontment')
        return redirect(url_for('admin.admin_homepage'))

    mongo.db.client_info.update({'_id': ObjectId(request.form['client_id'])}, request.form.to_dict())
    flash(u'Appiontment details are successfully updated', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))


@client_blueprint.route('/delete_client/<client_id>', methods=['POST', 'GET'])
def delete_client(client_id):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    print(client_id)
    mongo.db.client_info.remove({'_id': ObjectId(client_id)})

    flash(u'Client is successfully deleted from database.', 'client_deleted')
    return redirect(url_for('client_blueprint.view_all_clients'))


@client_blueprint.route('/remove_from_dashboard/<client_id>', methods=['POST', 'GET'])
def remove_from_dashboard(client_id):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    
    
    mongo.db.client_info.update({"_id": ObjectId(client_id)}, {'$set': {'dashboard_status':'false'}})
    return redirect (url_for('admin.admin_homepage'))


@client_blueprint.route('/move_to_dashboard/<client_id>', methods=['POST', 'GET'])
def move_to_dashboard(client_id): 
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))  
    mongo.db.client_info.update({"_id": ObjectId(client_id)}, {'$set': {'dashboard_status':'true'}})
    return redirect (url_for('client_blueprint.view_all_clients'))


@client_blueprint.route('/add_new_client', defaults={'reg_num': None})
@client_blueprint.route('/add_new_client/<reg_num>', methods=['POST', 'GET'])
def add_new_client(reg_num):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    
    if reg_num:
        other_appiontments = mongo.db.client_info.find({'reg_num': reg_num})
        car_clients_intrest = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
        return render_template('add_new_client.html', admin_cars_make=mongo.db.car_make.find(), car_clients_intrest=car_clients_intrest, other_appiontments=other_appiontments)

    return render_template('add_new_client.html', admin_cars_make=mongo.db.car_make.find())


@client_blueprint.route('/admin_make_appiontment', methods=['POST', 'GET'])
def admin_make_appiontment():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))

    other_car_appiontments = mongo.db.client_info.find({'reg_num': request.form['reg_num']})
    appiontment_time = request.form['appiontment_time']
    appiontment_date = request.form['appiontment_date']
    
    

    if other_car_appiontments.count() > 0:
        for apt in other_car_appiontments:

            if apt['appiontment_time'] == appiontment_time and apt['appiontment_date'] == appiontment_date:
                flash(u'there is already appiontment book on car with same date and time.', 'client_appiontment_message')
                return redirect(url_for('client_blueprint.add_new_client', reg_num=request.form['reg_num']))

        mongo.db.client_info.insert_one(request.form.to_dict())
        flash(u'Client appiontment has been made successfully.There are {} appiontments on the car.'.format(other_car_appiontments.count()), 'client_appiontment_message')
        return redirect(url_for('client_blueprint.add_new_client'))
        

    mongo.db.client_info.insert_one(request.form.to_dict())
    flash(u'Client appiontment has been made successfully.', 'client_appiontment_message')
    return redirect(url_for('client_blueprint.add_new_client'))


@client_blueprint.route('/client_search', methods=['POST', 'GET'])
def client_search():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    find_client_name = mongo.db.client_info.find({'full_name': request.form['search']})
    find_client_email = mongo.db.client_info.find({'email': request.form['search']})
    find_client_phone = mongo.db.client_info.find({'phone': request.form['search']})
    find_client_from_car_registration = mongo.db.client_info.find({'reg_num': request.form['search']})

    if find_client_name.count() > 0:
        client_name = 'with name ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_name, client=client_name)

    elif find_client_email.count() > 0:
        client_email = 'with email ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_email, client=client_email)

    elif find_client_phone.count() > 0:
        client_phone = 'with phone ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_phone, client=client_phone)
    
    elif find_client_from_car_registration.count() > 0:
        car_reg = 'with car registration ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_from_car_registration, client=car_reg)

    return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find())


@client_blueprint.route('/find_reg_num_for_client', methods=['POST', 'GET'])
def find_reg_num_for_client():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    find_registration_num = mongo.db.basic_car_information.find_one({'reg_num': request.form['reg_num']})
    if find_registration_num:
        return redirect(url_for('client_blueprint.add_new_client', reg_num=request.form['reg_num']))

    flash(u'Not find registraion number {}.'.format(request.form['reg_num']), 'client_appiontment_message')
    return redirect(url_for('client_blueprint.add_new_client'))


@client_blueprint.route('/view/<reg_num>/')
def view(reg_num):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    car_info = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
    if car_info:
        return render_template('view_car.html', admin_cars_make=mongo.db.car_make.find(), car_info=car_info)
    
    flash(u'Admin has removed car information from cars database.', 'appiontment')   
    return redirect(url_for('admin.admin_homepage'))



@client_blueprint.route('/sold_cars/')
def sold_cars():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    sold_cars = mongo.db.sold_cars.find()
    admin_cars_make = mongo.db.car_make.find()
    return render_template('sold_cars.html', admin_cars_make=admin_cars_make, sold_cars=sold_cars)


@client_blueprint.route('/sold_car_info/<reg_num>/')
def sold_car_info(reg_num):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))

    car_info = mongo.db.sold_cars.find_one({'reg_num': reg_num})
    if car_info:
        admin_cars_make = mongo.db.car_make.find()
        return render_template('sold_car_info.html', admin_cars_make=admin_cars_make, car_info=car_info)

    flash(u'Admin has removed client and car information from database.', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))

@client_blueprint.route('/delete_sold_car/<car_id>', methods=['POST', 'GET'])
def delete_sold_car(car_id):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))

    mongo.db.sold_cars.remove({'_id': ObjectId(car_id)})
    flash(u'Car and client inforamtion is successfully deleted from database.', 'delete_flash')
    return redirect(url_for('client_blueprint.sold_cars'))


@client_blueprint.route('/view_all_clients')
def view_all_clients():
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))
    client_info = mongo.db.client_info.find()
    admin_cars_make = mongo.db.car_make.find()
    return render_template('view_clients.html', admin_cars_make=admin_cars_make, clients_info=client_info)