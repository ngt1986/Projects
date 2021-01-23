import sys
import os
import math
import itertools as it
import pdb

puzzleinput=[3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,102,183,264,345,426,99999,3,9,1002,9,4,9,1001,9,3,9,102,2,9,
             9,1001,9,5,9,102,3,9,9,4,9,99,3,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,2,9,9,1001,
             9,2,9,1002,9,3,9,4,9,99,3,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,
             9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,
             102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,
             9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,
             3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,
             1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,
             9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,
             3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,
             9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,
             4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99]

#day 5:
'''
First, you'll need to add two new instructions:

Opcode 1 = addition of parameters
Opcode 2 = multiplication of parameters
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
For example, the instruction 3,50 would take an input value and store it at address 50.

Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the
value at address 50.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already
understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position -
if the parameter is 50, its value is the value stored at address 50 in memory.
Until now, all parameters have been in position mode.

0=position mode - [x] parameter value interpreted as value stored at position [x]
1=immediate mode- [x] parameter value interpreted as [x]
'''


#opcode handling

#addition of parameters
def op1(inp1,pm1,inp2,pm2,address):
    if pm1 == 0 and pm2 == 0:
        x[address]=x[inp1]+x[inp2]
    elif pm1 == 1 and pm2 == 0:
        x[address]=inp1+x[inp2]
    elif pm1 == 0 and pm2 == 1:
        x[address]=x[inp1]+inp2
    else:
        x[address]=inp1+inp2
    #print(address,x[address])
    return

#multiplication of parameters
def op2(inp1,pm1,inp2,pm2,address):
    if pm1 == 0 and pm2 == 0:
        x[address]=x[inp1]*x[inp2]
    elif pm1 == 1 and pm2 == 0:
        x[address]=inp1*x[inp2]
    elif pm1 == 0 and pm2 == 1:
        x[address]=x[inp1]*inp2
    else:
        x[address]=inp1*inp2
    return

#Input handling
def op3(INPUT, address):
    x[address]=INPUT
    return

#Output handling
def op4(pm, address):
    if pm ==0:
        return x[address]
    if pm ==1:
        return address

#jump-if-true
def op5(inp1,pm1,inp2,pm2,index):
    if pm1 ==0 and pm2 == 0:
        if x[inp1]!=0:
            index = x[inp2]
            return index
        else:
            return index+3
    elif pm1==0 and pm2 ==1:
        if x[inp1]!=0:
            index = inp2
            return index
        else:
            return index+3
    elif pm1==1 and pm2 == 0:
        if inp1!=0:
            index= x[inp2]
            return index
        else:
            return index+3
    elif pm1==1 and pm2==1:
        if inp1!=0:
            index=inp2
            return index
        else:
            return index+3
    else:
        return index+3

#jump-if-false
def op6(inp1,pm1,inp2,pm2,index):
    if pm1 ==0 and pm2 == 0:
        if x[inp1]==0:
            index = x[inp2]
            return index
        else:
            return index+3
    elif pm1==0 and pm2 ==1:
        if x[inp1]==0:
            index = inp2
            return index
        else:
            return index+3
    elif pm1==1 and pm2 == 0:
        if inp1==0:
            index= x[inp2]
            return index
        else:
            return index+3
    elif pm1==1 and pm2==1:
        if inp1==0:
            index=inp2
            return index
        else:
            return index+3
    else:
        return index+3

#less than
def op7(inp1,pm1,inp2,pm2,address):
    if pm1 ==0 and pm2 == 0:
        if x[inp1]<x[inp2]:
            x[address]=1
            return
    elif pm1==0 and pm2 ==1:
        if x[inp1]<inp2:
            x[address]=1
            return
    elif pm1==1 and pm2 ==0:
        if inp1<x[inp2]:
            x[address]=1
            return
    else:
        if inp1<inp2:
            x[address]=1
            return
    x[address]=0    
    return

