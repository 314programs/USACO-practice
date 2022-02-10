import sys

fin = open('shuffle.in', 'r')
fout = open('shuffle.out', 'w')

#I got confused with initial and final shuffle values
Row_num = int(fin.readline())
Cow_order = list(map(int, fin.readline().split()))
Cows = list(map(int, fin.readline().split()))

#Reverse shuffle
for i in range(3):
    temp = [0]*Row_num
    for i in range(Row_num):
        temp[i] = Cows[Cow_order[i]-1]
    Cows = temp

#Print
for item in Cows:
    fout.write(str(item))
    fout.write('\n')
