#Take in input
fin = open('cbarn.in', 'r')
fout = open('cbarn.out', 'w')

Room_num = int(fin.readline())
Cows_Needed = [int(fin.readline()) for v in range(Room_num)]
Cow_Total = sum(Cows_Needed)
min_distance = float('inf')

def calculate(index):
    global Cow_Total
    current_cow_num = Cow_Total
    Distance_traveled = 0
    
    #Travel in clockwise distance by using index
    while current_cow_num:
        current_cow_num -= Cows_Needed[index]
        #Update distance_traveled
        Distance_traveled += current_cow_num
        index += 1

        if index == Room_num:
            index = 0

    return Distance_traveled

#Can use bruteforce since n is small
for i in range(Room_num):
    min_distance = min(calculate(i), min_distance)
fout.write(str(min_distance))
