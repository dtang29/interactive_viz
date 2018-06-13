# import necessary libraries
import os
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import String
from sqlalchemy import cast, func, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

##############
# Flask set up
##############
app = Flask(__name__)

################
# Database Setup
################

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Otu = Base.classes.otu
Samples = Base.classes.samples
SamplesMeta = Base.classes.samples_metadata

# Create our session (link) from Python to the DB
session = Session(engine)

##################
#Configure endpoints
##################

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/names")
def bellybutton_name():

    #Write a query to filter out all sample ids with BB_ concated to it and return a list
    results = session.query("BB_" + cast(SamplesMeta.SAMPLEID, String)).all()

    all_sampleids = list(np.ravel(results))

    return jsonify(all_sampleids)

@app.route('/otu')
def bellybutton_otu():

    #Write a query to list all otu descriptions from the otu table 
    results = session.query(Otu.lowest_taxonomic_unit_found).all()

    all_otu = list(np.ravel(results))

    return jsonify(all_otu)


@app.route('/metadata/<sample>')
def bellybutton_metadata_sample(sample):

    #grab all the columns we need and create a list
    sel = [SamplesMeta.AGE,
        SamplesMeta.BBTYPE,
        SamplesMeta.ETHNICITY,
        SamplesMeta.GENDER,
        SamplesMeta.LOCATION,
        SamplesMeta.SAMPLEID]

    #Query the above columns for the sample id provided by user
    results = session.query(*sel).\
                filter(SamplesMeta.SAMPLEID == sample).all()
    print(results)

    #Create an empty list to store a dictionary
    all_samples = []

    #Create a dictionary to store the values pulled from results
    samples_dict = {}

    #Access each element within results to grab the data for each column
    samples_dict["AGE"] = results[0][0]
    samples_dict["BBTYPE"] = results[0][1]
    samples_dict["ETHNICITY"] = results[0][2]
    samples_dict["GENDER"] = results[0][3]
    samples_dict["LOCATION"] = results[0][4]
    samples_dict["SAMPLEID"] = results[0][5]
    all_samples.append(samples_dict)

    return jsonify(all_samples)


@app.route('/wfreq/<sample>')
def bellybutton_wfreq(sample):

    results = session.query(SamplesMeta.WFREQ).\
                filter(SamplesMeta.SAMPLEID == sample[3:]).all()

    wfreq = np.ravel(results)

    return jsonify(int(wfreq[0]))


@app.route('/samples/<sample>')
def samples(sample):

    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)

    # Check to see if sample is found
    if sample not in df.columns:
        return jsonify(f"Sample {sample} was not found")

    # Return any sample values greater than 1
    df = df[df[sample] > 1]

    # Sort results in descending order
    df = df.sort_values(by=sample, ascending=0)

    # Create a list of dictionaries 
    data = [{"otu_ids": df[sample].index.values.tolist(),
            "sample_values": df[sample].values.tolist()
            }]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
