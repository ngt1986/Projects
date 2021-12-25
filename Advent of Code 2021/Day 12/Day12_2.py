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


def get_paths(caves, paths, curr = None, path = None, stack  = None, smalls = ['start','end'], banned = None):
    if curr is None:
        curr = caves[11][1]
    if path is None:
        path = [curr]
    if stack is None:
        stack = [curr]
    if banned is None:
        banned = []
    if curr == 'end':
        temp = list(path)
        paths.append(temp)
        return paths
    for neighbor in neighbors(caves, curr):
        if neighbor not in stack:
            stack.append(neighbor)
            path.append(neighbor)
            if neighbor == neighbor.lower():
                smalls.append(neighbor)
            paths = get_paths(caves, paths, neighbor, path, stack, smalls, banned)
            stack.pop()
            path.pop()
            if neighbor == neighbor.lower():
                smalls.pop()

        elif neighbor != 'start' and neighbor != 'end' and neighbor in stack:  # can only visit a small cave again ONCE per path
            if neighbor == neighbor.upper():
                stack.append(neighbor)
                path.append(neighbor)
                paths = get_paths(caves, paths, neighbor, path, stack,smalls, banned)
                stack.pop()
                path.pop()
            elif neighbor == neighbor.lower() and neighbor in smalls and neighbor not in banned and len(banned)<1:
                stack.append(neighbor)
                path.append(neighbor)
                smalls.append(neighbor)
                banned.append(neighbor)
                paths = get_paths(caves, paths, neighbor, path, stack,smalls,banned)
                stack.pop()
                path.pop()
                smalls.pop()
                banned.pop()
    return paths


cave_paths = get_paths(caves, paths)
print(cave_paths)
print(len(cave_paths))
