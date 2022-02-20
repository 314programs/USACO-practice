#Very bruteforce solution but optimised
fin = open('pails.in', 'r')
fout = open('pails.out', 'w')

S, M, L = map(int, fin.readline().split())
maximum = 0

for i in range((L//S)+1):
    Temp = (L - i*S)//M
    maximum = max(maximum, i*S + Temp*M)

fout.write(str(maximum))
