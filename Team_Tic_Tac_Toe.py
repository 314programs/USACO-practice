#Should read the questions properly next time...
#I got confused because I thought it was how many they can win instead of how many groups can win
import sys

fin = open('tttt.in', 'r')
fout = open('tttt.out', 'w')

Graph = [list(map(str, fin.readline())) for v in range(3)]
Individual = []
Group = []

def count_type(a,b,c):
    global Individual
    global Group

    Temp = set([a,b,c])
    Real_List = list(Temp)
    Real_List.sort()
    if len(Temp) == 1 and Real_List not in Individual: Individual.append(Real_List)
    elif len(Temp) == 2 and Real_List not in Group: Group.append(Real_List)


for i in range(3):
    count_type(Graph[i][0], Graph[i][1], Graph[i][2])
    count_type(Graph[0][i], Graph[1][i], Graph[2][i])

count_type(Graph[0][0], Graph[1][1], Graph[2][2])
count_type(Graph[0][2], Graph[1][1], Graph[2][0])

fout.write(str(len(Individual)) + '\n' + str(len(Group)))
