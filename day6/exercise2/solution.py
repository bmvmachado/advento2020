import math
from groupAnswers import GroupAnswers

f = open("..\input.txt", "r")
lines = f.readlines()


groupAnswersStorage = []
groupAnswerDetails = []
allAnsweredTheSame = 0
for current in lines:
	if len(current.strip()) == 0 :
		p1 = GroupAnswers(groupAnswerDetails)
		groupAnswersStorage.append(p1)		
		groupAnswerDetails = []
		allAnsweredTheSame = allAnsweredTheSame + p1.countAllAnsweredTheSame()
	else :
		groupAnswerDetails.append(current)

p1 = GroupAnswers(groupAnswerDetails)
groupAnswersStorage.append(p1)		
groupAnswerDetails = []

allAnsweredTheSame = allAnsweredTheSame + p1.countAllAnsweredTheSame()

print(allAnsweredTheSame)
print(len(groupAnswersStorage))