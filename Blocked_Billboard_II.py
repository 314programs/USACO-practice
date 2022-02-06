import sys
fin = open("billboard.in", "r")
fout = open("billboard.out", "w")

LawnMower = list(map(int, fin.readline().split()))
CowFeed = list(map(int, fin.readline().split()))

#Find intersection points
x1,y1,x2,y2 = max(LawnMower[0], CowFeed[0]), max(LawnMower[1], CowFeed[1]), min(LawnMower[2], CowFeed[2]), min(LawnMower[3], CowFeed[3])

#Find area of lawnmower billboard
LawnMowerArea = abs(LawnMower[3] - LawnMower[1]) * abs(LawnMower[2] - LawnMower[0])
#Find area of intersection
Cowfeed_inter = abs(y2 - y1) * abs(x2 - x1)

if y2 - y1 < LawnMower[3] - LawnMower[1] and x2 - x1 < LawnMower[2] - LawnMower[0]:
  #If they do not cross or cross but does not make a rectangular shape
    fout.write(str(LawnMowerArea))
elif y2 - y1 >= LawnMower[3] - LawnMower[1] or x2 - x1 <= LawnMower[2] - LawnMower[0]:
  #If they cross to a rectangular shape that can be covered in 1 rectangle
    if (x1 == LawnMower[0] and y1 == LawnMower[1]) or (x2 == LawnMower[2] and y2 == LawnMower[3]):
        fout.write(str(LawnMowerArea - Cowfeed_inter))
    else:
        fout.write(str(LawnMowerArea))
#Complete cover
else:
    fout.write("0")
