# Longevity Prediction Tool
[Vist our site!](https://global-longevity-insights-706bdfb27940.herokuapp.com/)

![Alt text](img/readme_header_image.png)

## Overview
The Life Expectancy Prediction Model is a data-driven project designed to analyze and predict life expectancy for individuals in specific countries based on a wide array of features. Unlike traditional models that focus solely on prediction accuracy, our model stands out by emphasizing the interpretability of feature importance. The primary goal is to empower users with insights into the key drivers influencing life expectancy in a given country.

## Project Features

-`Interpretability`: The model's value lies not only in accurate predictions but also in its ability to highlight the most influential features impacting life expectancy.

-`Feature Importance`: Users can explore and understand the significance of different factors affecting life expectancy, offering a nuanced view of health determinants.

-`User Interaction`: Future updates will introduce a user-friendly interface allowing users to modify a country's feature values. The model will dynamically update predictions, showcasing the potential impact of changes in specific features on life expectancy.

## Data Sources
1. World Bank (CSV)​

       https://databank.worldbank.org/source/world-development-indicatorshttps://databank.worldbank.org/source/world-development-indicators   ​

2. Kaggle (CSV) ​

       https://www.kaggle.com/code/himanshukumar7079/life-expectancy-eda-pred#Loading-Data ​

3. The Culture Factor (Web Scraping)​

        https://www.hofstede-insights.com/country-comparison-tool

## How to Launch Locally
If you wish to launch this project locally, follow the steps below:

1. Clone the repository to your local machine.
2. Install Python and Node.js if not already installed.
3. Create a Python virtual environment 
   - This project runs on Python `3.9.12`, and guaranteed support for newer versions is coming soon.
   - Initalize environment with: `python -m venv venv`
   - Download dependencies with: `pip install -r requirements.txt`
   - Activate environment with: `source venv/bin/activate` (mac) or `venv\Scripts\activate` (windows)
4. Install Node.js dependencies
   - Navigate into the react-app directory: `cd react-app`
   - Install dependencies: `npm install`
5. Start Flask server
   - Navigate back to the root directory: `cd ..`
   - Navigate into the server directory: `cd flask-server`
   - Start the server: `python flask_server.py`
6. Start React server
   - Navigate back to the root directory: `cd ..`
   - Navigate into the react-app directory: `cd react-app`
   - Start the server: `npm start`

`Note:` For ease of local use, cleaned data files are downloaded into a project repository. Our full MySQL database is accessed via the Heroku server and is not required to run the project locally. If you wish to see how we connect to the database, please see the `load_data.py` file in the `flask-server` directory.


## Project Structure
```
├── README.md
├── flask-server
│   ├── flask_server.py
│   ├── predict_life_expectancy.py
│   ├── country_exceptions.py
│   ├── format_percentiles.py
│   ├── load_data.py
├── react-app
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── App.css
│   │   ├── apis
│   │   │   ├── country_data.js
│   │   ├── components
│   │   │   ├── CountryStats.js
│   │   │   ├── InteractiveMap.js
│   │   │   ├── NavBar.js
│   │   │   ├── stats_components
│   │   │   │   ├── IndividualData.js
│   │   │   │   ├── LifeExpecNum.js
│   │   │   │   ├── LocationData.js
│   │   ├── pages
│   │   │   ├── Home.js
│   │   │   ├── WorldMap.js
│   │   |   ├── index.js
│   ├── package.json
│   ├── package-lock.json
├── notebooks
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   ├── feature_engineering.ipynb
│   ├── modeling.ipynb
├── Data
│   ├── country_conversion.json
│   ├── country_life_expectancy.csv
│   ├── Cleaned
│   │   ├── cultural_df.csv
│   │   ├── features_flagged.csv
│   │   ├── longevity_reduced.csv
│   │   ├── longevity.csv
├── .gitignore
├── requirements.txt
