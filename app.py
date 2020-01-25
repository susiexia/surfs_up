

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
    results = session.query(station.station).all()
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days= 365)
    results = session.query(measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= prev_year).all()
    temp = list(np.ravel(results))

    return jsonify(temp)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs),\
        func.max(measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(measurement.date>=start).\
        filter(measurement.date<=end).all()
    
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(measurement.date>=start).\
    filter(measurement.date<=end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# check which destination execute app.py 
print("example __name__ = %s", __name__)
if __name__ == "__main__":
    print("example is being run directly.")
    app.run()
else:
    print("example is being imported")