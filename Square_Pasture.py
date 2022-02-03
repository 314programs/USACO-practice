#Learning how to submit using File I/O method
import sys

fin = open("square.in", "r")
fout = open("square.out", "w")

Rect1 = list(map(int, fin.readline().split()))
Rect2 = list(map(int, fin.readline().split()))

minimumY = min(Rect1[1],Rect2[1])
maximumY = max(Rect1[3],Rect2[3])
minimumX = min(Rect1[0],Rect2[0])
maximumX = max(Rect1[2],Rect2[2])

Side = max(maximumY - minimumY, maximumX - minimumX)

fout.write(str(Side**2))
