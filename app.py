

import datetime as dt  
import pandas as pd  
import numpy as np  
# sqlalchemy to connect with DB
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# flask module
from flask import Flask, jsonify


# set up the DB
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect= True)

measurement = Base.classes.measurement
station = Base.classes.station

session =  Session(engine)
# set up flask app
app = Flask(__name__)

# check which destination execute app.py 
print("example __name__ = %s", __name__)
if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

    
@app.route('/')
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days= 365)
    precipitation = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date>= prev_year).all()
    precip_js = {date: prcp for date, prcp in precipitation}

    return jsonify(precip_js)

@app.route('/api/v1.0/stations')
def stations():
    


app.run()