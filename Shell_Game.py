import sys
fin = open("shell.in", "r")
fout = open("shell.out", "w")

def getmax(start):
    pebble_pos = start
    point = 0
    
    #Easy switching algorithm
    for item in theList:
        if item[0] == pebble_pos:
            pebble_pos = item[1]
        elif item[1] == pebble_pos:
            pebble_pos = item[0]
        if pebble_pos == item[2]:
            point += 1
    return point
        
    
swapnum = int(fin.readline())
theList = [list(map(int, fin.readline().split())) for v in range(swapnum)]
max_score = 0

for i in range(1,4):
    max_score = max(getmax(i), max_score)
fout.write(str(max_score))

