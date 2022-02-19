#I tried doing something else more complicated but it did not work out
#I should check the range of the question and calculate the time complexity well
import sys
fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w')


Cownum = int(fin.readline())
CowList = []
Current_Display = []
Current_Best = 7
Change = 0
CowDict = {}

for i in range(Cownum):
    day, name, change = map(str, fin.readline().split())
    Current_Display.append(name)
    if change[0] == '+':
        actual_change = int(change[1:])
    else:
        actual_change = -int(change[1:])
    CowList.append([int(day), name, actual_change])

    if name not in CowDict:
        CowDict[name] = 7

CowList.sort(key = lambda x: x[0])

for day, name, change in CowList:
    Current_Milk = CowDict[name] + change
    CowDict[name] = Current_Milk

    temp = sorted(CowDict.items(), key = lambda x: x[1], reverse = True)
    Temp_Display = []

    max_milk = temp[0][1]
    for name, milk in temp:
        if milk == max_milk:
            Temp_Display.append(name)
        else:
            break

    if Temp_Display != Current_Display:
        Change += 1
    Current_Display = Temp_Display


        
fout.write(str(Change))
