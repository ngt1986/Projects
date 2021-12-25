# get dots
import numpy as np
import matplotlib.pyplot as plt
import itertools

dots=[]
with open('day13_input_dots.txt', 'r') as infile:
    for row in infile:
        row = (row.strip('\n').split(','))
        dot_row = (int(row[0]), int(row[1]))
        dots.append(dot_row)
print(dots)

max_x = 0
max_y = 0
for dot in dots:
    if dot[0] > max_y:
        max_y = dot[0]
    if dot[1] > max_x:
        max_x = dot[1]
# print(max_x, max_y)
dot_matrix = np.zeros((max_x+1,max_y+1))
for dot in dots:
    dot_matrix[dot[1]][dot[0]] = 1
# print(dot_matrix)

folds_list = []
with open('day13_input_folds.txt','r') as infile:
    for row in infile:
        row = row.strip('\n')
        row = row.strip('fold along ').split('=')
        folds_list.append((row[0],int(row[1])))
# print(folds_list)

def make_fold(dot_matrix, fold):
    matrix1 = 0
    matrix2 = 0
    if fold[0] == 'y':
        if len(dot_matrix) % 2==0:
            matrix1 = dot_matrix[0:fold[1]]
            matrix2 = np.flipud(dot_matrix[fold[1]:])
        else:
            matrix1 = dot_matrix[0:fold[1]]
            matrix2 = np.flipud(dot_matrix[fold[1]+1:])
    elif fold[0] == 'x':
        if len(dot_matrix[0]) % 2 != 0:
            matrix1 = dot_matrix[:,:fold[1]]
            matrix2 = np.fliplr(dot_matrix[:,fold[1]+1:])
        else:
            matrix1 = dot_matrix[:,:fold[1]]
            matrix2 = np.fliplr(dot_matrix[:,fold[1]:])
    return matrix1+matrix2

for fold in folds_list:
    dot_matrix = make_fold(dot_matrix, fold)
    count = 0

for i in range(len(dot_matrix[0])):
    for j in range(len(dot_matrix)):
        if dot_matrix[j][i] >= 1:
            count+=1
            dot_matrix[j][i] = 1
            plt.plot(i,j,'X', color = 'blue')
        else:
            plt.plot(i,j,'X',color='red')
b = dot_matrix
plt.show()
