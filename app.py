import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecret'

app.config["MONGO_DBNAME"] = 'Cars_Sales_Showroom'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

# Setting up variables for database collections

cars_make = mongo.db.car_make
cars_model = mongo.db.car_model
basic_car_info = mongo.db.basic_car_information


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', cars_make=cars_make.find())


@app.route('/admin')
def admin():
    if 'car_make' in session:
        flash('Registration number {} still neede updating'.format(session['reg_num']), 'reg_num')
        return render_template('admin.html',
                               cars_make=cars_make.find(),
                               car_make=session['car_make'],
                               car_model=session['car_model'],
                               reg_num=session['reg_num'])

    return render_template('admin.html', cars_make=cars_make.find())


@app.route('/add_new_car/<car_make>', methods=['Get', 'POST'])
def add_new_car(car_make):
    if 'car_make' in session:
        flash('Registration number {} still neede updating'.format(session['reg_num']), 'reg_num')
        return render_template('admin.html',
                               cars_make=cars_make.find(),
                               car_make=session['car_make'],
                               car_model=session['car_model'],
                               reg_num=session['reg_num'])

    car_models = cars_model.find({'car_make': car_make})
    if car_models.count() < 1:
        flash(u'Please add models', 'no_model_error')
        return redirect(url_for('add_car_company'))
    return render_template('add_car.html', car_make=car_make, cars_make=cars_make.find(),
                           car_models=car_models)


@app.route('/reg_verification/<car_make>', methods=['POST', 'GET'])
def reg_verification(car_make):
    existing_registration = \
        basic_car_info.find_one({'reg_num': request.form['reg_num']})
    session['car_make'] = car_make
    session['car_model'] = request.form['car_model']
    session['reg_num'] = request.form['reg_num']
    if existing_registration:
        flash('Registration number already exist')
        return redirect(url_for('add_new_car',
                        car_make=session['car_make']))
    else:
        return redirect(url_for('add_car_details',
                        car_make=session['car_make'],
                        car_model=session['car_model'],
                        reg_num=session['reg_num']))


@app.route('/add_car_details/<car_make>/<car_model>/<reg_num>',
           methods=['Get', 'POST'])
def add_car_details(car_make, car_model, reg_num):
    car_makers = cars_make.find_one({'car_make': session['car_make']})
    return render_template('add_new_car.html', car_makers=car_makers,
                           car_model=car_model, reg_num=reg_num,
                           cars_make=cars_make.find())


@app.route('/add_car', methods=['POST', 'GET'])
def add_car():
    existing_registration = \
        basic_car_info.find_one({'reg_num': request.form['reg_num']})
    if existing_registration:
        flash('Car already updated to registration number. {}.'.format(
            request.form['reg_num']))
        return redirect(url_for('add_car_details',
                        car_make=session['car_make'],
                        car_model=session['car_model'],
                        reg_num=session['reg_num']))

    if existing_registration is None:
        add_car = mongo.db.basic_car_information
        add_car.insert_one(request.form.to_dict())
        session.clear()
        flash('Thanks, car added to registration number {}.'.format(
            request.form['reg_num']))
        return redirect(url_for('admin'))


@app.route('/add_car_company')
def add_car_company():
    car_makers = cars_make.find()
    car_make = cars_make.find()
    return render_template('add_new_car_company.html',
                           car_makers=car_makers, car_make=car_make)


@app.route('/add_company', methods=['POST', 'GET'])
def add_company():
    if request.method == 'POST':
        existing_company = \
            cars_make.find_one({'car_make': request.form['car_make']})

        if existing_company is None:
            cars_make.insert_one(request.form.to_dict())
            flash(u'Thanks, {} car make is successfully added.'.format(
                request.form['car_make']), 'make_error')
            return redirect(url_for('add_car_company'))
        flash(u'We already have dealership in database', 'make_error')
    return redirect(url_for('add_car_company'))


@app.route('/add_model', methods=['POST', 'GET'])
def add_model():
    if request.method == 'POST':
        existing_model = \
            cars_model.find_one({'car_model': request.form['car_model']})

        if existing_model is None:
            cars_model.insert_one(request.form.to_dict())
            flash(u'Thanks, {} car model is successfully added.'.format(
                request.form['car_model']), 'model_error')
            return redirect(url_for('add_car_company'))
        flash(u'We already have model in database', 'model_error')
    return redirect(url_for('add_car_company'))


