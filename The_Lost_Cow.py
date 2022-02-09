#Very inefficient code, might change later but not today because I am tired
fin = open('lostcow.in', 'r')
fout = open('lostcow.out', 'w')

farm_pos, cow_pos = map(int, fin.readline().split())
Found = False
time = 0
i = 0

def Move(power, direction):
    global time
    global Found
    movement = 2**power
    
    if direction == 'forward':
        current_pos = movement + farm_pos
        if current_pos >= cow_pos and cow_pos > farm_pos:
            Found = True
            time += cow_pos - farm_pos
        else:
            time += movement*2

    elif direction == 'backward':
        current_pos = - movement + farm_pos
        if current_pos <= cow_pos and cow_pos < farm_pos:
            Found = True
            time += farm_pos - cow_pos
        else:
            time += movement*2
    
while True:
    Move(i, 'forward')
    if Found:
        break
    Move(i+1, 'backward')
    if Found:
        break
    i += 2
    
fout.write(str(time))
