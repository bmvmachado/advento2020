import os
from codeInstruction import CodeInstruction

def executeProgram(codeInstructionsBag, instNumberToAnalyse, alreadyChangedIndexes):
	accumulatorValue = 0;
	index = 0
	currentExecution = codeInstructionsBag[index]
	newInstruction = False
	breakExecution = False
	errorExecution = True

	for b in codeInstructionsBag:
		b.NumberExecutions = 0


	while not breakExecution:
		instructionCode = currentExecution.InstructionCode
		if instNumberToAnalyse == currentExecution.Number :		
			if instructionCode == "jmp" :
				instructionCode = "nop"
			else :
				instructionCode = "jmp"
			

		if instructionCode == "acc" :
			accumulatorValue = accumulatorValue + currentExecution.Value
			index = index + 1
		elif instructionCode == "jmp" :
			index = index + currentExecution.Value
			if not newInstruction and instNumberToAnalyse != currentExecution.Number and currentExecution.Number not in alreadyChangedIndexes :
				instNumberToAnalyse = currentExecution.Number
				newInstruction = True
		elif instructionCode == "nop" :
			index = index + 1
			if not newInstruction and instNumberToAnalyse != currentExecution.Number  and currentExecution.Number not in alreadyChangedIndexes:
				instNumberToAnalyse = currentExecution.Number
				newInstruction = True
		
		if index >= len(codeInstructionsBag) :
			breakExecution = True
			errorExecution = False
		else :		
			currentExecution.NumberExecutions = 1				
			currentExecution.print()
			currentExecution = codeInstructionsBag[index]
			breakExecution = currentExecution.NumberExecutions > 0	
			print(breakExecution)


	return (accumulatorValue , instNumberToAnalyse, errorExecution) ;



print(os.getcwd())
f = open("advento2020/day8/input.txt", "r")
lines = f.readlines()


codeInstructionsBag = []
number = 1;
for current in lines:
	codeInstruction = CodeInstruction(current, number)
	codeInstructionsBag.append(codeInstruction)
	number = number + 1
	codeInstruction.print()
	
alreadyChangedIndexes = []
result = executeProgram(codeInstructionsBag,-1,alreadyChangedIndexes )
index = result[1]
while result[2] :	
	result = executeProgram(codeInstructionsBag,index, alreadyChangedIndexes)
	alreadyChangedIndexes.append(index)
	if result[1] == index :
		index = result[1] + 1
	else :
		index = result[1]


print(result)
print(len(codeInstructionsBag))