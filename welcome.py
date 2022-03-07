import datetime as dt
from tkinter import EXCEPTION
import numpy as np
import pandas as pd



import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract

from flask import Flask, jsonify



engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)




print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")


    
# print("Hello top")
app = Flask(__name__)
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/JuneTempurature<br/>"
        f"/api/v1.0/Decembertempurature<br/>"
    )


@app.route("/api/v1.0/JuneTempurature")
def June_temp():
    try:
        june = [dt.date(year, 6, day) for day in range (1, 31) for year in range (2010, 2018)]
        results = []
        results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 6 )
        #result_list=list(results.all())
        #tempJune_df=pd.DataFrame(result_list, columns=['date', 'tobs'])
        #tempJune_df.describe()
        junetemp=list(np.ravel(results))
        return jsonify(junetemp=junetemp)
    except Exception as e:
	    return(str(e))

    

@app.route("/api/v1.0/Decembertempurature")
def Decemeber_temp():
    try:
        december = [dt.date(year, 12, day) for day in range (1, 31) for year in range (2010, 2018)]
        decembers=[]
        decembers = session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date) == 12)
        #decembers_list=list(decembers.all())
        #december_temp_df=pd.DataFrame(decembers_list, columns=['date','tempurature'])
        #december_temp_df.describe()
        temps = list(np.ravel(decembers))
        return jsonify(temps=temps)
    except Exception as e:
	    return(str(e))
    
   
    #


if __name__=="__main__":
    app.run(debug=True)

