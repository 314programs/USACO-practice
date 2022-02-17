import sys
fin = open('censor.in', 'r')
fout = open('censor.out', 'w')

Word = fin.readline().strip()
Censor = fin.readline().strip()
Stack = ''

for i in range(len(Word)):
    Stack += Word[i]
    if Word[i] == Censor[-1] and Stack[-len(Censor):] == Censor:
        Stack = Stack[:-len(Censor)]

fout.write(Stack)
