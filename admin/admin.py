from flask import app, Blueprint, render_template, redirect, url_for, request, flash, session
from passlib.hash import pbkdf2_sha256
from database import mongo
from bson.objectid import ObjectId


admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


@admin.route('/admin_homepage/<car_add_successfully>')
@admin.route('/admin_homepage', defaults={'car_add_successfully': None})
def admin_homepage(car_add_successfully):
    if 'username' not in session:
        return redirect(url_for('login.admin_login'))

    if 'car_make' in session:
        return admin_carmake_session_package()

    if car_add_successfully:
        return admin_with_login_package(car_add_successfully)

    return admin_with_login_package()


@admin.route('/add_new_car/<car_make>', methods=['Get', 'POST'])
def add_new_car(car_make):
    if 'car_make' in session:
        return admin_carmake_session_package()

    car_models = mongo.db.car_model.find({'car_make': car_make})
    if car_models.count() < 1:
        flash(u'Please add models', 'no_model_error')
        return redirect(url_for('admin.add_car_company'))
    return render_template('add_car.html', car_make=car_make, admin_cars_make=mongo.db.car_make.find(),
                           car_models=car_models)


# admin login with all information admin needs for nav/dashboard
def admin_with_login_package(car_add_successfully=None):
    # print(car_add_successfully)
    # client_info = mongo.db.client_info
    # cars_make = mongo.db.car_make
    # clients_info = mongo.db.client_info.find()
    # find_reg = mongo.db.client_info.find()
    # for reg in find_reg:
        # print(reg['reg_num'])
    if car_add_successfully:
        return render_template('admin.html', admin_cars_make=mongo.db.car_make.find(), clients_info=mongo.db.client_info.find(), car_add_successfully=car_add_successfully)
    return render_template('admin.html', admin_cars_make=mongo.db.car_make.find(), clients_info=mongo.db.client_info.find())


@admin.route('/reg_verification/<car_make>', methods=['POST', 'GET'])
def reg_verification(car_make):
    existing_registration = \
        mongo.db.basic_car_information.find_one({'reg_num': request.form['reg_num']})
    if existing_registration:
        flash(u'Registration number already exist', 'error')
        return redirect(url_for('admin.add_new_car',
                        car_make=car_make))
    else:
        session['car_make'] = car_make
        session['car_model'] = request.form['car_model']
        session['reg_num'] = request.form['reg_num']
        return redirect(url_for('admin.add_car_details',
                        car_make=session['car_make'],
                        car_model=session['car_model'],
                        reg_num=session['reg_num']))


@admin.route('/add_car_details/<car_make>/<car_model>/<reg_num>',
           methods=['Get', 'POST'])
def add_car_details(car_make, car_model, reg_num):
    car_makers = mongo.db.car_make.find_one({'car_make': session['car_make']})
    return render_template('add_new_car.html', car_makers=car_makers,
                           car_model=car_model, reg_num=reg_num,
                           admin_cars_make=mongo.db.car_make.find())


@admin.route('/add_car', methods=['POST', 'GET'])
def add_car():
    existing_registration = \
        mongo.db.basic_car_information.find_one({'reg_num': request.form['reg_num']})
    if existing_registration:
        flash('Car already updated to registration number. {}.'.format(
            request.form['reg_num']))
        return redirect(url_for('admin.add_car_details',
                        car_make=session['car_make'],
                        car_model=session['car_model'],
                        reg_num=session['reg_num'])) #this registration number is conflicitng with car update registraion number

    if existing_registration is None:
        add_car = mongo.db.basic_car_information
        add_car.insert_one(request.form.to_dict())
        session.pop('car_make', None)
        session.pop('car_model', None)
        session.pop('reg_num', None)
        flash('Thanks, car added to registration number {}.'.format(
            request.form['reg_num']))
        car_add_successfully = "Thanks, car registration number " + request.form['reg_num'] + " is added successfully to database" 
        return redirect(url_for('admin.admin_homepage', car_add_successfully=car_add_successfully ))


@admin.route('/add_car_company')
def add_car_company():
    car_makers = mongo.db.car_make.find()
    car_make = mongo.db.car_make.find()
    return render_template('add_new_car_company.html', admin_cars_make=mongo.db.car_make.find(),
                           car_makers=car_makers, car_make=car_make)


@admin.route('/add_company', methods=['POST', 'GET'])
def add_company():
    if request.method == 'POST':
        existing_company = \
            mongo.db.car_make.find_one({'car_make': request.form['car_make']})

        if existing_company is None:
            mongo.db.car_make.insert_one(request.form.to_dict())
            flash(u'Thanks, {} car make is successfully added.'.format(
                request.form['car_make']), 'make_error')
            return redirect(url_for('admin.add_car_company'))
        flash(u'We already have dealership in database', 'make_error')
    return redirect(url_for('admin.add_car_company'))


