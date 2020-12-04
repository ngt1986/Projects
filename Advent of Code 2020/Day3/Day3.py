
trees = []
with open("day3input.txt", 'r') as infile:
    for row in infile:
        trees.append(row[0:-1])
print(len(trees))

start = 0

count_hit = 0

for row in trees[1::]:
    if (start + 1) > len(trees[0])-1:
        start -= (len(trees[0]))
        start += 1
    else:
        start += 1

    if row[start] == '#':
        count_hit += 1
count_list=[]
count_list.append(count_hit)
print(count_list)
count_hit = 0
start = 0

for row in trees[1::]:
    if (start + 3) > len(trees[0])-1:
        start -= (len(trees[0]))
        start += 3
    else:
        start += 3

    if row[start] == '#':
        count_hit += 1
count_list.append(count_hit)
print(count_list)
count_hit = 0
start = 0

for row in trees[1::]:
    if (start + 5) > len(trees[0])-1:
        start -= (len(trees[0]))
        start += 5
    else:
        start += 5

    if row[start] == '#':
        count_hit += 1
count_list.append(count_hit)
print(count_list)
count_hit = 0
start = 0

for row in trees[1::]:
    if (start + 7) > len(trees[0])-1:
        start -= (len(trees[0]))
        start += 7
    else:
        start += 7

    if row[start] == '#':
        count_hit += 1
count_list.append(count_hit)
print(count_list)
count_hit = 0
start = 0

for row in range(2, len(trees), 2):
    if (start + 1) > len(trees[0])-1:
        start -= (len(trees[0]))
        start += 1
    else:
        start += 1

    if trees[row][start] == '#':
        count_hit += 1
count_list.append(count_hit)
print(count_list)
count_hit = 0
start = 0
multiple = count_list[0] * count_list[1] * count_list[2] * count_list[3] * count_list[4]
print(multiple)