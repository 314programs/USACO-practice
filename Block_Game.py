#Program is very easy to do, but I just cannot understand what the questions mean
fin = open('blocks.in', 'r')
fout = open('blocks.out', 'w')

N = int(fin.readline())
WordList = []
Dictionary = {}

for i in range(97, 123):
    Dictionary[chr(i)] = 0

for i in range(N):
    Word_1, Word_2 = map(str, fin.readline().split())
    for i in range(97, 123):
        Dictionary[chr(i)] += max(Word_1.count(chr(i)), Word_2.count(chr(i)))

for i in range(97, 123):
    fout.write(str(Dictionary[chr(i)]) + '\n')
