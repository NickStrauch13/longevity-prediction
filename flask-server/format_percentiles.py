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
            if str_percentile == '11':
                d['percentile'] = str_percentile + 'th'
        elif str_percentile.endswith('2'):
            d['percentile'] = str_percentile + 'nd'
            if str_percentile == '12':
                d['percentile'] = str_percentile + 'th'
        elif str_percentile.endswith('3'):
            d['percentile'] = str_percentile + 'rd'
            if str_percentile == '13':
                d['percentile'] = str_percentile + 'th'
        else:
            d['percentile'] = str_percentile + 'th'
    return feature_dict
