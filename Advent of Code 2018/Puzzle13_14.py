

with open("puzzle13input.txt","r") as puzzle:
    puzzle = puzzle.read().replace('\n','')

#break input into actual steps from long string
steps=[]
for i in range(0,len(puzzle),48):
    steps.append(puzzle[i:i+48])
#print(steps)

#break steps into just the important letters
#format (X, Y) means step X must finish before step Y
order=[]
for step in steps:
    order.append((step[5],step[36]))
order.sort()
#print(order)

def whatcomesbefore(letter):
    before=[]
    for step in order:
        if step[1]==letter:
            #print(step[0],letter)
            before.append(step[0])
    return before



#generates dictionary of all letters (keys) and what comes before them (values)
d={}
for i in range(65,65+26):
    #test prints
    #print('\n')
    d[chr(i)]=whatcomesbefore(chr(i))
    #whatcomesbefore(chr(i))
    #print('---------''\n')
#test print
print(d)

#a="""
sequence=[]
steps_remaining = True

while steps_remaining:
    #create a placeholder list (removal = []) to remove from dictionary after each loop, 
    #since the dictionary size cannot change during iteration
    #placed before for loop so that it's cleared after each for loop
    removal=[]
    
    for k, v in d.items():
        #if key has no values, it's the next step, so add it to SEQUENCE
        if d[k]==[]:
            sequence.append(k)
            removal.append(k)
            #check if key is in any remaining values, and if so remove it from all value sets
            for v in d.values():
                if k in v:
                    v.remove(k)
            #break out of the for loop above since other steps may now be available
            break
        
        elif v!='':
            continue
    #finally, remove key from dictionary so that it doesn't get added to sequence again
    for key in removal:
        del d[key]
            
    #check if any values remain, which means more iteration needed to determine rest of SEQUENCE
    for v in d.values():
        if v!=[]:
            steps_remaining = True
    if d=={}:
        steps_remaining = False
    
sequence=''.join(sequence)
print(sequence)
#"""
