# get lines
caves = []
with open('day12_input.txt', 'r') as infile:
    for row in infile:
        row = (row.strip('\n').split('-'))
        row.sort()
        caves.append(row)
print(caves)

paths = []

def neighbors(caves, curr):
    neighbors = []
    for cave in caves:
        if cave[0] == curr:
            neighbors.append(cave[1])
        elif cave[1] == curr:
            neighbors.append(cave[0])
        elif cave[0] == curr:
            neighbors.append(cave[1])
        elif cave[1] == curr:
            neighbors.append(cave[0])
    return neighbors


def get_paths(caves, paths, curr = None, path = None, stack  = None):
    if curr is None:
        curr = caves[11][1]
    if path is None:
        path = [curr]
    if stack is None:
        stack = [curr]
    if curr == 'end':
        temp = list(path)
        paths.append(temp)
        return paths
    for neighbor in neighbors(caves, curr):
        if neighbor not in stack:
            stack.append(neighbor)
            path.append(neighbor)
            paths = get_paths(caves, paths, neighbor, path, stack)
            stack.pop()
            path.pop()
        elif neighbor == neighbor.upper() and neighbor in stack:  # cant visit a small cave again
            stack.append(neighbor)
            path.append(neighbor)
            paths = get_paths(caves, paths, neighbor, path, stack)
            stack.pop()
            path.pop()
    return paths


cave_paths = get_paths(caves, paths)
print(cave_paths)
