class GroupAnswers:
    def __init__(self, answers = []):
        self.PersonsInGroup = len(answers)
        self.YesAnswers = {}
        self.TotalYesAnswers = 0
        self.TotalDistinctYesAnswers = 0

        for currentAnswer in answers:
            
            for answer in currentAnswer.strip()[0:len(currentAnswer.strip())] :
                strippedAnswer = answer.strip()
                if not strippedAnswer in self.YesAnswers :
                    self.YesAnswers[strippedAnswer] = 0 
                    self.TotalDistinctYesAnswers = self.TotalDistinctYesAnswers + 1
                
                self.YesAnswers[strippedAnswer] = self.YesAnswers[strippedAnswer] + 1 

                self.TotalYesAnswers =  self.TotalYesAnswers +1

    def print(self):
        print(f"PersonsInGroup: {self.PersonsInGroup} YesAnswers: {self.YesAnswers} TotalYesAnswers: {self.TotalYesAnswers}")
 