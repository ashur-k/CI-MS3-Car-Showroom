import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for, flash, session, jsonify, json
from database import mongo
from bson.objectid import ObjectId
from login.login import login
from admin.admin import admin
from clients.clients import client_blueprint

app = Flask(__name__)
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(client_blueprint, url_prefix="/client_blueprint")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config["MONGO_DBNAME"] = 'Cars_Sales_Showroom'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo.init_app(app)


# Setting up variables for database collections


cars_model = mongo.db.car_model
basic_car_info = mongo.db.basic_car_information
client_info = mongo.db.client_info


@app.route('/', defaults={'car_make': None, 'car_model': None})
@app.route('/index', defaults={'car_make': None, 'car_model': None})
@app.route('/index/<car_make>/<car_model>', methods=['GET', 'POST'])
@app.route('/index/<car_make>/', defaults={'car_model': None}, methods=['GET', 'POST'])
def index(car_make, car_model):
    random_collections = mongo.db.basic_car_information.aggregate( [ { '$sample': {'size': 3} } ] )

    if car_make:
        if car_model:
            total_car_in_models = mongo.db.basic_car_information.find({'car_model': car_model})
            car_models = cars_model.find({'car_make': car_make})
            return render_template('index.html', cars=mongo.db.car_make.find(), car_models=cars_model.find({'car_make': car_make}), total_car_in_models=total_car_in_models, car_make=car_make, car_model=car_model, random_collections=random_collections)

        total_car_in_make = mongo.db.basic_car_information.find({'car_make': car_make})
        car_models = cars_model.find({'car_make': car_make})
        
        return render_template('index.html' ,cars=mongo.db.car_make.find(), car_models=car_models, total_car_in_make=total_car_in_make, car_make=car_make, random_collections=random_collections)

    all_cars = mongo.db.basic_car_information.find()
    return render_template('index.html', cars=mongo.db.car_make.find(), all_cars=all_cars, random_collections=random_collections)


@app.route('/user_car_view', methods=['POST', 'GET'])
def user_car_view():
    if request.form['car_model']:
    
        availiable_cars_in_model = mongo.db.basic_car_information.find({'car_model': request.form['car_model']})
        return render_template('user_car_view.html', availiable_cars_in_model=availiable_cars_in_model)
    if request.form['car_make']:
        print(request.form['car_make'])
        availiable_cars_in_make = mongo.db.basic_car_information.find({'car_make': request.form['car_make']})
        return render_template('user_car_view.html', availiable_cars_in_make=availiable_cars_in_make)
    return 'code is in development'


@app.route('/book_test_drive/<car_id>', methods=['POST', 'GET'])
def book_test_drive(car_id):
    
    car_info = mongo.db.basic_car_information.find_one({'_id': ObjectId(car_id)})

    return render_template('book_test_drive_form.html', car_info = car_info)


@app.route('/user_book_test_request/<car_id>', methods=['POST', 'GET'])
def user_book_test_request(car_id):
    
    car_info = mongo.db.basic_car_information.find_one({'_id': ObjectId(car_id)})
    mongo.db.client_info.insert_one(request.form.to_dict())
    flash("Thanks {}, we have received your message. Our sales agent will contact you.".format(request.form["full_name"]))
    return render_template('book_test_drive_form.html', car_info = car_info)


@app.route('/user_view_car_specs/<car_id>')
def user_view_car_specs(car_id):
    car_info = mongo.db.basic_car_information.find_one({'_id': ObjectId(car_id)})
    return render_template('user_view_full_car_specs.html', car_info=car_info)


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False
        )
