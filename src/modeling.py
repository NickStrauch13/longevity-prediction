import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fuzzywuzzy import process
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import MinMaxScaler
import mysql.connector
from mysql.connector import Error
import joblib
import matplotlib.pyplot as plt


def source_data():
    data = fetch_data_from_db("longevity.LONGEVITY")
    return data


def train_rf_model(data):
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

    return rf_model, preds


# Function to predict life expectancy and top 3 influencing features for a given country
def predict_life_expectancy(country_name):
    file_path = '../data/Cleaned/longevity_reduced.csv'
    data = pd.read_csv(file_path)
    target = 'Life expectancy at birth, total (years)'

    # Find the row in the dataframe that corresponds to the given country
    country_data = data[data['Country Name'] == country_name].drop(
        columns=[target, 'Country Name'])

    # Predict life expectancy using the trained model
    rf_model = joblib.load('../models/rf_model.joblib')
    life_expectancy = rf_model.predict(country_data)

    # Calculate the deviation of the country's feature values from the dataset mean
    deviations = country_data.squeeze() - X.mean()

    # Determine if the deviation is higher or lower than the mean
    deviation_direction = deviations.apply(
        lambda x: 'higher' if x > 0 else 'lower')

    # Combine the absolute deviation and its direction
    deviations_with_direction = deviations.abs().sort_values(ascending=False).head(5)
    deviations_with_direction = deviations_with_direction.to_frame(
        name='Deviation')
    deviations_with_direction['Direction'] = deviation_direction.loc[deviations_with_direction.index]

    top_z_score_features = find_top_z_score_features(country_name)

    return life_expectancy[0], deviations_with_direction, top_z_score_features
    # Function to find the top features based on Z-scores alone for the United States


def find_top_z_score_features(country_name):
    # Isolate the row for the given country
    country_row = data[data['Country Name'] == country_name].drop(
        columns=[target, 'Country Name'])

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


def get_country_name_conversions():
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
