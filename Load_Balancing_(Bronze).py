#Very difficult in my opinion when which algorithm to use is given
#Its more similar to ad hoc at this point
CowNum, Dimension = map(int, input().split())
Cows = [list(map(int, input().split())) for v in range(CowNum)]
Min_Count = float('inf')

def Check(Border_Y, Border_X):
    Right_Up, Right_Down, Left_Down, Left_Up = 0,0,0,0
    for Y, X in Cows:
        if Y > Border_Y and X > Border_X:
            Right_Up += 1
        if Y < Border_Y and X > Border_X:
            Right_Down += 1
        if Y < Border_Y and X < Border_X:
            Left_Down += 1
        if Y > Border_Y and X < Border_X:
            Left_Up += 1

    return max(Right_Up, Right_Down, Left_Down, Left_Up)

for y in range(CowNum):
    for x in range(CowNum):
        Min_Count = min(Check(Cows[y][0] + 1, Cows[x][1] + 1), Min_Count)
print(Min_Count)

