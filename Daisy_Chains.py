#USACO still not working...
Flower_num = int(input())
Flowers = list(map(int, input().split()))
average = 0

for start in range(Flower_num):
    for end in range(start, Flower_num):
        Temp = Flowers[start:end+1]
        if sum(Temp)/len(Temp) in Temp:
            average += 1

print(average)

