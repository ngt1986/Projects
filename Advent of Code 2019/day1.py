import sys
import os
import math
with open('day1input.txt') as f:
    input1=f.readlines()
input1 = [x.strip() for x in input1]
input2 = []
print(input1)
for i in range(len(input1)):
    input2.append(math.floor(int(input1[i])/3-2))

x = sum(input2)    
print(input2)
print(x)

"part 2"

##for i in input2:
##    print(i)
input3=input2

while sum(input3)>0:
    for i in range(len(input3)):
        if input3[i] >= 9:
            x+=math.floor(input3[i]/3-2)
            input3[i]=math.floor(input3[i]/3-2)
        else:
            input3[i]=0
    print(input3)
print(x)

    
