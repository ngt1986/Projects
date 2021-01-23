import sys
import os
import numpy as np
import collections

with open('day6.txt')as a:
    puzzleinput=a.readlines()
puzzleinput = [x.strip() for x in puzzleinput]

'example input'
##puzzleinput = [
##'COM)B',
##'B)C',
##'C)D',
##'D)E',
##'E)F',
##'B)G',
##'G)H',
##'D)I',
##'E)J',
##'J)K',
##'K)L']

puzzleinput = [x.split(')') for x in puzzleinput]

"list of unique planets, including COM"
unique_list=[]
for sublist in puzzleinput:
    if sublist[0] not in unique_list:
        unique_list.append(sublist[0])
    if sublist[1] not in unique_list:
        unique_list.append(sublist[1])

d={}      
for pair in puzzleinput:
    d.setdefault(pair[1],[]).append(pair[0])

sets=[]

for k,v in d.items():
    set1=[]
    index=k
    while True:
        if d[index]==['COM']:
            set1.append(d[index][0])
            sets.append(set1)
            break
        else:
            set1.append(d[index][0])
            index=d[index][0]

count=0
for i in sets:
    count+=len(i)
##print(count)

'''part 2'''

k1='YOU'
k2='SAN'
set1=[]
set2=[]
index=k1
while True:
    if d[index]==['COM']:
        set1.append(d[index][0])
        break
    else:
        set1.append(d[index][0])
        index=d[index][0]
index=k2
while True:
    if d[index]==['COM']:
        set2.append(d[index][0])
        break
    else:
        set2.append(d[index][0])
        index=d[index][0]
##print(set1)
##print(set2)

for x in set1:
    if x in set2:
        print(x)
        break
print(set1.index(x)+set2.index(x))