#equals
def op8(inp1,pm1,inp2,pm2,address):
    if pm1 ==0 and pm2 == 0:
        if x[inp1]==x[inp2]:
            x[address]=1
            return
    elif pm1==0 and pm2 ==1:
        if x[inp1]==inp2:
            x[address]=1
            return
    elif pm1==1 and pm2 ==0:
        if inp1==x[inp2]:
            x[address]=1
            return
    else:
        if inp1==inp2:
            x[address]=1
            return
    x[address]=0    
    return

#get opcode and parameter modes
def instruction(num):

    if len(str(num))<2:
        opcode = num
    else:
        opcode = int(list(str(num))[-2]+list(str(num))[-1])
    try:
        pm1 = int(list(str(num))[::-1][2])
    except:
        pm1 = 0
    try:
        pm2 = int(list(str(num))[::-1][3])
    except:
        pm2 = 0
    try:
        pm3 = int(list(str(num))[::-1][4])
    except:
        pm3 = 0
    return (opcode,pm1, pm2, pm3)

#compute OUTPUT given INPUT
def comp(x, INPUT, PHASE, index):
    count3=0
    while instruction(x[index])[0]!=99:
        inst=instruction(x[index])
        #print(inst)
        if inst[0]==1:
            op1(x[index+1],inst[1],x[index+2],inst[2],x[index+3])
            index+=4
        elif inst[0]==2:
            op2(x[index+1],inst[1],x[index+2],inst[2],x[index+3])
            index+=4
        elif inst[0]==3:
            if count3==0:
                op3(PHASE,x[index+1])
                index+=2
                count3+=1
            elif count3==1:
                op3(INPUT,x[index+1])
                index+=2
                count3+=1
            else:
                break
        elif inst[0]==4:
            OUTPUT = op4(inst[1],x[index+1])
##            if OUTPUT != 0:
##                return OUTPUT
            index+=2
        elif inst[0]==5:
            index = op5(x[index+1],inst[1],x[index+2],inst[2],index)
        elif inst[0]==6:
            index = op6(x[index+1],inst[1],x[index+2],inst[2],index)
        elif inst[0]==7:
            op7(x[index+1],inst[1],x[index+2],inst[2],x[index+3])
            index+=4
        elif inst[0]==8:
            op8(x[index+1],inst[1],x[index+2],inst[2],x[index+3])
            index+=4
    return OUTPUT

def amploop(x,INPUT,PHASE,index):
    ampA=comp(x,INPUT,PHASE[0],index)
    print(ampA)
    if ampA == None:
        ampA=0
    ampB=comp(x,ampA,PHASE[1],index)
    ampC=comp(x,ampB,PHASE[2],index)
    ampD=comp(x,ampC,PHASE[3],index)
    ampE=comp(x,ampD,PHASE[4],index)
##    if ampE > max_out:
##        max_out=ampE
##        opt_phase=PHASE
    return ampE


#INPUTS
'''test input'''
puzzleinput=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

index=0
INPUT = 0
OUTPUT = 0
PHASES = list(it.permutations([5,6,7,8,9]))
x=list(puzzleinput)
max_out=0
opt_phase=()

##pdb.set_trace()



x=list(puzzleinput)

f_out=0


PHASE=(9,8,7,6,5)
print(x)
f_out=amploop(x,INPUT,PHASE,index)
##    print(f_out, PHASE)
print(x)
##while True:
##    f_out=amploop(x,PHASE,f_out,index)
##    
##    print(x)


print(f_out)

##for PHASE in PHASES:
##    x=list(puzzleinput)
##    f_out=amploop(x,PHASE,INPUT,index)
####    print(f_out, PHASE)
##    while True:
##        if amploop(x,PHASE,f_out,index)>139629729:
##            break
##        f_out=amploop(x,PHASE,f_out,index)
##        
##    if f_out>max_out:
##        max_out=f_out
##        opt_phase=PHASE
##    if f_out==139629729:
##        break
##print(max_out,opt_phase)
##
##
##print(f_out)








