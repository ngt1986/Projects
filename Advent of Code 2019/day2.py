import sys
import os
import math
puzzleinput=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,
   1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,
   1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,
   2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,
   1,143,2,147,1,147,5,0,99,2,0,14,0]

#x=[1,1,1,4,99,5,6,0,99]

index=0
#part 1 states to replace position 1 with 12 and position 2 with 2
#x[1]=12
#x[2]=2
#dont need this for part 2 though

#print(x)

##while x[index]!=99:
##    if x[index]==1:
##        x[x[index+3]]=x[x[index+1]]+x[x[index+2]]
##        index+=4
##    if x[index]==2:
##        x[x[index+3]]=x[x[index+1]]*x[x[index+2]]
##        index+=4
##    print("x[index] = ", x[index])
##print(x)

#part 2 noun = position 1 and verb = position 2, output is position 0
#whats the noun/verb pair that gives output 19690720
x=list(puzzleinput)
for noun in range(0,100):
    for verb in range(0,100):
        x=list(puzzleinput)
        index=0
        x[1]=noun
        x[2]=verb
        while x[index]!=99:
            if x[index]==1:
                x[x[index+3]]=x[x[index+1]]+x[x[index+2]]
                index+=4
            elif x[index]==2:
                x[x[index+3]]=x[x[index+1]]*x[x[index+2]]
                index+=4
            else:
                break
        if x[0]==19690720:
            print(x)
            print("noun = ",noun,"verb = ", verb, 100*noun+verb)
            break
        #x=puzzleinput
    #x=puzzleinput
    #print("x[index] = ", x[index])



