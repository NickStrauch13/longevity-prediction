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
        print("Life Expectancy: ", predict_life_expectancy(country_name))


if __name__ == "__main__":
    main()