@app.route('/search', methods=['POST', 'GET'])
def search():
    registration_num_search = \
        basic_car_info.find_one({'reg_num': request.form['search']})
    car_make_search = \
        cars_make.find_one({'car_make': request.form['search']})
    car_model_search = \
        cars_model.find_one({'car_model': request.form['search']})

    if registration_num_search:
        return render_template('search.html',
                               results=registration_num_search)
    elif car_make_search:
        available_car_makes = \
            basic_car_info.find({'car_make': request.form['search']})
        if available_car_makes.count() > 0:
            return render_template('make_search.html',
                                   car_make_search=car_make_search,
                                   results=available_car_makes)
        else:
            flash('No cars aviliable in car make.')
            return render_template('make_search.html',
                                   car_make_search=car_make_search,
                                   results=car_make_search)
    elif car_model_search:
        available_car_models = \
            basic_car_info.find({'car_model': request.form['search']})

        if available_car_models.count() > 0:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('model_search.html',
                                   results=available_car_models)
        else:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('model_search.html',
                                   results=available_car_models)
    flash('No results found')
    return redirect(url_for('index'))


@app.route('/update_car_info', methods=['POST', 'GET'])
def update_car_info():
    return render_template('update_car_info.html')


@app.route('/update_options', methods=['POST', 'GET'])
def update_options():
    car_make_results = cars_make.find()
    reg_num = request.form['car_reg_num']
    print(reg_num)
    car_coll = basic_car_info.find_one({'reg_num': reg_num})
    flash(u'Update basic informaiton for registraion number {}.'.format(reg_num), 'update_registration')
    flash(u'Change Car make to change {}.'.format(reg_num), 'update_make_model')
    return render_template('update_car_info.html', car_coll=car_coll, car_make_results=car_make_results)


@app.route('/car_update_page/<car_make>/<coll_id>', methods=['GET', 'POST'])
def car_update_page(car_make, coll_id):
    car_make_results = cars_make.find_one({'car_make': car_make})
    car_model_results = cars_model.find({'car_make': car_make})
    car_coll = basic_car_info.find_one({'_id': ObjectId(coll_id)})
    return render_template('update_car.html', car_make =car_make_results ,car_model_results=car_model_results, car_coll=car_coll)


@app.route('/update_info_db/<car_id>', methods=['POST', 'GET'])
def update_info_db(car_id):
    existing_reg_num = basic_car_info.find_one({'reg_num': request.form['reg_num']})
    print(existing_reg_num)
    print('testing')
    basic_car_info.update({'_id': ObjectId(car_id)}, {
        'car_make': request.form.get('car_make'),
        'car_model': request.form.get('car_model'),
        'reg_num': request.form.get('reg_num'),
        'body_type': request.form.get('body_type'),
        'exterior_colour': request.form.get('exterior_colour'),
        'gear_box': request.form.get('gear_box'),
        'fuel_type': request.form.get('fuel_type'),
        'is_ULEZ_compliant': request.form.get('is_ULEZ_compliant'),
        'warranty_expire_date': request.form.get('warranty_expire_date'),
        'registration_year': request.form.get('registration_year'),
        'mileage': request.form.get('mileage'),
        'transmisson': request.form.get('transmisson'),
        'seats': request.form.get('seats'),
        'drive_type': request.form.get('drive_type'),
        'alloy wheels': request.form.get('alloy wheels'),
        'metallic_paint': request.form.get('metallic_paint'),
        'bluetooth': request.form.get('bluetooth'),
        'climate_control': request.form.get('climate_control'),
        'seats_material': request.form.get('seats_material'),
        'cruise_control': request.form.get('cruise_control'),
        'DAB': request.form.get('DAB'),
        'ISOFIX_fittings': request.form.get('ISOFIX_fittings'),
        'rear_parking_sensors': request.form.get('rear_parking_sensors'),
        'start_stop_technology': request.form.get('start_stop_technology'),
        'top_Speed': request.form.get('top_Speed'),
        'acceleration': request.form.get('acceleration'),
        'engine_power': request.form.get('engine_power'),
        'fuel_tank_capacity': request.form.get('fuel_tank_capacity'),
        'boot_space': request.form.get('boot_space'),
        'length': request.form.get('length'),
        'vehicle_tax': request.form.get('vehicle_tax'),
        'insurance': request.form.get('insurance'),
        'fuel_consumption': request.form.get('fuel_consumption'),

    })
    return '<h1>Update code is under construction</h1>'


@app.route('/update_make_model/<reg_num>', methods=['GET', 'POST'])
def update_make_model(reg_num):
    car_make_results = cars_make.find()
    car_model_results = cars_model.find({'car_make': 'audi'})
    return render_template('edit_car_make_model.html',
                           car_make_results=car_make_results,
                           car_model_results=car_model_results)


@app.route('/update/<car_make>', methods=['POST', 'GET'])
def update(car_make):
    car_make_results = cars_make.find()
    car_model_results = cars_model.find({'car_make': car_make})
    return render_template('edit_car_make_model.html', car_make_results=car_make_results, car_model_results=car_model_results )


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
