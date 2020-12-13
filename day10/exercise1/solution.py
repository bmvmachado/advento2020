def getAdapterConfiguration(startVoltage, adapters):

	
	outputValue = startVoltage
	for adapterValue in adapters:
		searchValues = [adapterValue -1 , adapterValue -2, adapterValue -3]
		if startVoltage in searchValues:
			outputValue = adapterValue
			break
	
	return outputValue;

f = open("advento2020/day10/input.txt", "r")
lines = f.readlines()

adaptersBag = []
for current in lines:
	parsedValue = int(current.strip())
	
	adaptersBag.append(parsedValue)	
		
sortedAdapters = sorted(adaptersBag)

maxVoltage = sortedAdapters[len(sortedAdapters)-1]+3

index = 0
startVoltage = 0
singleDif = 0
tripleDif = 1 # My adapter
while index < len(sortedAdapters):
	result = getAdapterConfiguration(startVoltage,sortedAdapters[index:len(sortedAdapters)])

	if (result - startVoltage) > 1 :
		tripleDif = tripleDif + 1
	else :
		singleDif = singleDif + 1
	
	startVoltage = result
	index = index + 1


print(sortedAdapters)
print(f"maxVoltage:{maxVoltage} singleDif:{singleDif} tripleDif:{tripleDif}")
print(f"Result:{singleDif*tripleDif}")
