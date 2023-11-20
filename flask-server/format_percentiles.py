def format_percentiles(feature_dict: dict) -> dict:
    """
    Formats the percentile values to be more readable.
    """
    for d in feature_dict:
        percent = int(d['percentile'])
        if percent == 100:
            percent = 99
        if percent == 0:
            percent = 1
        str_percentile = str(percent)
        if str_percentile.endswith('1'):
            d['percentile'] = str_percentile + 'st'
        elif str_percentile.endswith('2'):
            d['percentile'] = str_percentile + 'nd'
        elif str_percentile.endswith('3'):
            d['percentile'] = str_percentile + 'rd'
        else:
            d['percentile'] = str_percentile + 'th'
    return feature_dict
