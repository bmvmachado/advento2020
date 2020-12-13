from bagRule import BagRule

def canCarryBag(searchBag , currentBag, listOfBags ):
	nrOccurrences = 0;
	for current in currentBag.BagRules:	
		print(f"searchBag '{searchBag}' current '{current}' currentBag.MainBag '{currentBag.MainBag}'")
		if searchBag == current :		
			print(f"current {current} currentBag.MainBag {currentBag.MainBag}")
			nrOccurrences = nrOccurrences + 1
		else :
			existentRules = [x for x in listOfBags if x.MainBag == current] 
			if len(existentRules) > 0 :
				nrOccurrences = nrOccurrences + canCarryBag(searchBag ,existentRules[0],listOfBags)

	return nrOccurrences
 



f = open("..\input.txt", "r")
lines = f.readlines()

bagRules = []

searchBag = "shiny gold"
for current in lines:
	bagRule = BagRule(current)
	bagRules.append(bagRule)

nrOcurrrences = 0
nrDistinct = 0
for rule in bagRules :
	res = canCarryBag(searchBag ,rule,bagRules)
	nrOcurrrences = nrOcurrrences + res
	if res > 0 :
		nrDistinct = nrDistinct +1

	
print(nrOcurrrences)
print(nrDistinct)
print(len(bagRules))