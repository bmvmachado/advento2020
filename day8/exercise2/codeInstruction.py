class CodeInstruction:
    def __init__(self, instruction, number ):
        self.RawInstruction = instruction.strip()
        self.InstructionCode = {}
        self.Value = 0
        self.NumberExecutions = 0        
        self.Number = number

        splittedInstruction = self.RawInstruction.split(' ')
        self.InstructionCode = splittedInstruction[0]
        self.Value = int(splittedInstruction[1].replace('+',''))

    def print(self):
        print(f"RawInstruction: '{self.RawInstruction}' Number: '{self.Number}' InstructionCode: '{self.InstructionCode}' Value: '{self.Value}' NumberExecutions: '{self.NumberExecutions}'")
