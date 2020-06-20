import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html', cars=cars_info.find())


@app.route('/trial')
def trial():
    return render_template('trial.html', cars=cars_summary.find())


@app.route('/view_car/<car_registration>')
def view_car(car_registration):
    car_info = cars_info.find({'registration_number': car_registration})
    c_summary = cars_summary.find({'registration_number': car_registration})
    return render_template('view_car.html', cars=car_info, summary=c_summary)


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
