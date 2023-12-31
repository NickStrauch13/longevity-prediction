from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
import pandas as pd
import json
from predict_life_expectancy import predict_new_life_expectancy, get_country_data
from scipy.stats import norm
from format_percentiles import format_percentiles
from country_exceptions import check_for_exceptions
from load_data import load_data



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
DF = load_data()
COUNTRY_NORMALIZATION = json.load(open('../Data/country_conversion.json', 'r'))


@app.route('/get_country_data', methods=['GET'])
@cross_origin()
def get_country_data_route():
    country_name = request.args.get('country')
    country_name = COUNTRY_NORMALIZATION[country_name]
    # Check for exceptions
    country_exception = check_for_exceptions(country_name)
    if country_exception:
        return jsonify(country_exception)
    
    life_expectancy, top_country_features = get_country_data(DF, country_name)
    # Clean life expectancy float
    life_expectancy = round(life_expectancy, 1)
    # Convert series to list of dicts
    top_country_features = top_country_features.to_dict()
    top_country_features = [{'feature': key, 'std_devs': round(value,3), 'percentile': round(norm.cdf(value) * 100, 0)} for key, value in top_country_features.items()]
    top_country_features = format_percentiles(top_country_features)

    # Format response
    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'life_expectancy': life_expectancy,
        'top_features': top_country_features
    }
    
    return jsonify(response)
    


@app.route('/calc_life_expec', methods=['POST'])
@cross_origin()
def generate():
    query = request.json['query']
    country = query['country']



if __name__ == '__main__':
    app.run(debug=True)