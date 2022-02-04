#Take input as a form of list
White = list(map(int, input().split()))
Black1 = list(map(int, input().split()))
Black2 = list(map(int, input().split()))
 
#Function which calculates area of the intersection
def intersect(rect1, rect2):
    x_intersect = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_intersect = max(0, min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]))
    return x_intersect*y_intersect

#Find area of white plate
Area = (White[2] - White[0])*(White[3] - White[1])

#Find intersecting area between black and white plates
Intersect1 = intersect(White, Black1) 
Intersect2 = intersect(White, Black2) 

#Find overlapping point between black plates
Black_inter = max(Black1[0], Black2[0]), max(Black1[1], Black2[1]), min(Black1[2], Black2[2]), min(Black1[3], Black2[3]) 
#Using the overlapping points of black plates, use that to calculate overlapping areas of blac plates in white plate
Intersect_black = intersect(White, Black_inter)

#Subtract black and white plate intersecting
#Also remove black overlaps inside the white plate intersection
Area -= Intersect1 + Intersect2 - Intersect_black

#If area is below zero, it means it is completely covered
if Area <= 0:
    print('NO')
else:
    print('YES')
