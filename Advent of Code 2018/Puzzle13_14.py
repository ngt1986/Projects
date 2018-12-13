

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
print('--------')

#a="""
sequence=[]

#add new list, completed=[], which is now different than just sequence
#and is based on the order in which steps are completed
completed=[]
steps_remaining = True

counter=0
workers=5

#dict with active steps and start time
active_steps={}


#puzzle 14 section:
while steps_remaining:

    for k, v in d.items():
        #if key has no values, it's the next step, so add it to SEQUENCE
        if d[k]==[]and k not in sequence:
            
            #if workers available, add the step to active steps
            if len(active_steps)<workers:
                sequence.append(k)
                active_steps[k]=counter #start time = current counter value
                
        elif v!='':
            continue
    
    
    counter+=1
    #for steps in active steps, check if counter - start time = the numeric value of step (letter)
    #if that check is true, then step is done, add step for removal, add step to completed
    #then remove the step from the rest of the dictionary, allowing those other steps to be "ready"
    removal=[]
    for ka, va in active_steps.items():
        if counter-va==ord(ka)-4:
            removal.append(ka)
            completed.append(ka)
            for value in d.values():
                try:
                    value.remove(ka)
                except:
                    continue

    #remove the step from active_steps if in removal=[]
    for k in removal:
        del active_steps[k]

    #check if any values remain, which means more iteration needed to determine rest of SEQUENCE

    
    
    if len(completed)==len(d):
        steps_remaining = False
    
##    print("completed: ",completed,'\n',"sequence: ",sequence,'\n',"active: ", active_steps,'\n', 
##          "counter: ", counter,'\n', d)
    
completed=''.join(completed)
print("completed order: ", completed, "seconds: ", counter)

#puzzle 13 section:

##sequence=[]
##steps_remaining = True
##
##
##while steps_remaining:
##    #create a placeholder list (removal = []) to remove from dictionary after each loop, 
##    #since the dictionary size cannot change during iteration
##    #placed before for loop so that it's cleared after each for loop
##    removal=[]
##    
##    for k, v in d.items():
##        #if key has no values, it's the next step, so add it to SEQUENCE
##        if d[k]==[]:
##            sequence.append(k)
##            removal.append(k)
##            #check if key is in any remaining values, and if so remove it from all value sets
##            for v in d.values():
##                if k in v:
##                    v.remove(k)
##            #break out of the for loop above since other steps may now be available
##            break
##        
##        elif v!='':
##            continue
##    #finally, remove key from dictionary so that it doesn't get added to sequence again
##    for key in removal:
##        del d[key]
##            
##    #check if any values remain, which means more iteration needed to determine rest of SEQUENCE
##    for v in d.values():
##        if v!=[]:
##            steps_remaining = True
##    if d=={}:
##        steps_remaining = False
##    
##sequence=''.join(sequence)
##print(sequence)




