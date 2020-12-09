BirthYearDef ="byr" 
IssueYearDef = "iyr"
ExpirationYearDef = "eyr"
HeightDef = "hgt"
HairColorDef = "hcl"
EyeColorDef = "ecl"
PassportIdDef = "pid"
CountryIdDef = "cid"

class Passport:
    def __init__(self, details = []):
        self.BirthYearDef ="byr" 
        self.IssueYearDef = "iyr"
        self.ExpirationYearDef = "eyr"
        self.HeightDef = "hgt"
        self.HairColorDef = "hcl"
        self.EyeColorDef = "ecl"
        self.PassportIdDef = "pid"
        self.CountryIdDef = "cid"
        infoList = []

        self.BirthYear = BirthYearDef 
        self.IssueYear = IssueYearDef
        self.ExpirationYear = ExpirationYearDef
        self.Height = HeightDef
        self.HairColor = HairColorDef
        self.EyeColor = EyeColorDef 
        self.PassportID = PassportIdDef 
        self.CountryID = CountryIdDef 

        for currentDetail in details:
            splitted = currentDetail.split(' ')
            infoList = infoList + splitted

        for info in infoList :
            infoDetail = info.strip().split(':')

            if infoDetail[0] == self.BirthYearDef :
                self.BirthYear = infoDetail[1]        
            elif infoDetail[0] == self.IssueYearDef :
                self.IssueYear = infoDetail[1]        
            elif infoDetail[0] == self.ExpirationYearDef :
                self.ExpirationYear = infoDetail[1]        
            elif infoDetail[0] == self.HeightDef :
                self.Height = infoDetail[1]        
            elif infoDetail[0] == self.HairColorDef :
                self.HairColor = infoDetail[1]        
            elif infoDetail[0] == self.EyeColorDef :
                self.EyeColor = infoDetail[1]        
            elif infoDetail[0] == self.PassportIdDef :
                self.PassportID = infoDetail[1]        
            elif infoDetail[0] == self.CountryIdDef :
                self.CountryID = infoDetail[1]

    def print(self):
        print(f"BirthYear: {self.BirthYear} IssueYear: {self.IssueYear} ExpirationYear: {self.ExpirationYear} Height: {self.Height} HairColor: {self.HairColor} EyeColor: {self.EyeColor} PassportID: {self.PassportID} CountryID: {self.CountryID}")

    def wrong(self):
        return self.BirthYear == BirthYearDef or self.IssueYear == IssueYearDef or self.ExpirationYear == ExpirationYearDef or self.Height == HeightDef or self.HairColor == HairColorDef or self.EyeColor == EyeColorDef or self.PassportID == PassportIdDef #or self.CountryID == self.CountryIdDef