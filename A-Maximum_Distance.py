N = int(input())
X_List = list(map(int, input().split()))
Y_List = list(map(int, input().split()))

maximum = 0

for x in range(N):
    for y in range(N):
        #X > Y to avoid repetition
        if x > y:
            maximum = max((X_List[x] - X_List[y])**2 + (Y_List[x] - Y_List[y])**2, maximum)

print(maximum)
