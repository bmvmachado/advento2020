import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def readRegionSeat(seatRegionCode, lowerHalfCode, lowerBoundary, higherBoundary):
    
    regionRange = higherBoundary - lowerBoundary + 1;

    roundRegionRange = round_up(regionRange/2)

    print(f" {seatRegionCode} regionRange: {regionRange} roundRegionRange: {roundRegionRange}")

    if seatRegionCode == lowerHalfCode :
        return lowerBoundary, lowerBoundary + roundRegionRange+ -1
    else :
        return lowerBoundary + roundRegionRange, higherBoundary


f = open("..\input.txt", "r")
lines = f.readlines()

highestSeatID = 0;

for currentPass in lines:
    rowLowerBoundary = 0;
    rowHigherBoundary = 127;
    print(currentPass)
    for seatRegion in currentPass[0:7]:
        regionReturn = readRegionSeat(seatRegion,"F",rowLowerBoundary,rowHigherBoundary)
        rowLowerBoundary = regionReturn[0]
        rowHigherBoundary = regionReturn[1]
        print(f" {seatRegion} from {rowLowerBoundary} to {rowHigherBoundary}")

    columnLowerBoundary = 0;
    columnHigherBoundary = 7;
    for seatNumber in currentPass[7:len(currentPass)]:
        regionReturn = readRegionSeat(seatNumber,"L",columnLowerBoundary,columnHigherBoundary)
        columnLowerBoundary = regionReturn[0]
        columnHigherBoundary = regionReturn[1]
        print(f" {seatRegion} from {columnLowerBoundary} to {columnHigherBoundary}")

    seatId = rowHigherBoundary * 8 + columnHigherBoundary

    if seatId > highestSeatID :
        highestSeatID = seatId
        

print(len(lines))
print(highestSeatID)