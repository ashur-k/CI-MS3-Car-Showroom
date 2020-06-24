import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for, flash
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
cars_specs = mongo.db.car_specs_perfomance_economy
cars_summary = mongo.db.car_summary
cars_info = mongo.db.cars
cars_running_cost = mongo.db.running_cost
cars_features = mongo.db.car_features


@app.route('/', methods=['GET', 'POST'])
def index():
    car_features = cars_features.find()
    return render_template('index.html',  cars_make=cars_make.find(), car_features = car_features)


@app.route('/add_new_car')
def add_new_car():
    car_makers = cars_make.find()
    car_models = cars_model.find()
    return render_template('add_new_car.html', car_makers=car_makers, car_models=car_models)


@app.route('/add_car', methods=['POST'])
def add_car():
    add_car = mongo.db.basic_car_information
    add_car.insert_one(request.form.to_dict())
    flash("Thanks, new car added to registration number {}.".format(
        request.form["reg_num"]))

    return redirect(url_for("add_new_car"))


@app.route('/add_car_company')
def add_car_company():
    car_makers = cars_make.find()
    return render_template('add_new_car_company.html', car_makers=car_makers)


@app.route('/add_company', methods=['POST', 'GET'])
def add_company():
    if request.method == 'POST':
        existing_company = cars_make.find_one({'car_make': request.form['car_make']})

        if existing_company is None:
            cars_make.insert_one(request.form.to_dict())
            flash(u"Thanks, {} car make is successfully added to cars sales showroom database.".format(request.form["car_make"]), 'make_error')
            return redirect(url_for("add_car_company"))
        flash(u'We already have dealership in database', 'make_error')
    return redirect(url_for('add_car_company'))


@app.route('/add_model', methods=['POST', 'GET'])
def add_model():
    if request.method == 'POST':
        existing_model = cars_model.find_one({'car_model': request.form['car_model']})

        if existing_model is None:
            cars_model.insert_one(request.form.to_dict())
            flash(u"Thanks, {} car model is successfully added to cars sales showroom database.".format(request.form["car_model"]), 'model_error')
            return redirect(url_for("add_car_company"))
        flash(u'We already have model in database', 'model_error')
    return redirect(url_for('add_car_company'))


@app.route('/view_car/<car_registration>')
def view_car(car_registration):
    
    return render_template('view_car.html', )


def helper_function():
    car_makers = cars_make.find()
    for makers in car_makers:
        print(makers.car_make)



if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
