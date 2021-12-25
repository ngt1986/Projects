# get lines
import numpy as np
dumbos = np.zeros((12,12))
dumbos+=11
with open('day11_input.txt', 'r') as infile:
    dumbos_row=1
    for row in infile:
        row = row.strip('\n')
        for i in range(1,len(row)+1):
            dumbos[dumbos_row][i] = int(row[i-1])
        dumbos_row += 1

# for dumbo in dumbos:
#     print(dumbo)

def flash(dumbos, dumbo, flash_count, visited):
    for i in range(dumbo[0]-1,dumbo[0]+2):
        for j in range(dumbo[1]-1,dumbo[1]+2):
            if (i,j) not in visited:
                if i != dumbo[0] or j != dumbo[1]:
                    if dumbos[i][j] < 9:
                        dumbos[i][j] +=1
                    elif dumbos[i][j] == 9:
                        dumbos[i][j] +=1
                        visited.append((i,j))
                        flash_count = flash(dumbos, (i,j), flash_count+1, visited)
                    elif dumbos[i][j] == 10:
                        dumbos[i][j] == 10
    return flash_count
steps = 0
flash_count = 0
visited = []
all_flashing = False
# while steps < 101:
while all_flashing == False:
    dumbos+=1
    for i in range(1,len(dumbos)-1):
        for j in range(1, len(dumbos)-1):
            if dumbos[i][j] == 10 and (i,j) not in visited:
                visited.append((i,j))
                flash_count = flash(dumbos, (i,j), flash_count+1, visited)
    all_flashing = True
    for i in range(1, len(dumbos) - 1):
        for j in range(1, len(dumbos) - 1):
            if dumbos[i][j] == 10:
                dumbos[i][j] = 0
            else:
                all_flashing = False
    steps +=1
    visited = []
    for dumbo in dumbos:
        print(dumbo)
print(steps)