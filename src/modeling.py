import pandas as pd
import numpy as np
from fuzzywuzzy import process
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import MinMaxScaler
import mysql.connector
from mysql.connector import Error
import joblib
from util import fetch_data_from_db, web_scraper
import requests
import pickle


def source_data(table_name, web_scraper_url):
    '''
    This function fetches data from the MySQL database and returns it as a Pandas DataFrame.
    '''
    data = fetch_data_from_db(table_name)
    return data

def preprocess_data():
    web_scraper_url = 'https://www.hofstede-insights.com/country-comparison-tool'
    mysql_table_name = 'longevity.LONGEVITY'
    scraped_data = web_scraper(web_scraper_url)
    # save scraped data to csv
    scraped_data.to_csv('../data/cleaned/culture_df.csv')
    data = fetch_data_from_db(mysql_table_name)
    return data


def train_rf_model(data):
    '''
    This function trains a Random Forest Regressor model on the data and returns
    the model and the predictions.
    '''
    # dropping columns with bad data
    data.drop(columns=["Measles", "Polio",
              "Literacy rate, youth total"], inplace=True)

    # Select columns to normalize
    columns_to_normalize = [col for col in data.columns if col not in [
        'Country Name', 'Life expectancy at birth, total (years)']]

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Normalize the selected columns
    data[columns_to_normalize] = scaler.fit_transform(
        data[columns_to_normalize])

    # Exclude the 'Country Name' column which is not needed for the model
    target = 'Life expectancy at birth, total (years)'
    X = data.drop(columns=[target, 'Country Name'])
    y = data[target]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=0)

    # Initialize the Random Forest Regressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=0)

    # Fit the model on the training data
    rf_model.fit(X_train, y_train)
    preds = rf_model.predict(X_test)

    # Save the model
    save_pickled_model(rf_model)

    return rf_model, preds


# Function to predict life expectancy and top 3 influencing features for a given country
def predict_life_expectancy(country_name):
    '''
    This function returns the predicted life expectancy for a given country
    and the top 3 features that influence the prediction.
    '''
    file_path = '../data/Cleaned/longevity_reduced.csv'
    data = pd.read_csv(file_path)
    data_copy = data.copy()
    target = 'Life expectancy at birth, total (years)'
    # Find the row in the dataframe that corresponds to the given country
    country_data = data_copy[data_copy['Country Name'] == country_name].drop(
        columns=[target, 'Country Name'])
    # load the model
    life_expectancy = data[data['Country Name'] == country_name][target].values[0]
    top_z_score_features = find_top_z_score_features(data, target, country_name)
    top_rf_features = rf_feature_importance(country_data)
    
    return life_expectancy, top_rf_features, top_z_score_features
    # Function to find the top features based on Z-scores alone for the United States

def rf_feature_importance(country_data):
    '''
    This function returns the top 3 features for a given country based on the feature
    importances of the Random Forest model.
    '''
    # Get feature importances specific to the country's data
    rf_model = load_pickled_model()
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[-5:]  # Get indices of top 3 features
    top_features = country_data.columns[indices].tolist()  # Get names of top 3 features
    # return if the deviation is higher or lower than the mean
    return top_features

def find_top_z_score_features(data, target, country_name):
    '''
    This function returns the top 3 features for a given country based on the Z-scores
    of the features.
    '''
    # Isolate the row for the given country
    country_row = data[data['Country Name'] == country_name].drop(
        columns=[target, 'Country Name'])
    X = data.drop(columns=[target, 'Country Name'])

    # Calculate the mean and std deviation for the features
    mean_values = X.mean()
    std_dev_values = X.std()

    # Calculate the Z-scores for the country's features
    z_scores = (country_row - mean_values) / std_dev_values
    z_scores = z_scores.squeeze()

    # Make new series for z-score sign
    z_scores_signed = z_scores.copy()
    z_scores_signed[z_scores_signed > 0] = 1
    z_scores_signed[z_scores_signed < 0] = -1

    # Sort by absolute Z-score value
    sorted_z_scores = z_scores.abs().sort_values(ascending=False)

    # Multiply the sign by the absolute value to get a series with the sorted magnitudes
    for index, value in sorted_z_scores.items():
        sorted_z_scores[index] = value * z_scores_signed[index]

    top_z_scores = sorted_z_scores.head(25)

    return top_z_scores


def get_country_name_conversions(data):
    '''
    This function returns a dictionary of country names from the world atlas
    and the corresponding country names from the World Bank data.
    '''
    url = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json"
    # Get json from url
    r = requests.get(url)
    # Convert to dict
    d = r.json()

    countries = []
    for country in d["objects"]["countries"]["geometries"]:
        name = country["properties"]["name"]
        countries.append(name)

        sorted_countries = sorted(countries)
        # Get countries from df
        df_countries = data["Country Name"].unique()

        # Convert to list
        df_countries = df_countries.tolist()
        sorted_df_countries = sorted(df_countries)
        conversion_dict = {}
        z = 0
        for c in sorted_countries:
            match, score = process.extractOne(c, df_countries)

            if score >= 94:
                conversion_dict[c] = match
            else:
                print(f"{c} ---> {match}")
                conversion_dict[c] = None
                z += 1
        for key in conversion_dict.keys():
            if conversion_dict[key] and conversion_dict[key] != key:
                print(f"Key: {key}, Value: {conversion_dict[key]}")
        return conversion_dict


def save_pickled_model(model):
    '''
    This function saves the model as a pickle file.
    '''
    with open('../models/rf_model.pkl', 'wb') as f:
        pickle.dump(model, f)


def load_pickled_model():
    '''
    This function loads the pickle file and returns the model.
    '''
    with open('../models/rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model