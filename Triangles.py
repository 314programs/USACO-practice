#Very basic 3 for loop as data range is very small
coord_num = int(input())
coords = [list(map(int, input().split())) for v in range(coord_num)]

max_area = 0

for x in range(coord_num):
    for y in range(coord_num):
        for z in range(coord_num):
            if x != y and y != z and z != x:
                X = coords[x]
                Y = coords[y]
                Z = coords[z]
                if (X[0] == Y[0] and X[1] == Z[1]) or (X[1] == Y[1] and X[1] == Z[1]): 
                    if (X[0] == Y[0] and X[1] == Z[1]):
                        max_area = max(abs(X[1] - Y[1]) * abs(X[0] - Z[0]), max_area)
                    else:
                        max_area = max(abs(X[0] - Y[0]) * abs(X[1] - Z[1]), max_area)
                        
print(max_area)
