import sys
fin = open("cowsignal.in", "r")
fout = open("cowsignal.out", "w")

Height, Width, Multiply = map(int, fin.readline().split())
Symbol = [list(map(str, fin.readline())) for v in range(Height)]

for item in Symbol:
    multi_x = ''
    for char in item:
        multi_x += char * Multiply

    #This didn't work for reason at first time
    #So i used strip() with new line
    for x in range(Multiply):
        fout.write(str(multi_x).strip() + '\n')

