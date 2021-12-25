# get lines
tubes = []
with open('day9_input.txt', 'r') as infile:
    for row in infile:
        row = list(row.strip('\n'))
        for i in range(len(row)):
            row[i] = int(row[i])
        row.insert(0, 9)
        row.append(9)
        tubes.append(row)
tubes.insert(0, [9]*len(tubes[0]))
tubes.append([9]*len(tubes[0]))

def neighbors(tubes, node):
    neighbors = []
    if node == 9:
        return False
    else:
        if tubes[node[0] - 1][node[1]] != 9:
            neighbors.append((node[0]-1,node[1]))
        if tubes[node[0] + 1][node[1]] != 9:
            neighbors.append((node[0] + 1, node[1]))
        if tubes[node[0]][node[1] + 1] != 9:
            neighbors.append((node[0], node[1]+1))
        if tubes[node[0]][node[1] - 1] != 9:
            neighbors.append((node[0], node[1]-1))
    return neighbors

def get_basin(tubes, root, curr= None, visited= None, stack= None):
    if curr is None:
        curr = root
    if visited is None:
        visited = [curr]
    if stack is None:
        stack = []

    for neighbor in neighbors(tubes,curr):
        if neighbor not in visited and neighbor not in stack:
            stack.append(neighbor)
    if len(stack) == 0 and curr != root:
        return visited

    curr = stack.pop()
    visited.append(curr)
    get_basin(tubes, root, curr, visited, stack)
    return visited


basins = []
for i in range(1,len(tubes)-1):
    for j in range(1,len(tubes[0])-1):
        if len(basins) == 0:
                basins.append(get_basin(tubes, (i,j)))
        else:
            if tubes[i][j] != 9:
                found_in_basin = False
                for basin in basins:
                    if (i,j) in basin:
                        found_in_basin = True
                        break
                if not found_in_basin:
                    basins.append(get_basin(tubes, (i,j)))
lengths = []
for basin in basins:
    lengths.append(len(basin))
lengths.sort()
print(lengths)
print(lengths[-3]*lengths[-2]*lengths[-1])