import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for, flash, session, jsonify, json
from database import mongo
from bson.objectid import ObjectId
from admin.login import login

app = Flask(__name__)
app.register_blueprint(login, url_prefix="/login")

app.config['SECRET_KEY'] = 'mySecret'

app.config["MONGO_DBNAME"] = 'Cars_Sales_Showroom'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo.init_app(app)


# Setting up variables for database collections

cars_make = mongo.db.car_make
cars_model = mongo.db.car_model
basic_car_info = mongo.db.basic_car_information


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/admin/')
def admin():
    if 'car_make' in session:
        flash('Registration number {} still neede updating'.format(session['reg_num']), 'reg_num')
        return render_template('admin.html',
                               admin_cars_make=cars_make.find(),
                               car_make=session['car_make'],
                               car_model=session['car_model'],
                               reg_num=session['reg_num'])

    return render_template('admin.html', admin_cars_make=cars_make.find())


@app.route('/add_new_car/<car_make>', methods=['Get', 'POST'])
def add_new_car(car_make):
    if 'car_make' in session:
        flash('Registration number {} still neede updating'.format(session['reg_num']), 'reg_num')
        return render_template('admin.html',
                               admin_cars_make=cars_make.find(),
                               car_make=session['car_make'],
                               car_model=session['car_model'],
                               reg_num=session['reg_num'])

    car_models = cars_model.find({'car_make': car_make})
    if car_models.count() < 1:
        flash(u'Please add models', 'no_model_error')
        return redirect(url_for('add_car_company'))
    return render_template('add_car.html', car_make=car_make, admin_cars_make=cars_make.find(),
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
                           admin_cars_make=cars_make.find())


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
    return render_template('add_new_car_company.html', admin_cars_make=cars_make.find(),
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
            return redirect(url_for('add_new_car', car_make=request.form['car_make']))
        flash(u'We already have model in database', 'model_error')
    return redirect(url_for('add_new_car'))


@app.route('/search', methods=['POST', 'GET'])
def search():
    registration_num_search = \
        basic_car_info.find_one({'reg_num': request.form['search']})
    car_make_search = \
        cars_make.find_one({'car_make': request.form['search']})
    car_model_search = \
        cars_model.find_one({'car_model': request.form['search']})

    if registration_num_search:
        return render_template('make_search.html',
                               reg_results=registration_num_search)
    elif car_make_search:
        available_car_makes = \
            basic_car_info.find({'car_make': request.form['search']})
        if available_car_makes.count() > 0:
            return render_template('make_search.html',
                                    admin_cars_make=cars_make.find(),
                                   car_make_search=car_make_search,
                                   car_make_results=available_car_makes)
        else:
            flash('No results found in car make')
            return render_template('make_search.html', 
                                admin_cars_make=cars_make.find(),
                                   car_make_search=car_make_search)
    elif car_model_search:
        available_car_models = \
            basic_car_info.find({'car_model': request.form['search']})

        if available_car_models.count() > 0:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('make_search.html', admin_cars_make=cars_make.find(),
                                    car_model_search=car_model_search,
                                   model_results=available_car_models)
        else:
            flash('{} Results found in {}.'.format(
                available_car_models.count(),
                  request.form['search']))
            return render_template('make_search.html', admin_cars_make=cars_make.find(),
                                   car_model_search=car_model_search)
    
    return render_template('make_search.html', admin_cars_make=cars_make.find())


@app.route('/update_car_info', methods=['POST', 'GET'])
def update_car_info():
    return render_template('update_car_info.html', admin_cars_make=cars_make.find())


@app.route('/update_options', methods=['POST', 'GET'])
def update_options():
    if 'reg_num' in session:
        new_reg_num = session['new_reg_num']
        car_make_results = cars_make.find()
        car_coll = basic_car_info.find_one({'reg_num': session['reg_num']})
        return render_template('starter_car_edit.html', car_coll=car_coll, car_make_results=car_make_results, new_reg_num=new_reg_num, admin_cars_make=cars_make.find())

    reg_num = request.form['reg_num']

    car_coll = basic_car_info.find_one({'reg_num': reg_num})
    if car_coll:
        car_make_results = cars_make.find()
        return render_template('starter_car_edit.html', car_coll=car_coll, car_make_results=car_make_results, admin_cars_make=cars_make.find())
    else:
        flash('Sorry, There is no car in database with this registration number {}.'.format(reg_num))
        return redirect(url_for('update_car_info'))


@app.route('/car_update_page', methods=['GET', 'POST'])
def car_update_page():
    old_reg_num = request.form['old_reg_num']
    new_reg_num = request.form['reg_num']
    car_make = request.form['car_make']
    session['reg_num'] = old_reg_num
    session['new_reg_num'] = new_reg_num

    if new_reg_num != old_reg_num:
        existing_registration = \
        basic_car_info.find_one({'reg_num': new_reg_num})
        if existing_registration:
            flash('{} registraion number is already in database.'.format(new_reg_num))
            return redirect(url_for('update_options'))

    car_make = request.form['car_make']
    coll_Id = request.form['hiddenCarId']
    car_make_results = cars_make.find_one({'car_make': car_make})
    car_model_results = cars_model.find({'car_make': car_make})
    car_coll = basic_car_info.find_one({'_id': ObjectId(coll_Id)})
    session.clear()
    return render_template('update_car.html', car_make =car_make_results ,car_model_results=car_model_results, car_coll=car_coll, new_reg_num=new_reg_num)


@app.route('/update_info_db/<car_id>', methods=['POST', 'GET'])
def update_info_db(car_id):
    session.clear()

    basic_car_info.update({'_id': ObjectId(car_id)},
                          request.form.to_dict())
    flash('Car details are successfully updated to registration number {}.'.format(request.form['reg_num']))
    return redirect(url_for('update_car_info'))


@app.route('/delete_car/<car_id>/<reg_num>', methods=['POST', 'GET'])
def delete_car(car_id, reg_num):
    basic_car_info.remove({'_id': ObjectId(car_id)})
    session.clear()
    flash('{} Registraion number is deleted succesfully'.format(reg_num))
    return redirect(url_for('update_car_info'))


@app.route('/view/<car_id>/')
def view(car_id):
    car_info = basic_car_info.find_one({'_id': ObjectId(car_id)})
    return render_template('view_car.html', admin_cars_make=cars_make.find(), car_info=car_info)


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
