from flask import Flask, jsonify
import numpy as np 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



#Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect = True)
session = Session(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    return (
        f"Welcome to my page! <br/>"
        f"<br/>"
        f"Please go to one of these extensions: <br/>"
        f"<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"       

    )


@app.route("/api/v1.0/precipitation")
def rain():

    raindata = session.query(Measurement.date, Measurement.prcp).all()
    raindata1 = list(np.ravel(raindata))
    print(raindata1)
    print(raindata)
    result = []
    for row in raindata:
        d = {}
        d['date'] = row[0]
        d['rain'] = row[1]
        result.append(d)
    return jsonify(result)
    


@app.route("/api/v1.0/stations")
def stations():

    stations_data = session.query(Station.station).all()
    result = []
    for row in stations_data:
        d = {}
        d['station'] = row[0]
        result.append(d)
    return jsonify(result)


 


@app.route("/api/v1.0/tobs")
def more_rain():
    tobs_data = session.query(Measurement.date, Measurement.tobs).all()
   
    result = []
    for row in tobs_data:
        d = {}
        d['date'] = row[0]
        d['tobs'] = row[1]
        result.append(d)
    return jsonify(result)






# End Flask App

if __name__ == '__main__':
    app.run(debug=True)
