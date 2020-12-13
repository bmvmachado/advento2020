from bagRule import BagRule

def nrOfBags(currentBag, listOfBags ):
	count = 0;
	for rule in currentBag.BagRules:	
		print(f"rule {rule} currentBag {currentBag.print()}")

		existentRules = [x for x in listOfBags if x.MainBag == rule] 
		if len(existentRules) > 0 :
			res = nrOfBags(existentRules[0],bagRules)
			count = count + currentBag.BagRules[rule] + currentBag.BagRules[rule]*res

	return count
 



f = open("..\input.txt", "r")
lines = f.readlines()

bagRules = []

searchBag = "shiny gold"
shinyGoldBagRule = {}
for current in lines:
	bagRule = BagRule(current)
	bagRules.append(bagRule)
	if bagRule.MainBag == searchBag :
		shinyGoldBagRule = bagRule



shinyGoldBagRule.print()
nrOcurrrences = 0
nrDistinct = 0
for rule in shinyGoldBagRule.BagRules :	
	print(f"rule '{rule}' shinyGoldBagRule : {shinyGoldBagRule.BagRules[rule]}")
	existentRules = [x for x in bagRules if x.MainBag == rule] 
	if len(existentRules) > 0 :
		res = nrOfBags(existentRules[0],bagRules)
		nrOcurrrences = nrOcurrrences + shinyGoldBagRule.BagRules[rule] + shinyGoldBagRule.BagRules[rule]*res
		if res > 0 :
			nrDistinct = nrDistinct +1

	
print(nrOcurrrences)
print(nrDistinct)
print(len(bagRules))