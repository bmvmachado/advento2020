class CodeInstruction:
    def __init__(self, instruction ):
        self.RawInstruction = instruction.strip()
        self.InstructionCode = {}
        self.Value = 0
        self.NumberExecutions = 0

        splittedInstruction = self.RawInstruction.split(' ')
        self.InstructionCode = splittedInstruction[0]
        self.Value = int(splittedInstruction[1].replace('+',''))

    def print(self):
        print(f"RawInstruction: '{self.RawInstruction}' InstructionCode: '{self.InstructionCode}' Value: '{self.Value}'")
