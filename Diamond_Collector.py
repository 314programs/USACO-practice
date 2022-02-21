#USACO submitting system decided not to work today, so I had to go to baekjoon to submit my code
#Why did I have trouble over this simple question.
import sys

fin = sys.stdin
fout = sys.stdout

Diamond, max_size = map(int, fin.readline().split())
Diamond_List = [int(fin.readline()) for v in range(Diamond)]
Display = 0
Diamond_List.sort()

for y in range(Diamond):
    Temp = 0
    for x in range(Diamond):
        if x >= y and Diamond_List[x] - Diamond_List[y] <= max_size:
            Temp += 1
    Display = max(Display, Temp)
fout.write(str(Display))