@admin.route('/add_model', methods=['POST', 'GET'])
def add_model():
    if request.method == 'POST':
        existing_model = \
            mongo.db.car_model.find_one({'car_model': request.form['car_model']})

        if existing_model is None:
            mongo.db.car_model.insert_one(request.form.to_dict())
            flash(u'Thanks, {} car model is successfully added.'.format(
                request.form['car_model']), 'model_error')
            return redirect(url_for('admin.add_company'))

    flash(u'We already have model in database', 'model_error')
    return redirect(url_for('admin.add_company'))


@admin.route('/search', methods=['POST', 'GET'])
def search():
    # cars_make = mongo.db.car_make
    # cars_model = mongo.db.car_model
    # client_info = mongo.db.client_info

    registration_num_search = \
        mongo.db.basic_car_information.find_one({'reg_num': request.form['search']})

    sold_car_search = \
        mongo.db.sold_cars.find_one({'reg_num': request.form['search']})

    car_make_search = \
        mongo.db.car_make.find_one({'car_make': request.form['search']})

    car_model_search = \
        mongo.db.car_model.find_one({'car_model': request.form['search']})

    if registration_num_search:
        return render_template('search.html',
                               reg_results=registration_num_search, admin_cars_make=mongo.db.car_make.find())
    elif sold_car_search:
        return redirect (url_for('client_blueprint.sold_car_info', reg_num=request.form['search']))
    elif car_make_search:
        available_car_makes = \
            mongo.db.basic_car_information.find({'car_make': request.form['search']})
        if available_car_makes.count() > 0:
            return render_template('search.html',
                                    admin_cars_make=mongo.db.car_make.find(),
                                   car_make_search=car_make_search,
                                   car_make_results=available_car_makes)
        else:
            flash('No results found in car make')
            return render_template('search.html', 
                                admin_cars_make=mongo.db.car_make.find(),
                                   car_make_search=car_make_search)
    elif car_model_search:
        available_car_models = \
            mongo.db.basic_car_information.find({'car_model': request.form['search']})

        if available_car_models.count() > 0:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('search.html', admin_cars_make=mongo.db.car_make.find(),
                                    car_model_search=car_model_search,
                                   model_results=available_car_models)
        else:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('search.html', admin_cars_make=mongo.db.car_make.find(),
                                   car_model_search=car_model_search)
    
    return render_template('search.html', admin_cars_make=mongo.db.car_make.find())


@admin.route('/update_car_info', methods=['POST', 'GET'])
def update_car_info():
    return render_template('update_car_info.html', admin_cars_make=mongo.db.car_make.find())


# using doubel route to finsish if reg_num session if in session
# if request is coming from update car info search template
@admin.route('/update_options', methods=['POST', 'GET'], defaults={'registration_number': None})
@admin.route('/update_options/<registration_number>', methods=['POST', 'GET'])
def update_options(registration_number):
    # ending session if request is generated from update_car_info.html template
    if registration_number:
        if 'old_reg_num' and 'new_reg_num' in session: #change to old_reg_num here
            session.pop('old_reg_num', None) #change to old_reg_num here
            session.pop('new_reg_num', None)

    if 'old_reg_num' in session: # change to old_reg_num here
        new_reg_num = session['new_reg_num']
        car_make_results = mongo.db.car_make.find()
        car_coll = mongo.db.basic_car_information.find_one({'reg_num': session['old_reg_num']}) # change to old_reg_num here
        return render_template('starter_car_edit.html', car_coll=car_coll, car_make_results=car_make_results, new_reg_num=new_reg_num, admin_cars_make=mongo.db.car_make.find())

    reg_num = request.form['reg_num']

    car_coll = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
    if car_coll:
        car_make_results = mongo.db.car_make.find()
        return render_template('starter_car_edit.html', car_coll=car_coll, car_make_results=car_make_results, admin_cars_make=mongo.db.car_make.find())
    else:
        flash('Sorry, There is no car in database with this registration number {}.'.format(reg_num))
        return redirect(url_for('admin.update_car_info'))


@admin.route('/car_update_page', methods=['GET', 'POST'])
def car_update_page():
    old_reg_num = request.form['old_reg_num']
    new_reg_num = request.form['reg_num']

    car_make = request.form['car_make']
    session['old_reg_num'] = old_reg_num # this is registration number which is conflicting #changing name to old_reg_num
    session['new_reg_num'] = new_reg_num

    if new_reg_num != old_reg_num:
        existing_registration = mongo.db.basic_car_information.find_one({'reg_num': request.form['reg_num']})
        if existing_registration:
            flash('{} registraion number is already in database.'.format(new_reg_num))
            return redirect(url_for('admin.update_options'))

    car_make = request.form['car_make']
    coll_Id = request.form['hiddenCarId']
    car_make_results = mongo.db.car_make.find_one({'car_make': car_make})
    car_model_results = mongo.db.car_model.find({'car_make': car_make})
    car_coll = mongo.db.basic_car_information.find_one({'_id': ObjectId(coll_Id)})
    # session.pop('reg_num', None)
    # session.pop('new_reg_num', None)
    return render_template('update_car.html', car_make =car_make_results ,car_model_results=car_model_results, car_coll=car_coll, new_reg_num=new_reg_num,admin_cars_make=mongo.db.car_make.find())


