from passport import Passport

f = open("..\input.txt", "r")
lines = f.readlines()

passportStorage = []
passportDetails = []

valid = 0
for currentPass in lines:
	if len(currentPass) == 1 :
		p1 = Passport(passportDetails)
		passportStorage.append(p1)
		
		passportDetails = []

		if not p1.wrong() :
			valid += 1;
	else :
		passportDetails.append(currentPass)

#last one
if len(passportDetails)>0:
	p1 = Passport(passportDetails)
	passportStorage.append(p1)

	if not p1.wrong() :
		valid += 1;

print(len(passportDetails))
print(valid)