
import numpy as np
import sqlalchemy
import pandas as pd
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

###### Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

####### Flask Setup
app = Flask(__name__)

####### Flask Routes
@app.route("/")
def welcome():
    """"List all available api routes."""
    return(
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/start_date<br/>"
    f"/api/v1.0/start_date/end_date<br/>"
    )


####### Convert the query results to a Dictionary
# using `date` as the key and `prcp` as the value.
# return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():

    print("Request received for Precipitation Information")
    
    results = session.query(Measurement).filter(Measurement.date >= '2016-08-23').all()
    session.close()

    # Create a dictionary from the row data and append to a list of precipitation_info
    precipitation_info = []
    
    for data in results:
        precipitation_dict = {}
        precipitation_dict[data.date] = data.prcp
        precipitation_info.append(precipitation_dict)

    return jsonify(precipitation_info)


####### Return a list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():

    print("Request received for Station Information")
    
    results = session.query(Station.station).all()
    session.close()
    station_list = list(np.ravel(results))
    
    return jsonify(station_list)

####### query for the dates and temperature observations from 
# a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) 
#  for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():

  print("Request received for Temperature Observations")
  
  results = session.query(Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()
  session.close()
  tobs_list = list(np.ravel(results))
  
  return jsonify(tobs_list)

####### Return a JSON list of the minimum temperature, the average temperature, 
# and the max temperature for a given start date
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` 
# for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>")
def startdate_tobs(start):

    print("Request received for Temperature Observations for all dates greater than and equal to your start date")
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()  
    return jsonify(results)

####### Return a JSON list of the minimum temperature, the average temperature, 
# and the max temperature for the range within a given start date and end date
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` 
# for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end>")
def start_end_tobs(start, end):

    print("Request received for Temperature Observations for the range within your start and end dates")
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
