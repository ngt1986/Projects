# get lines
import numpy as np
lines = []
with open('day5_input.txt', 'r') as infile:
    for row in infile:
        row = row.split('->')
        start=(row[0].split(','))
        end = (row[1].strip('\n').split(','))
        start = (int(start[0]),int(start[1]))
        end = (int(end[0]),int(end[1]))
        lines.append((start,end))

size = (1000,1000)
# size = (10,10)
matrix = np.zeros(size)

print(lines)
for line in lines:
    if line[0][0] == line[1][0]:
        if line[0][1] < line[1][1]:
            matrix[line[0][1]:(line[1][1]+1),line[0][0]] += + 1
        else:
            matrix[line[1][1]:(line[0][1]+1),line[0][0]] += + 1
    elif line[0][1] == line[1][1]:
        if line[0][0] < line[1][0]:
            matrix[line[0][1],line[0][0]:(line[1][0]+1)] += + 1
        else:
            matrix[line[0][1],line[1][0]:(line[0][0]+1)] += + 1
    else:  # diagonal
        #right
        if line[0][0] < line [1][0]:
            # down
            if line[0][1]< line[1][1]:
                i = line[0][0]
                j = line[0][1]
                matrix[j][i] += 1
                while i < line[1][0]:
                    i += 1
                    j+=1
                    matrix[j][i] += 1
            # up
            else:
                i = line[0][0]
                j = line[0][1]
                matrix[j][i] += 1
                while i < line[1][0]:
                    i += 1
                    j-=1
                    matrix[j][i] += 1
        #left
        else:
            #down
            if line[0][1] < line[1][1]:
                i = line[0][0]
                j = line[0][1]
                matrix[j][i] += 1
                while i > line[1][0]:
                    i -= 1
                    j += 1
                    matrix[j][i] += 1
            #up
            else:
                i = line[0][0]
                j = line[0][1]
                matrix[j][i] += 1
                while i > line[1][0]:
                    i -= 1
                    j -= 1
                    matrix[j][i] += 1

print(matrix)
sum2plus = 0
for row in matrix:
    for digit in row:
        if digit >= 2:
            sum2plus +=1

print(sum2plus)