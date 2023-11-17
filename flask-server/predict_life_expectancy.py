import joblib
import pandas as pd


def predict_life_expectancy(input_data: pd.DataFrame) -> float :
    """
    Use the saved model to predict the life expectancy of a country

    Args:
        input_data (pd.DataFrame): Dataframe containing the input data

    Returns:
        float: Predicted life expectancy
    """

    # Load the model and predict
    model = joblib.load("../models/rf_model.joblib")
    pred_life_expectancy = model.predict(input_data)

    return pred_life_expectancy[0]



