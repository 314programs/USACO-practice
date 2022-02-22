#The question was confusing and I had to look at the solution
#I have to learn more ways to solve questions in USACO
Animal_num = int(input())
Animal_Dict = {}
AnimalList = []
Large = 0

for i in range(Animal_num):
    Temp = list(map(str, input().split()))
    AnimalList.append(Temp[0])
    Animal_Dict[Temp[0]] = list(set(Temp[2:]))
    

def find_same(a, b):
    Count = 0
    for x in a:
        for y in b:
            if x == y:
                Count += 1

    return int(Count)

for x in range(Animal_num):
    for y in range(Animal_num):
        if x != y:
            Large = max(find_same(Animal_Dict[AnimalList[x]], Animal_Dict[AnimalList[y]]), Large)

print(Large + 1)
