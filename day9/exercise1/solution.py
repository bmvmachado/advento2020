def existsSumInArray(valueToCompare, values):
	for firstValue in values :
		for secondValue in values :
			if firstValue != secondValue and (firstValue + secondValue) == valueToCompare:
				return True;
	return False;

f = open("advento2020/day9/input.txt", "r")
lines = f.readlines()

xmasNumbers = []
notValidNumbers = []
preamble = 5
for current in lines:
	parsedValue = int(current.strip())
	if len(xmasNumbers) >= (preamble + 1) and not existsSumInArray(parsedValue,xmasNumbers[len(xmasNumbers)-(preamble + 1):len(xmasNumbers)]):
		notValidNumbers.append(parsedValue)
	
	xmasNumbers.append(parsedValue)	
		
print(notValidNumbers)
