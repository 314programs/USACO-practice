#Struggled with this for no reason
#Why did the program not give me signs of printing other things other then the answer when I set it to print chr(i) and chr(j)...
from collections import deque
Cow_map = list(input())

Cow_Dict = {}
for i in range(65, 91):
    Cow_Dict[chr(i)] = [-1, -1]
Count = 0

for i in range(len(Cow_map)):
    if Cow_Dict[Cow_map[i]][0] == -1:
        Cow_Dict[Cow_map[i]][0] = i
    else:
        Cow_Dict[Cow_map[i]][1] = i


for i in range(65, 91):
    for j in range(65, 91):
        if j > i:
            if Cow_Dict[chr(i)][0] < Cow_Dict[chr(j)][0] < Cow_Dict[chr(i)][1] and not Cow_Dict[chr(i)][0] < Cow_Dict[chr(j)][1] < Cow_Dict[chr(i)][1]:
                Count += 1
            if Cow_Dict[chr(i)][0] < Cow_Dict[chr(j)][1] < Cow_Dict[chr(i)][1] and not Cow_Dict[chr(i)][0] < Cow_Dict[chr(j)][0] < Cow_Dict[chr(i)][1]:
                Count += 1
print(Count)
