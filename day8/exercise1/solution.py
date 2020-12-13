def executeProgram(codeInstructionsBag):
	accumulatorValue = 0;
	index = 0

	currentExecution = codeInstructionsBag[index]
	
	while currentExecution.NumberExecutions == 0 :
		if currentExecution.InstructionCode == "acc" :
			accumulatorValue = accumulatorValue + currentExecution.Value
			index = index + 1
		elif currentExecution.InstructionCode == "jmp" :
			index = index + currentExecution.Value
		elif currentExecution.InstructionCode == "nop" :
			index = index + 1
		currentExecution.NumberExecutions = 1
		currentExecution.print()
		print(accumulatorValue)
		
		currentExecution = codeInstructionsBag[index]

	return accumulatorValue;


from codeInstruction import CodeInstruction

f = open("..\input.txt", "r")
lines = f.readlines()

codeInstructionsBag = []

for current in lines:
	codeInstruction = CodeInstruction(current)
	codeInstructionsBag.append(codeInstruction)

accumulator = executeProgram(codeInstructionsBag)

print(accumulator)
print(len(codeInstructionsBag))