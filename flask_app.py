
# Import Dependencies
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS



#################################################
'''
Run these commands in terminal/bash to import the csv files to our database:
    mongod
    mongoimport --type csv -d HDI -c hdi_countries --headerline --drop HDI_countries.csv
    mongoimport --type csv -d HDI -c hdi_regions --headerline --drop HDI_regions.csv
    mongoimport --type csv -d HDI -c hdi_levels --headerline --drop HDI_levels.csv
    mongoimport --type csv -d HDI -c ihdi_countries --headerline --drop IHDI_countries.csv
    mongoimport --type csv -d HDI -c ihdi_regions --headerline --drop IHDI_regions.csv
    mongoimport --type csv -d HDI -c ihdi_levels --headerline --drop IHDI_levels.csv
    mongoimport --type csv -d HDI -c le_countries --headerline --drop le_countries.csv
    mongoimport --type csv -d HDI -c le_regions --headerline --drop le_regions.csv
    mongoimport --type csv -d HDI -c le_levels --headerline --drop le_levels.csv
    mongoimport --type csv -d HDI -c eys_countries --headerline --drop eys_countries.csv
    mongoimport --type csv -d HDI -c eys_regions --headerline --drop eys_regions.csv
    mongoimport --type csv -d HDI -c eys_levels --headerline --drop eys_levels.csv
    mongoimport --type csv -d HDI -c mys_countries --headerline --drop mys_countries.csv
    mongoimport --type csv -d HDI -c mys_regions --headerline --drop mys_regions.csv
    mongoimport --type csv -d HDI -c mys_levels --headerline --drop mys_levels.csv
    mongoimport --type csv -d HDI -c gni_countries --headerline --drop GNI_countries.csv
    mongoimport --type csv -d HDI -c gni_regions --headerline --drop GNI_regions.csv
    mongoimport --type csv -d HDI -c gni_levels --headerline --drop GNI_levels.csv
    mongoimport --type csv -d HDI -c gii_countries --headerline --drop GII_countries.csv
    mongoimport --type csv -d HDI -c gii_regions --headerline --drop GII_regions.csv
    mongoimport --type csv -d HDI -c gii_levels --headerline --drop GII_levels.csv
    

'''
#################################################
# Database Setup
#################################################

mongo = MongoClient(port=27017)
db = mongo['HDI']
hdi_countries = db['hdi_countries']
ihdi_countries = db['ihdi_countries']
gii_countries = db['gii_countries']
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def names():
    # query = {'HDI Code' : 'Very High'}
    results_hdi =  hdi_countries.find()
    results_ihdi = ihdi_countries.find()
    results_gii = gii_countries.find()
    # Convert MongoDB results to a format that's easily serializable
    hdi_outputs = {}
    output = []
    for result in results_hdi: #results_ihdi, results_gii:
        
        # Convert ObjectId to string
        result['_id'] = str(result['_id'])  
        output.append(result)
        
    hdi_outputs['hdi'] = output

    output = []
    for result in results_ihdi: #, results_gii:
        
        # Convert ObjectId to string
        result['_id'] = str(result['_id'])  
        output.append(result)
        
    hdi_outputs['ihdi'] = output

    output = []
    for result in results_gii: #, :
        # Convert ObjectId to string
        result['_id'] = str(result['_id'])  
        output.append(result)
        
    hdi_outputs['gii'] = output

    return hdi_outputs


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9500, debug=True)