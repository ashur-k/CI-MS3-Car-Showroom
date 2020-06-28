import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo


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
    return render_template('admin.html', cars_make=cars_make.find())


@app.route('/add_new_car/<car_make>', methods=['Get', 'POST'])
def add_new_car(car_make):
    session['car_make'] = car_make
    car_models = cars_model.find({'car_make': car_make})
    return render_template('add_car.html', cars_make=cars_make.find(), car_models=car_models)


@app.route('/add_car_details/<car_model>/<reg_num>', methods=['Get', 'POST'])
def add_car_details(car_model, reg_num):
    print(car_model)
    car_makers = cars_make.find_one({'car_make': session['car_make']})
    
    return render_template('add_new_car.html', car_makers=car_makers, car_model=car_model, reg_num=reg_num, cars_make=cars_make.find())


@app.route('/reg_verification', methods=['POST', 'GET'])
def reg_verification():
    existing_registration = \
        basic_car_info.find_one({'reg_num': request.form['reg_num']})
    if existing_registration:
        flash('Registration number already exist')
        return redirect(url_for('add_new_car', car_make=session['car_make']))
    else:
        reg_num = request.form['reg_num']
        car_model = request.form['car_model']
        print(reg_num)
        print(car_model)
        return redirect(url_for('add_car_details', car_model=car_model, reg_num=reg_num))


@app.route('/add_car', methods=['POST', 'GET'])
def add_car():
    existing_registration = \
        basic_car_info.find_one({'reg_num': request.form['reg_num']})
    if existing_registration:
        car_make = session['car_make']
        flash('Sorry, registation num already existed. {}.'.format(
            request.form['reg_num']))
        return redirect(url_for('add_car_details', car_make=car_make))

    if existing_registration is None:
        add_car = mongo.db.basic_car_information
        add_car.insert_one(request.form.to_dict())
        flash('Thanks, car added to registration number {}.'.format(
            request.form['reg_num']))
    return redirect(url_for('add_new_car', car_make=session['car_make']))


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

    return '<h1>No reults found</h1>'


@app.route('/trial/<car_make>', methods=['GET', 'POST'])
@app.route('/trial')
def trial(car_make):
    car_make_results = cars_make.find()
    car_model_results = cars_model.find({'car_make': car_make})
    return render_template('add_car.html',
                           car_make_results=car_make_results,
                           car_model_results=car_model_results)


@app.route('/temp_route', methods=['POST', 'GET'])
def temp_route():
    cars_model.insert_one(request.form.to_dict())
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
