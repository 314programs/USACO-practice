N, M = map(int, input().split())
Spotty = [list(input()) for v in range(N)]
Normal = [list(input()) for v in range(N)]

same_gene = []
same_gene_normal = []
gene = M

for i in range(M):
    Temp = []
    for x in range(N):
        Temp.append(Spotty[x][i])
    same_gene.append(Temp)

for i in range(M):
    Temp = []
    for x in range(N):
        Temp.append(Normal[x][i])
    same_gene_normal.append(Temp)


for i in range(M):
    item = same_gene[i]
    for x in item:
        if x in same_gene_normal[i]:
            gene -= 1
            break

print(gene)
