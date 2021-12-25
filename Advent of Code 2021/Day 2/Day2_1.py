path = []
with open('day2_input.txt', 'r') as infile:
    for row in infile:
        row = row.split(' ')
        row[1]= int(row[1].strip('\n'))
        path.append(row)

print(path)

horizontal = 0
depth = 0
aim = 0

for row in path:
    if row[0] == 'forward':
        horizontal += row[1]
    elif row[0] == 'up':
        depth -= row[1]
    elif row[0] == 'down':
        depth += row[1]
print(horizontal*depth)

