f = open("..\input.txt", "r")
lines = f.readlines()

validPass = 0
for currentPass in lines:
	inputs = currentPass.split(' ')
	
	#Reps
	repsSplitted = inputs[0].split('-')
	minRep = int(repsSplitted[0])
	maxRep = int(repsSplitted[1])

	#letter
	passLetter = inputs[1][:-1]

	#passToValidate
	passToValidate = inputs[2].strip()

	charOccurences = passToValidate.count(passLetter) 

	countMatches = 0

	if passToValidate[minRep-1] == passLetter :
		countMatches +=1

	if passToValidate[maxRep-1] == passLetter:
		countMatches +=1

	if countMatches == 1:
		validPass +=1
		continue
	else :
		print(f"currentPass : '{currentPass}' minRep : {minRep} maxRep : {minRep} passLetter : {passLetter} passToValidate : {passToValidate} ")
	
print(validPass)
