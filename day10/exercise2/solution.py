import itertools

def validConfiguration(adapters):
	index = 1
	while index < len(adapters) :
		firstAdapter = adapters[index-1]
		secondAdapter = adapters[index]
		difference = secondAdapter - firstAdapter
		index = index +1
		if difference > 3 :
			return False
	return True;

def runConfigurations(listOfAdapters,cleanList):	
	index = 1
	isValid = validConfiguration(listOfAdapters)

	if listOfAdapters not in cleanList:
			cleanList.append(listOfAdapters[:])
		

	while index < len(listOfAdapters)-1:		
		if 1<= (listOfAdapters[index+1] - listOfAdapters[index-1]) <= 3 : 
			slicedAdapters = listOfAdapters[:index] + listOfAdapters[index+1 :]			
			if slicedAdapters not in cleanList:
				runConfigurations(slicedAdapters, cleanList)
		index = index +1
	return

def getAllCombinations(listOfAdapters):	
	index = 0		
	listSize = len(listOfAdapters)
	slicedAdapters = listOfAdapters[:]

	cleanList = []

	while index < listSize:
		
		combinationsResult = itertools.combinations(slicedAdapters,len(slicedAdapters)-1)
		for result in combinationsResult:
			if result not in cleanList:
				cleanList.append(result);						 
		slicedAdapters = listOfAdapters[:index] + listOfAdapters[index+1 :]		
		index = index +1
	return cleanList

f = open("advento2020/day10/input.txt", "r")
lines = f.readlines()
adaptersBag = []
for current in lines:
	parsedValue = int(current.strip())
	
	adaptersBag.append(parsedValue)	

sortedAdapters = sorted(adaptersBag)
cleanList  = getAllCombinations(sortedAdapters)

validCombination = 0;
for combination in cleanList:
	if validConfiguration(combination) :
		validCombination = validCombination +1

print(cleanList)
print(cleanList[:5])
print(len(cleanList))

print(validCombination)
