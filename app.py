# import necessary libraries
import os
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import String
from sqlalchemy import cast, func

##############
# Flask set up
##############
app = Flask(__name__)

################
# Database Setup
################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

# from .models import SamplesMeta
# from .models import Samples
class SamplesMeta(db.Model):
    __tablename__ = 'samples_metadata'

    sampleid = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String)
    ethnicity = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    wfreq = db.Column(db.Integer)
    bbtype = db.Column(db.String)
    location = db.Column(db.String)
    country012 = db.Column(db.String)
    zip012 = db.Column(db.Integer)
    country1319 =db.Column(db.String)
    zip1319 = db.Column(db.Integer)
    dog = db.Column(db.String)
    cat = db.Column(db.String)
    impsurface013 = db.Column(db.Integer)
    npp013 = db.Column(db.Float)
    mmaxtemp013 = db.Column(db.Float)
    pfc013 = db.Column(db.Float)
    impsurface1319 = db.Column(db.Integer)
    npp1319 = db.Column(db.Float)
    mmaxtemp1319 = db.Column(db.Float)
    pfc1319 = db.Column(db.Float)

    def __repr__(self):
        return '<BellyButton %r>' % (self.gender)

class Otu(db.Model):
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)

    def __repr__(self):
        return '<Otu %r>' % (self.otu_id)


class Samples(db.Model):
    __tablename__ = 'samples'

    otu_id = db.Column(db.Integer, primary_key=True)
    BB_940 = db.Column(db.Integer)
    BB_941 = db.Column(db.Integer)
    BB_943 = db.Column(db.Integer)
    BB_944 = db.Column(db.Integer)
    BB_945 = db.Column(db.Integer)
    BB_946 = db.Column(db.Integer)
    BB_947 = db.Column(db.Integer)
    BB_948 = db.Column(db.Integer)
    BB_949 = db.Column(db.Integer)
    BB_950 = db.Column(db.Integer)
    BB_952 = db.Column(db.Integer)
    BB_953 = db.Column(db.Integer)
    BB_954 = db.Column(db.Integer)
    BB_955 = db.Column(db.Integer)
    BB_956 = db.Column(db.Integer)
    BB_958 = db.Column(db.Integer)
    BB_959 = db.Column(db.Integer)
    BB_960 = db.Column(db.Integer)
    BB_961 = db.Column(db.Integer)
    BB_962 = db.Column(db.Integer)
    BB_963 = db.Column(db.Integer)
    BB_964 = db.Column(db.Integer)
    BB_966 = db.Column(db.Integer)
    BB_967 = db.Column(db.Integer)
    BB_968 = db.Column(db.Integer)
    BB_969 = db.Column(db.Integer)
    BB_970 = db.Column(db.Integer)
    BB_971 = db.Column(db.Integer)
    BB_972 = db.Column(db.Integer)
    BB_973 = db.Column(db.Integer)
    BB_974 = db.Column(db.Integer)
    BB_975 = db.Column(db.Integer)
    BB_978 = db.Column(db.Integer)
    BB_1233 = db.Column(db.Integer)
    BB_1234 = db.Column(db.Integer)
    BB_1235 = db.Column(db.Integer)
    BB_1236 = db.Column(db.Integer)
    BB_1237 = db.Column(db.Integer)
    BB_1238 = db.Column(db.Integer)
    BB_1242 = db.Column(db.Integer)
    BB_1243 = db.Column(db.Integer)
    BB_1246 = db.Column(db.Integer)
    BB_1253 = db.Column(db.Integer)
    BB_1254 = db.Column(db.Integer)
    BB_1258 = db.Column(db.Integer)
    BB_1259 = db.Column(db.Integer)
    BB_1260 = db.Column(db.Integer)
    BB_1264 = db.Column(db.Integer)
    BB_1265 = db.Column(db.Integer)
    BB_1273 = db.Column(db.Integer)
    BB_1275 = db.Column(db.Integer)
    BB_1276 = db.Column(db.Integer)
    BB_1277 = db.Column(db.Integer)
    BB_1278 = db.Column(db.Integer)
    BB_1279 = db.Column(db.Integer)
    BB_1280 = db.Column(db.Integer)
    BB_1281 = db.Column(db.Integer)
    BB_1282 = db.Column(db.Integer)
    BB_1283 = db.Column(db.Integer)
    BB_1284 = db.Column(db.Integer)
    BB_1285 = db.Column(db.Integer)
    BB_1286 = db.Column(db.Integer)
    BB_1287 = db.Column(db.Integer)
    BB_1288 = db.Column(db.Integer)
    BB_1289 = db.Column(db.Integer)
    BB_1290 = db.Column(db.Integer)
    BB_1291 = db.Column(db.Integer)
    BB_1292 = db.Column(db.Integer)
    BB_1293 = db.Column(db.Integer)
    BB_1294 = db.Column(db.Integer)
    BB_1295 = db.Column(db.Integer)
    BB_1296 = db.Column(db.Integer)
    BB_1297 = db.Column(db.Integer)
    BB_1298 = db.Column(db.Integer)
    BB_1308 = db.Column(db.Integer)
    BB_1309 = db.Column(db.Integer)
    BB_1310 = db.Column(db.Integer)
    BB_1374 = db.Column(db.Integer)
    BB_1415 = db.Column(db.Integer)
    BB_1439 = db.Column(db.Integer)
    BB_1441 = db.Column(db.Integer)
    BB_1443 = db.Column(db.Integer)
    BB_1486 = db.Column(db.Integer)
    BB_1487 = db.Column(db.Integer)
    BB_1489 = db.Column(db.Integer)
    BB_1490 = db.Column(db.Integer)
    BB_1491 = db.Column(db.Integer)
    BB_1494 = db.Column(db.Integer)
    BB_1495 = db.Column(db.Integer)
    BB_1497 = db.Column(db.Integer)
    BB_1499 = db.Column(db.Integer)
    BB_1500 = db.Column(db.Integer)
    BB_1501 = db.Column(db.Integer)
    BB_1502 = db.Column(db.Integer)
    BB_1503 = db.Column(db.Integer)
    BB_1504 = db.Column(db.Integer)
    BB_1505 = db.Column(db.Integer)
    BB_1506 = db.Column(db.Integer)
    BB_1507 = db.Column(db.Integer)
    BB_1508 = db.Column(db.Integer)
    BB_1510 = db.Column(db.Integer)
    BB_1511 = db.Column(db.Integer)
    BB_1512 = db.Column(db.Integer)
    BB_1513 = db.Column(db.Integer)
    BB_1514 = db.Column(db.Integer)
    BB_1515 = db.Column(db.Integer)
    BB_1516 = db.Column(db.Integer)
    BB_1517 = db.Column(db.Integer)
    BB_1518 = db.Column(db.Integer)
    BB_1519 = db.Column(db.Integer)
    BB_1521 = db.Column(db.Integer)
    BB_1524 = db.Column(db.Integer)
    BB_1526 = db.Column(db.Integer)
    BB_1527 = db.Column(db.Integer)
    BB_1530 = db.Column(db.Integer)
    BB_1531 = db.Column(db.Integer)
    BB_1532 = db.Column(db.Integer)
    BB_1533 = db.Column(db.Integer)
    BB_1534 = db.Column(db.Integer)
    BB_1535 = db.Column(db.Integer)
    BB_1536 = db.Column(db.Integer)
    BB_1537 = db.Column(db.Integer)
    BB_1539 = db.Column(db.Integer)
    BB_1540 = db.Column(db.Integer)
    BB_1541 = db.Column(db.Integer)
    BB_1542 = db.Column(db.Integer)
    BB_1543 = db.Column(db.Integer)
    BB_1544 = db.Column(db.Integer)
    BB_1545 = db.Column(db.Integer)
    BB_1546 = db.Column(db.Integer)
    BB_1547 = db.Column(db.Integer)
    BB_1548 = db.Column(db.Integer)
    BB_1549 = db.Column(db.Integer)
    BB_1550 = db.Column(db.Integer)
    BB_1551 = db.Column(db.Integer)
    BB_1552 = db.Column(db.Integer)
    BB_1553 = db.Column(db.Integer)
    BB_1554 = db.Column(db.Integer)
    BB_1555 = db.Column(db.Integer)
    BB_1556 = db.Column(db.Integer)
    BB_1557 = db.Column(db.Integer)
    BB_1558 = db.Column(db.Integer)
    BB_1561 = db.Column(db.Integer)
    BB_1562 = db.Column(db.Integer)
    BB_1563 = db.Column(db.Integer)
    BB_1564 = db.Column(db.Integer)
    BB_1572 = db.Column(db.Integer)
    BB_1573 = db.Column(db.Integer)
    BB_1574 = db.Column(db.Integer)
    BB_1576 = db.Column(db.Integer)
    BB_1577 = db.Column(db.Integer)
    BB_1581 = db.Column(db.Integer)
    BB_1601 = db.Column(db.Integer)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/names")
