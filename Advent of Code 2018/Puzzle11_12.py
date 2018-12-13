#9/10
import numpy as np
from collections import Counter

def str2num(string):
    total_val=0
    for i in string:
        total_val+=ord(i)-96
    return total_val

puzzle = """305, 349
315, 193
154, 62
246, 310
145, 283
260, 324
342, 79
321, 353
40, 242
351, 353
337, 297
174, 194
251, 160
314, 195
114, 81
204, 246
203, 169
203, 296
60, 276
201, 47
206, 96
243, 46
295, 304
319, 80
213, 330
337, 255
40, 262
302, 150
147, 349
317, 240
96, 315
133, 305
320, 348
210, 300
266, 216
223, 319
207, 152
127, 214
312, 245
49, 329
211, 84
129, 276
247, 143
208, 235
271, 126
124, 211
144, 184
54, 88
354, 300
148, 85"""

##puzzle = """305, 349
##315, 193
##154, 62
##246, 310
##145, 283
##260, 324
##342, 79
##321, 353
##40, 242
##351, 353
##337, 297"""

puzzle = puzzle.split('\n')
##print(puzzle)

def closest_node(x,y):
    shortest_dist=500
    for i in range(0,len(puzzle_coords)):
        dist = distance(x, y, puzzle_coords[i])
        if dist < shortest_dist:
            shortest_dist = dist
            grid[x,y]=i+1
        elif dist == 0:
            grid[x,y]=i+1
        elif dist == shortest_dist:
            grid[x,y]=0
    return grid

def distance(x,y,coord):
    dist = (abs(coord[0]-x)+abs(coord[1]-y))
    return dist

def total_distance(x,y):
    total_dist=0
    for i in range(0,len(puzzle_coords)): 
        total_dist += (abs(puzzle_coords[i][0]-x)+abs(puzzle_coords[i][1]-y))
    if total_dist < 10000:
        grid2[x,y] = True
    return grid2

def assign_node(x,y,grid,i):
    grid[x,y]=i+1
    return grid

grid = np.zeros((355,355))
grid2 = np.full((355,355),False)

puzzle_coords=[]
for i in range(len(puzzle)):
    if puzzle[i][3] ==' ':   
        puzzle_coords.append(((int(puzzle[i][0:2])),(int(puzzle[i][4:]))))
    else:
        puzzle_coords.append(((int(puzzle[i][0:3])),(int(puzzle[i][4:]))))

##print(puzzle_coords)

for i in range(0,len(puzzle_coords)):
    grid=assign_node(puzzle_coords[i][0],puzzle_coords[i][1],grid,i)
                             

for x in range(355):
    for y in range(355):
        closest_node(x,y)
        
#used for part 11
counts=np.unique(grid, return_counts=True)

for i in range(0,len(puzzle_coords)+1):
    if (i not in grid[:,0]) and (i not in grid[0,:]) and (i not in grid[354,:]) and (i not in grid[:,354]):
        print(counts[0][i],counts[1][i])

#used for part 12
for x in range(355):
    for y in range(355):
        total_distance(x,y)
        
counts2=np.unique(grid2, return_counts=True)
print(counts2)
