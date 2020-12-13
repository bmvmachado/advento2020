import math
from groupAnswers import GroupAnswers

f = open("..\input.txt", "r")
lines = f.readlines()


groupAnswersStorage = []
groupAnswerDetails = []
totalDistinctYesAnswers = 0
for current in lines:
	if len(current.strip()) == 0 :
		p1 = GroupAnswers(groupAnswerDetails)
		groupAnswersStorage.append(p1)		
		groupAnswerDetails = []

		totalDistinctYesAnswers = totalDistinctYesAnswers + p1.TotalDistinctYesAnswers
		p1.print()
	else :
		groupAnswerDetails.append(current)

p1 = GroupAnswers(groupAnswerDetails)
groupAnswersStorage.append(p1)		
groupAnswerDetails = []

totalDistinctYesAnswers = totalDistinctYesAnswers + p1.TotalDistinctYesAnswers
p1.print()
        
		
print(totalDistinctYesAnswers)
print(len(groupAnswersStorage))