fin = open('blist.in', 'r')
fout = open('blist.out', 'w')

Cow_Num = int(fin.readline())
Cow_List = [list(map(int, fin.readline().split())) for v in range(Cow_Num)]

Cow_List.sort(key = lambda x: x[1])
#Get ending time
Ending_Time = Cow_List[-1][1]
Cow_List.sort(key = lambda x: x[0])

Timing = [0 for v in range(Ending_Time+1)]

#See how bucket usage time overlaps
for i in range(Cow_Num):
    Current_Cow = Cow_List[i]
    for x in range(Current_Cow[0], Current_Cow[1]):
        Timing[x] += Current_Cow[2]

#Get max bucket number from overlaps
fout.write(str(max(Timing)))
