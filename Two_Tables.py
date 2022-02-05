Testcase = int(input())

for x in range(Testcase):
    Room_X, Room_Y = map(int, input().split())
    Table = list(map(int, input().split()))
    SizeX, SizeY = map(int, input().split())
    TableSizeX, TableSizeY = (Table[2]-Table[0]), (Table[3]-Table[1])

    if TableSizeX + SizeX > Room_X and SizeY + TableSizeY > Room_Y:
        print('-1')

    else:
      #Can put table either in the top of the table, bottom of the table and left and right side of the table
        Up, Down, Left, Right = float('inf'), float('inf'), float('inf'), float('inf')
        
        #Similar logic for loops, if the original table placement can already fit the new table, set direction distance to 0
        #If not, calculate how much distance needs to be moved and check if that distance is moved, it exceeds the wall rooms or not
        if Table[3] <= Room_Y - SizeY:
            Up = 0
        elif Table[1] + ((Room_Y - SizeY) - Table[3]) >= 0:
            Up = Table[3] - (Room_Y - SizeY)
            
        if Table[1] >= SizeY:
            Down = 0
        elif Table[3] + SizeY-Table[1] <= Room_Y:
            Down = SizeY-Table[1]
            
        if Table[0] >= SizeX:
            Left = 0
        elif Table[2] + SizeX-Table[0] <= Room_X:
            Left = SizeX-Table[0]
            
        if Table[2] <= Room_X - SizeX:
            Right = 0
        elif Table[0] + ((Room_X - SizeX) - Table[2]) >= 0:
            Right = Table[2] - (Room_X - SizeX)

        #Print the smallest distance
        Distance = min(Up, Down, Left, Right)
        print('{0:.9f}'.format(Distance))
