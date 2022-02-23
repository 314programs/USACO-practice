#Silver python doesn't work
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Spotty = [list(input()) for v in range(N)]
Plain = [list(input()) for v in range(N)]
Count = 0

I = [0 for v in range(64)]

def check(i1, j1, z1):
    v = True
    for i in range(N):
        I[Spotty[i][i1]*16+Spotty[i][j1]*4+Spotty[i][z1]] = 1
    for i in range(N):
        if I[Plain[i][i1]*16+Plain[i][j1]*4+Plain[i][z1]] == 1:
            v = False
    for i in range(N):
        I[Spotty[i][i1]*16+Spotty[i][j1]*4+Spotty[i][z1]] = 0
    return v

dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(N):
    for x in range(M):
        Spotty[i][x] = dict[Spotty[i][x]]
        Plain[i][x] = dict[Plain[i][x]]

for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            if check(i, j, k):
                Count += 1
print(Count)

