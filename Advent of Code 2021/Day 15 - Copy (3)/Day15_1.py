# get dots
import heapq
import numpy as np
cave = []
with open('day15_input.txt', 'r') as infile:
    for row in infile:
        row = row.strip('\n')
        cave_row = []
        for digit in row:
            cave_row.append(int(digit))
        cave_row.insert(0,10)
        cave_row.append(10)
        cave.append(cave_row)

length = len(cave[0])
cave.insert(0,[10]*length)
cave.append([10]*length)
print(cave)

def neighbors(cave, curr):
    neighbors = []  # (risk, (i, j))
    if cave[curr[0]-1][curr[1]] != 10:
        neighbors.append((cave[curr[0]-1][curr[1]],(curr[0]-1,curr[1])))
    if cave[curr[0]+1][curr[1]] != 10:
        neighbors.append((cave[curr[0]+1][curr[1]],(curr[0]+1,curr[1])))
    if cave[curr[0]][curr[1]-1] != 10:
        neighbors.append((cave[curr[0]][curr[1]-1],(curr[0],curr[1]-1)))
    if cave[curr[0]][curr[1]+1] != 10:
        neighbors.append((cave[curr[0]][curr[1]+1],(curr[0],curr[1]+1)))
    return neighbors

def get_visited(cave, curr = None):
    if curr is None:
        curr = (0,(1, 1))

    #start at cave(1,1) and don't consider risk
    priority_queue = []
    heapq.heappush(priority_queue, curr)

    risk_matrix = np.zeros((len(cave),len(cave[0])))
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            risk_matrix[i][j] = float('inf')
    risk_matrix[1][1] = 0
    # print(risk_matrix)

    visited = []
    while priority_queue:
        curr = heapq.heappop(priority_queue)
        if curr[1] not in visited:
            visited.append(curr[1])
        for neighbor in neighbors(cave, curr[1]):
            if neighbor[0] + risk_matrix[curr[1][0]][curr[1][1]] < risk_matrix[neighbor[1][0]][neighbor[1][1]]:
                risk_matrix[neighbor[1][0]][neighbor[1][1]] = neighbor[0] + risk_matrix[curr[1][0]][curr[1][1]]
            if neighbor[1] not in visited:
                visited.append(neighbor[1])
                heapq.heappush(priority_queue,(curr[0]+neighbor[0],(neighbor[1][0],neighbor[1][1])))
        # print(len(priority_queue))
        # print(risk_matrix)
    # print(visited)
    return risk_matrix
min_risk_visited = get_visited(cave)
print(min_risk_visited)