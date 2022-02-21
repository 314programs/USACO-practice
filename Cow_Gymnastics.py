Session_num, Cow_num = map(int, input().split())
Session_ranking = [list(map(int, input().split())) for v in range(Session_num)]
Consistence = 0

def better(a, b):
    for rank in Session_ranking:
        if rank.index(a) < rank.index(b):
            return False
    return True

for i in range(1, Cow_num+1):
    for j in range(1, Cow_num+1):
        if i != j:
            if better(i, j): 
                Consistence += 1
print(Consistence)
