def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def validYear(value,valueDef, lowerBound, higherBound):
    isValid = False
    if len(value) == 4 and value != valueDef:
        value = intTryParse(value)
        isValid = value[1] and lowerBound<=value[0]<=higherBound                
                
    return isValid