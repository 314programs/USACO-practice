#Relatively new to geometry
import sys

fin = open("billboard.in", "r")
fout = open("billboard.out", "w")
BillBoard1 = list(map(int, fin.readline().split()))
BillBoard2 = list(map(int, fin.readline().split()))
Truck = list(map(int, fin.readline().split()))

Area = 0
Area += (BillBoard1[2] - BillBoard1[0]) * (BillBoard1[3] - BillBoard1[1])
Area += (BillBoard2[2] - BillBoard2[0]) * (BillBoard2[3] - BillBoard2[1])

def intersect(rect1, rect2):
    x_overlap = max(0,min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0,min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]))
    return(x_overlap * y_overlap)
    
fout.write(str(Area - intersect(BillBoard1, Truck) - intersect(BillBoard2, Truck)))
    
