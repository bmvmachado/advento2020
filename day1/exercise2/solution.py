f = open("..\input.txt", "r")
lines = f.readlines()

first = 0
while first < len(lines):  
    second = 0
    while second < len(lines):              
        if first != second :
            if (int(lines[first]) + int(lines[second])) == 2020:  
                print(f"{lines[first]} + {lines[second]}")            
                print(int(lines[first]) * int(lines[second]))
            
        second += 1
    first += 1
    