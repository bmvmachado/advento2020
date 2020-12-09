import re

validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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

def validEyeColor(eyeColor,  eyeColorDef):
    return eyeColor !=  eyeColorDef and validEyeColors.count(eyeColor)


def validPassport(value,  valueDef):
    parsedValue = intTryParse(value)

    return parsedValue[1] and value !=  valueDef and len(value) == 9 


def validHeight(value,  valueDef):
    isValid = False
    if value != valueDef and ( value.find("cm")> 0 or value.find("in")> 0):
        if value.find("cm")> 0 :
            value = intTryParse(value.replace("cm", ""))    
            isValid = value[1] and 150<=value[0]<=193                
        else :
            value = intTryParse(value.replace("in", ""))
            isValid = value[1] and 59<=value[0]<=76
    return isValid

def validHairColor(value,  valueDef):
    isValid = False
    if value != valueDef and len(value) == 7 and value[0] == "#":
        isValid = re.search("^#[0-9a-f]{6}", value)
        print(f"{value} isValid: {isValid}")
    return isValid
    
    