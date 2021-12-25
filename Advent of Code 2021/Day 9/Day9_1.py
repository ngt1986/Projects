# get lines
tubes = []
# with open('day9_input_sample.txt', 'r') as infile:
#     for row in infile:
#         row = list(row.strip('\n'))
#         for i in range(len(row)):
#             row[i] = int(row[i])
#         tubes.append(row)
# print(tubes)
with open('day9_input.txt', 'r') as infile:
    for row in infile:
        row = list(row.strip('\n'))
        for i in range(len(row)):
            row[i] = int(row[i])
        tubes.append(row)
print(tubes)

def neighbors(tubes, x, y):
    #corners
    neighbor_nodes = ()
    if x == 0 and y == 0:
        neighbor_nodes = (tubes[x+1][y], tubes[x][y+1], 10, 10)
        return neighbor_nodes
    elif x == 0 and y == len(tubes[0])-1:
        neighbor_nodes = (tubes[x + 1][y], tubes[x][y - 1], 10, 10)
        return neighbor_nodes
    elif x == len(tubes)-1 and y == 0:
        neighbor_nodes = (tubes[x - 1][y], tubes[x][y + 1], 10, 10)
        return neighbor_nodes
    elif x == len(tubes)-1 and y == len(tubes[0])-1:
        neighbor_nodes = (tubes[x - 1][y], tubes[x][y - 1], 10, 10)
        return neighbor_nodes

    elif x > 0 and x < len(tubes)-1:
        if y > 0 and y < len(tubes[0])-1:
            neighbor_nodes = (tubes[x-1][y], tubes[x+1][y], tubes[x][y+1], tubes[x][y-1])
            return neighbor_nodes

        elif y == 0:
            neighbor_nodes = (tubes[x-1][y], tubes[x+1][y], tubes[x][y+1], 10)
            return neighbor_nodes
        elif y == len(tubes[0])-1:
            neighbor_nodes =(tubes[x - 1][y], tubes[x + 1][y], tubes[x][y - 1], 10)
            return neighbor_nodes
    elif y > 0 and y < len(tubes[0])-1:
        if x > 0 and x < len(tubes)-1:
            neighbor_nodes = (tubes[x - 1][y], tubes[x + 1][y], tubes[x][y + 1], tubes[x][y - 1])
            return neighbor_nodes

        elif x == 0:
            neighbor_nodes = (tubes[x][y+1], tubes[x + 1][y], tubes[x][y - 1], 10)
            return neighbor_nodes
        elif x == len(tubes) - 1:
            neighbor_nodes = (tubes[x - 1][y], tubes[x][y+1], tubes[x][y - 1], 10)
    return neighbor_nodes

low_points = []
for i in range(len(tubes)):
    for j in range(len(tubes[0])):
        lowpoint = True
        for neighbor in neighbors(tubes, i, j):
            if tubes[i][j] >= neighbor:
                lowpoint = False
                break
        if lowpoint:
            low_points.append(tubes[i][j]+1)

print(sum(low_points))