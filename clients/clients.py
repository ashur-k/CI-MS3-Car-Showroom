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
    other_car_appiontments = mongo.db.client_info.find({'reg_num': request.form['reg_num']})
    #print(other_car_appiontments.count())

    if other_car_appiontments.count() > 0:
        for apt in other_car_appiontments:
            print(apt['full_name'])
            if apt['appiontment_time'] == request.form['appiontment_time'] and apt['appiontment_date'] == request.form['appiontment_date']:
                flash(u'There is already appiontment book on car with same date and time.', 'appiontment')
                print(apt)
                return redirect(url_for('admin.admin_homepage'))
            #if (apt['appiontment_time']) == "" and (apt['appiontment_date']) == "":
                #mongo.db.client_info.update({'_id': ObjectId(request.form['client_id'])}, request.form.to_dict())
                #flash(u'Client appiontment has been made successfully.There are {} appiontments on the car.'.format(other_car_appiontments.count()), 'appiontment')
                #return redirect(url_for('admin.admin_homepage'))
            #else:
        mongo.db.client_info.update({'_id': ObjectId(request.form['client_id'])}, request.form.to_dict())
        flash(u'Client appiontment has been made successfully.There are {} more appiontments on the same car.'.format(other_car_appiontments.count()), 'appiontment')
        return redirect(url_for('admin.admin_homepage'))

    mongo.db.client_info.update({'_id': ObjectId(request.form['client_id'])}, request.form.to_dict())
    flash(u'Appiontment details are successfully updated', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))



@client_blueprint.route('/delete_client/<client_id>', methods=['POST', 'GET'])
def delete_client(client_id):
    print(client_id)
    mongo.db.client_info.remove({'_id': ObjectId(client_id)})

    flash(u'Client is successfully deleted from database.', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))


@client_blueprint.route('/remove_from_dashboard/<client_id>', methods=['POST', 'GET'])
def remove_from_dashboard(client_id):
    #mongo.db.x_clients_records.insert_one(request.form.to_dict())
    #mongo.db.client_info.remove({'_id': ObjectId(client_id)})
    
    mongo.db.client_info.update({"_id": ObjectId(client_id)}, {'$set': {'dashboard_status':'false'}})
    return redirect (url_for('admin.admin_homepage'))


@client_blueprint.route('/move_to_dashboard/<client_id>', methods=['POST', 'GET'])
def move_to_dashboard(client_id):   
    mongo.db.client_info.update({"_id": ObjectId(client_id)}, {'$set': {'dashboard_status':'true'}})
    return redirect (url_for('admin.admin_homepage'))


@client_blueprint.route('/add_new_client', defaults={'reg_num': None})
@client_blueprint.route('/add_new_client/<reg_num>', methods=['POST', 'GET'])
def add_new_client(reg_num):
    
    if reg_num:
        other_appiontments = mongo.db.client_info.find({'reg_num': reg_num})
        car_clients_intrest = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
        return render_template('add_new_client.html', admin_cars_make=mongo.db.car_make.find(), car_clients_intrest=car_clients_intrest, other_appiontments=other_appiontments)

    return render_template('add_new_client.html', admin_cars_make=mongo.db.car_make.find())


@client_blueprint.route('/admin_make_appiontment', methods=['POST', 'GET'])
def admin_make_appiontment():

    other_car_appiontments = mongo.db.client_info.find({'reg_num': request.form['reg_num']})
    appiontment_time = request.form['appiontment_time']
    appiontment_date = request.form['appiontment_date']
    #print(appiontment_time)
    

    if other_car_appiontments.count() > 0:
        for apt in other_car_appiontments:
            #if (apt['appiontment_time']) == "" and (apt['appiontment_date']) == "":
                
                #mongo.db.client_info.insert_one(request.form.to_dict())
                #flash(u'Client appiontment has been made successfully.There are {} appiontments on the car.'.format(other_car_appiontments.count()), 'client_appiontment_message')
                #return redirect(url_for('client_blueprint.add_new_client'))

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
    find_client_name = mongo.db.client_info.find({'full_name': request.form['search']})
    find_client_email = mongo.db.client_info.find({'email': request.form['search']})
    find_client_phone = mongo.db.client_info.find({'phone': request.form['search']})

    if find_client_name.count() > 0:
        client_name = 'with name ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_name, client=client_name)

    elif find_client_email.count() > 0:
        client_email = 'with email ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_email, client=client_email)

    elif find_client_phone.count() > 0:
        client_phone = 'with phone ' + request.form['search']
        return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find(), clients=find_client_phone, client=client_phone)

    return render_template('client_search.html', admin_cars_make=mongo.db.car_make.find())


@client_blueprint.route('/find_reg_num_for_client', methods=['POST', 'GET'])
def find_reg_num_for_client():
    find_registration_num = mongo.db.basic_car_information.find_one({'reg_num': request.form['reg_num']})
    if find_registration_num:
        return redirect(url_for('client_blueprint.add_new_client', reg_num=request.form['reg_num']))

    flash(u'Not find registraion number {}.'.format(request.form['reg_num']), 'client_appiontment_message')
    return redirect(url_for('client_blueprint.add_new_client'))


@client_blueprint.route('/view/<reg_num>/')
def view(reg_num):
    car_info = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
    admin_cars_make = mongo.db.car_make.find()
    return render_template('view_car.html', admin_cars_make=admin_cars_make, car_info=car_info)


@client_blueprint.route('/sold_car_info/<reg_num>/')
def sold_car_info(reg_num):
    car_info = mongo.db.sold_cars.find_one({'reg_num': reg_num})
    admin_cars_make = mongo.db.car_make.find()
    return render_template('sold_car_info.html', admin_cars_make=admin_cars_make, car_info=car_info)