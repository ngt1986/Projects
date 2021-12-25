# get dots
import heapq
import numpy as np
cave_system= np.zeros((500,500))
# cave_system= np.zeros(502,502)
cave = []

with open('day15_input.txt', 'r') as infile:
    for row in infile:
        row = row.strip('\n')
        cave_row = []
        for i in range(5):
            for digit in row:
                if int(digit)+i <=9:
                    cave_row.append(int(digit)+i)
                else:
                    cave_row.append((int(digit)+i)%9)
        cave.append(cave_row)
    # print(cave)

for i in range(len(cave)):
    for j in range(len(cave[0])):
        cave_system[i][j] = cave[i][j]
# print(cave_system)

for i in range(100):
    for j in range(len(cave[0])):
        if cave[i][j] + 1 <= 9:
            cave_system[100+i][j] = cave[i][j]+1
        else:
            cave_system[100+i][j] = (cave[i][j]+1)%9
for i in range(100,200):
    for j in range(len(cave[0])):
        if cave_system[i][j] + 1 <= 9:
            cave_system[100+i][j] = cave_system[i][j]+1
        else:
            cave_system[100+i][j] = (cave_system[i][j]+1)%9
for i in range(200,300):
    for j in range(len(cave[0])):
        if cave_system[i][j] + 1 <= 9:
            cave_system[100+i][j] = cave_system[i][j]+1
        else:
            cave_system[100+i][j] = (cave_system[i][j]+1)%9
for i in range(300,400):
    for j in range(len(cave[0])):
        if cave_system[i][j] + 1 <= 9:
            cave_system[100+i][j] = cave_system[i][j]+1
        else:
            cave_system[100+i][j] = (cave_system[i][j]+1)%9
# print(cave_system)


def neighbors(cave, curr):
    neighbors = []  # (risk, (i, j))
    if curr[0]-1 >0:
        neighbors.append((cave[curr[0]-1][curr[1]],(curr[0]-1,curr[1])))
    if curr[0]+1 < len(cave):
        neighbors.append((cave[curr[0]+1][curr[1]],(curr[0]+1,curr[1])))
    if curr[1]-1 > 0:
        neighbors.append((cave[curr[0]][curr[1]-1],(curr[0],curr[1]-1)))
    if curr[1]+1 < len(cave[0]):
        neighbors.append((cave[curr[0]][curr[1]+1],(curr[0],curr[1]+1)))
    return neighbors

def get_visited(cave, curr = None):
    if curr is None:
        curr = (0,(0, 0))

    #start at cave(1,1) and don't consider risk
    priority_queue = []
    heapq.heappush(priority_queue, curr)

    risk_matrix = np.zeros((len(cave_system),len(cave_system[0])))
    for i in range(len(cave_system)):
        for j in range(len(cave_system[0])):
            risk_matrix[i][j] = float('inf')
    risk_matrix[0][0] = 0
    # print(risk_matrix)

    visited = []
    while priority_queue:
        curr = heapq.heappop(priority_queue)
        if curr[1] not in visited:
            visited.append(curr[1])
        for neighbor in neighbors(cave_system, curr[1]):
            if neighbor[0] + risk_matrix[curr[1][0]][curr[1][1]] < risk_matrix[neighbor[1][0]][neighbor[1][1]]:
                risk_matrix[neighbor[1][0]][neighbor[1][1]] = neighbor[0] + risk_matrix[curr[1][0]][curr[1][1]]
            if neighbor[1] not in visited:
                visited.append(neighbor[1])
                heapq.heappush(priority_queue,(curr[0]+neighbor[0],(neighbor[1][0],neighbor[1][1])))
        print(len(priority_queue))
        # print(risk_matrix)
    # print(visited)
    return risk_matrix
min_risk_visited = get_visited(cave)
print(min_risk_visited)