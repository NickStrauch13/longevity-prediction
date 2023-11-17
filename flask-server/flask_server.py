from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from predict_life_expectancy import predict_life_expectancy

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get_country_data', methods=['GET'])
@cross_origin()
def get_difficulty_and_stuff():
    country_name = request.args.get('country')
    


@app.route('/calc_life_expec', methods=['POST'])
@cross_origin()
def generate():
    query = request.json['query']
    country = query['country']



if __name__ == '__main__':
    app.run(debug=True)