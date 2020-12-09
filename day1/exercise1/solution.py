f = open("..\input.txt", "r")
lines = f.readlines()

first = 0
while first < len(lines):  
    second = 0
    while second < len(lines):              
        if first != second :
            third = 0
            while third < len(lines):              
                if second != third:
                    if (int(lines[first]) + int(lines[second])+ int(lines[third])) == 2020:  
                        print(f"{lines[first]} + {lines[second]} + {lines[third]}")            
                        print(int(lines[first]) * int(lines[second])* int(lines[third]))            
                third += 1            
        second += 1
    first += 1
    