def bellybutton_name():

    #Write a query to filter out all sample ids with BB_ concated to it and return a list
    results = db.session.query("BB_" + cast(SamplesMeta.sampleid, String)).all()

    all_sampleids = list(np.ravel(results))

    return jsonify(all_sampleids)

@app.route('/otu')
def bellybutton_otu():

    #Write a query to list all otu descriptions from the otu table 
    results = db.session.query(Otu.lowest_taxonomic_unit_found).all()

    all_otu = list(np.ravel(results))

    return jsonify(all_otu)


@app.route('/metadata/<sample>')
def bellybutton_metadata_sample(sample):

    #grab all the columns we need and create a list
    sel = [SamplesMeta.age,
        SamplesMeta.bbtype,
        SamplesMeta.ethnicity,
        SamplesMeta.gender,
        SamplesMeta.location,
        SamplesMeta.sampleid]

    #Query the above columns for the sample id provided by user
    results = db.session.query(*sel).\
                filter(SamplesMeta.sampleid == sample).all()
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

    results = db.session.query(SamplesMeta.wfreq).\
                filter("BB_" + SamplesMeta.sampleid == "BB_" + sample).all()

    wfreq_list = []
    wfreq_dict = {}
    wfreq_dict["wfreq"] = results
    wfreq_list.append(wfreq_dict)
    return jsonify(wfreq_list)
#     """Weekly Washing Frequency as a number.

#     Args: Sample in the format: `BB_940`

#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """


# @app.route('/samples/<sample>')
#     """OTU IDs and Sample Values for a given sample.

#     Sort your Pandas DataFrame (OTU ID and Sample Value)
#     in Descending Order by Sample Value

#     Return a list of dictionaries containing sorted lists  for `otu_ids`
#     and `sample_values`

#     [
#         {
#             otu_ids: [
#                 1166,
#                 2858,
#                 481,
#                 ...
#             ],
#             sample_values: [
#                 163,
#                 126,
#                 113,
#                 ...
#             ]
#         }
#     ]
    # """
    




if __name__ == "__main__":
    app.run(debug=True)
