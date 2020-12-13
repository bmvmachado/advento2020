def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


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
            
            value = intTryParse(ocurrences)
            parsedValue = 0
            if value[1] :
                parsedValue = value[0]
                
            self.BagRules[strippedValue[firstSpaceIndex:len(strippedValue)].replace('.','').strip()] = parsedValue

    def print(self):
        print(f"MainBag: {self.MainBag} BagRules: {self.BagRules}")