@admin.route('/update_info_db/<car_id>', methods=['POST', 'GET'])
def update_info_db(car_id):
    # session.clear()
    if session['old_reg_num'] != session['new_reg_num']: #change to old_reg_num here
        clients_who_requested_same_this_car = mongo.db.client_info.find({'reg_num': session['reg_num']})
        print (clients_who_requested_same_this_car)
        mongo.db.client_info.update_many({"reg_num": session['reg_num'] }, {'$set': {'reg_num':session['new_reg_num']}})

    mongo.db.basic_car_information.update({'_id': ObjectId(car_id)},
                          request.form.to_dict())
    session.pop('old_reg_num', None) #change to old_reg_num here
    session.pop('new_reg_num', None)
    flash('Car details are successfully updated to registration number {}.'.format(request.form['reg_num']))
    return redirect(url_for('admin.update_car_info'))


@admin.route('/delete_car/<car_id>/<reg_num>', methods=['POST', 'GET'])
def delete_car(car_id, reg_num):
    mongo.db.basic_car_information.remove({'_id': ObjectId(car_id)})
    #session.clear()
    flash('{} Registraion number is deleted succesfully'.format(reg_num))
    return redirect(url_for('admin.update_car_info'))


@admin.route('/view/<car_id>/')
def view(car_id):
    car_info = mongo.db.basic_car_information.find_one({'_id': ObjectId(car_id)})
    admin_cars_make = mongo.db.car_make.find()
    return render_template('view_car.html', admin_cars_make=admin_cars_make, car_info=car_info)


def admin_carmake_session_package():
    flash('Registration number {} still needed updating'.format(session['reg_num']), 'reg_num')
    return render_template('admin.html', admin_cars_make=mongo.db.car_make.find(),
                           car_make=session['car_make'],
                           car_model=session['car_model'],
                           reg_num=session['reg_num'])


@admin.route('/end_car_reg_session')
def end_car_reg_session():
    session.pop('car_make', None)
    session.pop('car_model', None)
    session.pop('reg_num', None)
    return redirect(url_for('admin.admin_homepage'))


@admin.route('/finish_car_registration')
def finish_car_registration():
    return redirect(url_for('admin.add_car_details',
                        car_make=session['car_make'],
                        car_model=session['car_model'],
                        reg_num=session['reg_num']))


@admin.route('/add_new_client/<reg_num>', defaults={'client_id': None})
@admin.route('/car_sold_form/<reg_num>/<client_id>', methods=['POST', 'GET'])
def car_sold_form(reg_num, client_id):
    sold_car = mongo.db.basic_car_information.find_one({'reg_num': reg_num})
    client_info = mongo.db.client_info.find_one({'_id': ObjectId(client_id)})
    
    return render_template('car_sold_form.html', admin_cars_make=mongo.db.car_make.find(), sold_car=sold_car, client_info=client_info)


@admin.route('/car_sold/<car_id>', methods=['POST', 'GET'])
def car_sold(car_id):

    registraion_number = request.form['reg_num']
    print(registraion_number)
    add_car_sold_info_to_client_db = mongo.db.client_info.find({'reg_num': request.form['reg_num']})
    
    if add_car_sold_info_to_client_db.count() > 0:
        mongo.db.client_info.update_many({"reg_num": request.form['reg_num'] }, {'$set': {'car_status':'car_is_sold'}})


    #mongo.db.basic_car_information.update({'_id': ObjectId(car_id)}, request.form.to_dict())
    # mongo.db.basic_car_information.remove({'_id': ObjectId(car_id)})
    mongo.db.sold_cars.insert_one(request.form.to_dict())
    mongo.db.basic_car_information.remove({'_id': ObjectId(car_id)})
    flash(u'Information is succesfully added to sold car datebase.', 'car_sold')
    return redirect(url_for('admin.admin_homepage'))


@admin.route('/delete_client_admin_url/<client_id>', methods=['POST', 'GET'])
def delete_client_admin_url(client_id):
    print(client_id)
    mongo.db.client_info.remove({'_id': ObjectId(client_id)})

    flash(u'Client is successfully deleted from database.', 'appiontment')
    return redirect(url_for('admin.admin_homepage'))