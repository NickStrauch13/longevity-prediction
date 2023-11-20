import joblib
import pandas as pd
from typing import Tuple


MODEL = joblib.load("../models/rf_model.joblib")


def get_country_data(df: pd.DataFrame, country_name: str, n: int = 8) -> Tuple[float, pd.Series]:
    """
    Return the top n features for the given country
    """
    # Isolate the row for the given country
    target = 'Life expectancy at birth, total (years)'
    country_row = df[df['Country Name'] == country_name].drop(columns=[target, 'Country Name'])
    X = df.drop(columns=[target, 'Country Name'])
    life_expect = float(df[df['Country Name'] == country_name][target].squeeze())

    # Calculate the mean and std deviation for the features in the dataset
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

    top_z_scores = sorted_z_scores.head(n)

    # Isolate the top features for the country using the zscores and the model importances
    ret_best_zscores = crossover_feature_importances(top_z_scores)

    return life_expect, ret_best_zscores


def crossover_feature_importances(top_z_scores: pd.Series) -> pd.Series:
    """
    Utlize the feature importances from the model and z-scores to idolate the most influential 
    features for a single country.

    Args:
        top_z_scores (pd.Series): Series containing the top z-scores for a country

    Returns:
        pd.DataFrame: Series containing the top features for a country
    """
    try:
        top_feats_curr_rf = MODEL.feature_importances_[top_z_scores.index]
        curr_b_features = top_z_scores.copy()
        top_feats_indexed = pd.Series(top_feats_curr_rf, index=top_z_scores.index)
        top_feats_i = top_feats_indexed.sort_values(ascending=False)
        for isolated_feature in top_feats_i.index:
            top_feats_i[isolated_feature] = top_feats_i[isolated_feature] / top_feats_curr_rf.sum()
            top_feats_i[isolated_feature] = top_feats_i[isolated_feature] * top_z_scores[isolated_feature]
            if top_feats_i[isolated_feature] < 0 and isolated_feature != 'Life expectancy at birth, total (years)' and isinstance(isolated_feature, float):
                curr_b_features[isolated_feature] = top_feats_i[isolated_feature]
                top_feats_i[isolated_feature] = 0
        top_feats_rel = top_feats_i.sort_values(ascending=True)
        top_feats_rel = top_feats_rel[top_feats_rel > top_feats_indexed.mean()]
        return curr_b_features
    except:
        # Country with no overlap
        return top_z_scores


def predict_new_life_expectancy(input_data: pd.DataFrame) -> float :
    """
    Use the saved model to predict the life expectancy of a country

    Args:
        input_data (pd.DataFrame): Dataframe containing the input data

    Returns:
        float: Predicted life expectancy
    """

    pred_life_expectancy = MODEL.predict(input_data)

    return pred_life_expectancy[0]
        