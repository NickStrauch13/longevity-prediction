import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import MinMaxScaler
import mysql.connector
from mysql.connector import Error
import joblib
import matplotlib.pyplot as plt


def fetch_data_from_db(tablename):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='longevity',
            user='root',
            password='root'
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)

    data = pd.read_sql(f'SELECT * FROM {tablename}', con=connection)
    connection.close()
    return data
