import sys

# Local
from modeling import predict_life_expectancy

def main():
    option = str(sys.argv[1]).lower().strip()
    if option == "train":
        pass
    elif option == "predict":
        country_name = str(sys.argv[2]).lower().title().strip()

        print("Country Name: ", country_name)
        life_expectancy, top_rf_features, top_z_score_features = predict_life_expectancy(country_name)
        print("Life Expectancy: ", life_expectancy)
        print("Top RF Features: ", top_rf_features)
        print("Top Z-Score Features: ", top_z_score_features)
    else:
        print("Invalid option. Please enter either 'train' or 'predict'.")
        sys.exit(1)
if __name__ == "__main__":
    main()
