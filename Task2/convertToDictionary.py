def convert_to_dictionary(**kwargs):
    result = {}

    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result
