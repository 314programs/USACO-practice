import sys
fin = open("mixmilk.in", "r")
fout = open("mixmilk.out", "w")

#Pouring algorithm
def pour(bucket1, bucket2):
    #Pour into bucket 2
    bucket2[1] += bucket1[1]
    bucket1[1] = 0
    
    #If it is overflowing, remove the amount that overflowed and put it back
    if bucket2[1] > bucket2[0]:
        bucket1[1] = bucket2[1] - bucket2[0]
        bucket2[1] = bucket2[0]

Bucket_list = [list(map(int, fin.readline().split())) for v in range(3)]

#Repeat 3 mixes for 33
for i in range(33):
    pour(Bucket_list[0], Bucket_list[1])
    pour(Bucket_list[1], Bucket_list[2])
    pour(Bucket_list[2], Bucket_list[0])

#One last time need before it hits 100 mixes
pour(Bucket_list[0], Bucket_list[1])

fout.write(str(Bucket_list[0][1]) + '\n')
fout.write(str(Bucket_list[1][1]) + '\n')
fout.write(str(Bucket_list[2][1]) + '\n')
