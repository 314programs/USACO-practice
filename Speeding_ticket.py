import sys
fin = open("speeding.in", "r")
fout = open("speeding.out", "w")

Road_segment_num, Bessie_segment_num = map(int, fin.readline().split())
Road_segment = [list(map(int, fin.readline().split())) for v in range(Road_segment_num)]
Bessie_segment = [list(map(int, fin.readline().split())) for v in range(Bessie_segment_num)]

max_speed = 0
SpeedList = [[0,0]for v in range(101)]

start_road = 0
for item in Road_segment:
    for i in range(start_road+1, item[0]+1 + start_road):
        SpeedList[i][0] = item[1]
    start_road += item[0]

start_bessie = 0
for item in Bessie_segment:
    for i in range(start_bessie+1, item[0]+1 + start_bessie):
        SpeedList[i][1] = item[1]
    start_bessie += item[0]

for item in SpeedList:
    max_speed = max(0, max_speed, item[1]-item[0])

fout.write(str(max_speed))
    
