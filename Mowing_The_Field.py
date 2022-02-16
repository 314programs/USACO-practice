fin = open('mowing.in', 'r')
fout = open('mowing.out', 'w')

#Using pure brutal force because the data is very small
Movements = int(fin.readline())
Movement_List = [list(map(str, fin.readline().split())) for v in range(Movements)]
Graph = [[0,0]]
Current_x, Current_y = 0,0
Min_Time = float('inf')

#Bool for if there were cells revisited
Visited = False

for direction, distance in Movement_List:
    distance = int(distance)

    for i in range(distance):
        #Direction
        if direction == 'N': Current_y += 1
        if direction == 'W': Current_x += 1
        if direction == 'S': Current_y -= 1
        if direction == 'E': Current_x -= 1

        if [Current_x, Current_y] not in Graph:
            Graph.append([Current_x, Current_y])
            
        #Find nearest index from back
        #index() gets it from the front and we want minimum
        else:
            Visited = True
            Temp = 0
            for x in range(len(Graph)-1, -1, -1):
                if Graph[x] == [Current_x, Current_y]:
                    Temp = x
                    break

            Min_Time = min(Min_Time, len(Graph) - x)
            Graph.append([Current_x, Current_y])

if Visited:
    fout.write(str(Min_Time))
else:
    fout.write('-1')
