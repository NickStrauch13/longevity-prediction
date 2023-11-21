import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import MinMaxScaler
import mysql.connector
from mysql.connector import Error
import joblib
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def fetch_data_from_db(tablename):
    '''
    This function fetches data from the MySQL database and returns it as a Pandas DataFrame.
    ''' 
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

def web_scraper(url):
    # Scrping data from hofstedes website
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # find the class: "l-comparison__content__item-multiple__top"
    table = soup.find('div', attrs={'class': 'l-comparison__content__item-multiple__top'})
    # loop through all classes c-overview fadeInUp
    culture_dict = {}
    for row in table.findAll('div', attrs={'class': 'c-overview fadeInUp'}):
        # save country name as key and score as value
        country_scores = []
        # save country name within data-country in dictionary as key
        country = row['data-country']
        # power-distance score in span class
        power_distance = row.find('span', attrs={'class': 'power-distance fadeIn active'}).text
        individualism = row.find('span', attrs={'class': 'individualism fadeIn'}).text
        motivation = row.find('span', attrs={'class': 'motivation fadeIn'}).text
        uncertainty_avoidance = row.find('span', attrs={'class': 'uncertainty-avoidance fadeIn'}).text
        long_term_orientation = row.find('span', attrs={'class': 'long-term-orientation fadeIn'}).text
        indulgence = row.find('span', attrs={'class': 'indulgence fadeIn'}).text

        # save country name as key and score as value
        country_scores.append(power_distance)
        country_scores.append(individualism)
        country_scores.append(motivation)
        country_scores.append(uncertainty_avoidance)
        country_scores.append(long_term_orientation)
        country_scores.append(indulgence)
        if country not in culture_dict:
            culture_dict[country] = country_scores
    
    # create dataframe from dictionary
    culture_df = pd.DataFrame.from_dict(culture_dict, orient='index', columns=['power_distance', 'individualism', 'motivation', 'uncertainty_avoidance', 'long_term_orientation', 'indulgence'])
    culture_df.head()

    return culture_df
