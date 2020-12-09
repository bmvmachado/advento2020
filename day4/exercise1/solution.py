from passport import Passport

f = open("..\input.txt", "r")
lines = f.readlines()

passportStorage = []
passportDetails = []

valid = 0
for currentPass in lines:
	print(currentPass)
	if len(currentPass) == 1 :
		p1 = Passport(passportDetails)
		passportStorage.append(p1)
		
		passportDetails = []

		if p1.wrong() :
			p1.print()
		else :
			valid += 1;
	else :
		passportDetails.append(currentPass)

#last one
if len(passportDetails)>0:
	p1 = Passport(passportDetails)
	passportStorage.append(p1)

	if not p1.wrong() :
		p1.print()
	else :
		valid += 1;

print(len(passportDetails))
print(valid)