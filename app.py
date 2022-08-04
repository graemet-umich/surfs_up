# The Flask Weather App

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create the session link
session = Session(engine)

# define Flask app
app = Flask(__name__)




# # create new flask instance
# app = Flask(__name__)

# #create root starting point
# @app.route('/')
# def index():
#     return 'index'

# @app.route('/hello')
# def hello_world():
#     return 'Hello world'

# @app.route('/hard_fib')
# def hard_fib():
#     return '[0,1,1,2,3,5,8,13]'
