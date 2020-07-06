import os
from flask_pymongo import PyMongo
if os.path.exists('env.py'):
    import env


mongo = PyMongo()