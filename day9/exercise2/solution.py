def existsSumInArray(valueToCompare, values):
	for firstValue in values :
		for secondValue in values :
			if firstValue != secondValue and (firstValue + secondValue) == valueToCompare:
				return True;
	return False;

def sumContiguous(valueToCompare, values):
	setNumbers = []
	sumValue = 0;
	for firstValue in values :
		sumValue = sumValue + firstValue
		setNumbers.append(firstValue)
		if sumValue == valueToCompare :
				return (True,setNumbers)
	
	return (False, []);
				

f = open("advento2020/day9/input.txt", "r")
lines = f.readlines()

xmasNumbers = []
notValidNumbers = []
preamble = 25
for current in lines:
	parsedValue = int(current.strip())
	if len(xmasNumbers) >= (preamble + 1) and not existsSumInArray(parsedValue,xmasNumbers[len(xmasNumbers)-(preamble + 1):len(xmasNumbers)]):
		notValidNumbers.append(parsedValue)
	
	xmasNumbers.append(parsedValue)	
		
print(notValidNumbers)

valueToCompare = notValidNumbers[0]

index = 0;
result = {}
while index < len(xmasNumbers) :
	result = sumContiguous(valueToCompare,xmasNumbers[index:len(xmasNumbers)])
	index = index +1

	if result[0] :
		print(sorted(result[1]))
		break;

sortedList = sorted(result[1])
print (f"{sortedList[0]} + {sortedList[len(sortedList)-1]} = {sortedList[0] + sortedList[len(sortedList)-1]}" )