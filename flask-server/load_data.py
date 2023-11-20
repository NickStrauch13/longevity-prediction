import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_data() -> pd.DataFrame:
    """
    Load the data from the csv file

    Returns: 
        pd.DataFrame: Dataframe containing the data
    """

    # Load the data
    file_path = '../data/Cleaned/longevity_reduced.csv'
    data = pd.read_csv(file_path)
    data.drop(columns=["Measles", "Polio", "Literacy rate, youth total", "Prevalence of HIV"], inplace=True)

    # Select columns to normalize
    columns_to_normalize = [col for col in data.columns if col not in ['Country Name', 'Life expectancy at birth, total (years)']]

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Normalize the selected columns
    data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

    return data