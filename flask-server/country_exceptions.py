def check_for_exceptions(country_name: str) -> dict:
    """
    Static country exceptions. 
    This handles countries that are not in the dataset, or countries that have no data.
    """
    if country_name == "Antarctica":
        return {
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'life_expectancy': 0,
            'top_features': [{'feature': "Cold", 'std_devs': 5, 'percentile': "100th"}]
        }
    return None