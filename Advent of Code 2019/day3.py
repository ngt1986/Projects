import sys
import os
import math
import numpy as np

with open('day3A.txt')as a:
    A=a.readlines()
A = [x.strip() for x in A]
wireA=A[0].split(",")

for i in range(0,len(wireA)):
    wireA[i]=(str(wireA[i][0]),int(wireA[i][1:]))
##print(wireA)
              
with open('day3B.txt')as b:
    B=b.readlines()
B = [x.strip() for x in B]
wireB=B[0].split(",")

for i in range(0,len(wireB)):
    wireB[i]=(str(wireB[i][0]),int(wireB[i][1:]))
##print(wireB)

def checkdistance(x,y):
    distance=abs(x)+abs(y)
    return distance

pathA = [(0,0)]
positionA =[0,0]
pathB = [(0,0)]
positionB =[0,0]
##wireA = [('R',75),('D',30),('R',83),('U',83),('L',12),('D',49),('R',71),('U',7),('L',72)]
##wireB =[('U',62),('R',66),('U',55),('R',34),('D',71),('R',55),('D',58),('R',83)]

def route(wire,path,position):
    for line in wire:
        if line[0]=='R':
            for i in range (1,line[1]+1):
                path.append((position[0]+i,position[1]))
            position[0]+=i
        elif line[0]=='L':
            for i in range (1,line[1]+1):
                path.append((position[0]-i,position[1]))
            position[0]-=i
        elif line[0]=='U':
            for i in range (1,line[1]+1):
                path.append((position[0],position[1]+i))
            position[1]+=i
        else:
            for i in range (1,line[1]+1):
                path.append((position[0],position[1]-i))
            position[1]-=i
           
    return path

pathA = route(wireA,pathA,positionA)
pathB = route(wireB,pathB,positionB)

commonpoints=[]
for point in pathA:
    if point in pathB and point!=(0,0):
        commonpoints.append(point)
        print("Point ",point," is common")
print(commonpoints)

distances=[]
for point in commonpoints:
    distances.append(checkdistance(point[0],point[1]))

print("Min distance is ",min(distances))

minsteps = 0
for point in commonpoints:
    minsteps = pathA.index(point) + pathB.index(point)
    print("Min steps to common point ", point, " is ", minsteps)
##
##Gridsize = 10000
##
##board=np.zeros((int(Gridsize),int(Gridsize)))
##wireA = [('R',75),('D',30),('R',83),('U',83),('L',12),('D',49),('R',71),('U',7),('L',72)]
##wireB =[('U',62),('R',66),('U',55),('R',34),('D',71),('R',55),('D',58),('R',83)]
##center=[int(Gridsize/2),int(Gridsize/2)]
##positionA=[int(Gridsize/2),int(Gridsize/2)]
##for line in wireA:
##    if line[0]=='R':
##        for i in range (0,line[1]):
##            board[positionA[0],positionA[1]+1]=1
##            positionA[1]+=1
##    elif line[0]=='L':
##        for i in range (0,line[1]):
##            board[positionA[0],positionA[1]-1]=1
##            positionA[1]-=1
##    elif line[0]=='U':
##        for i in range (0,line[1]):
##            board[positionA[0]-1,positionA[1]]=1
##            positionA[0]-=1
##    else:
##        for i in range (0,line[1]):
##            board[positionA[0]+1,positionA[1]]=1
##            positionA[0]+=1
##    print(positionA[0],positionA[1])
##positionB=[int(Gridsize/2),int(Gridsize/2)]
##
##for line in wireB:
##    if line[0]=='R':
##        for i in range (0,line[1]):
##            if board[positionB[0],positionB[1]+1]==1:
##                board[positionB[0],positionB[1]+1]=3
##                checkdistance(positionB[0],positionB[1]+1)
##            else:
##                board[positionB[0],positionB[1]+1]=2
##            positionB[1]+=1
##    elif line[0]=='L':
##        for i in range (0,line[1]):
##            if board[positionB[0],positionB[1]-1]==1:
##                board[positionB[0],positionB[1]-1]=3
##                checkdistance(positionB[0],positionB[1]-1)
##            else:
##                board[positionB[0],positionB[1]-1]=2
##            positionB[1]-=1
##    elif line[0]=='U':
##        for i in range (0,line[1]):
##            if board[positionB[0]-1,positionB[1]]==1:
##                board[positionB[0]-1,positionB[1]]=3
##                checkdistance(positionB[0]-1,positionB[1])
##            else:
##                board[positionB[0]-1,positionB[1]]=2
##            positionB[0]-=1
##    else:
##        for i in range (0,line[1]):
##            if board[positionB[0]+1,positionB[1]]==1:
##                board[positionB[0]+1,positionB[1]]=3
##                checkdistance(positionB[0]+1,positionB[1])
##            else:
##                board[positionB[0]+1,positionB[1]]=2
##            positionB[0]+=1
##


