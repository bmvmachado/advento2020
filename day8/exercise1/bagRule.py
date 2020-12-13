class BagRule:
    def __init__(self, rule ):
        self.BagRules = {}
        rule = rule.replace("bags", "").replace("bag", "")
        firstRuleSplitted = rule.split(" contain ");
        self.MainBag = firstRuleSplitted[0].strip()
        remainingRuleSplitted = firstRuleSplitted[1].split(", ");
        
        #plaid orange bags contain 2 vibrant bronze bags, 3 pale silver bags, 1 shiny blue bag, 3 plaid maroon bags.
        for current in remainingRuleSplitted:
            strippedValue = current.strip()
            firstSpaceIndex = int(strippedValue.index(' '))
            ocurrences = strippedValue[0:firstSpaceIndex]
            self.BagRules[strippedValue[firstSpaceIndex:len(strippedValue)].replace('.','').strip()] = ocurrences    

    def print(self):
        print(f"MainBag: {self.MainBag} BagRules: {self.BagRules}")
