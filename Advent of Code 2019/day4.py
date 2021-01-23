import sys
import os
import math
import numpy as np
import re


'''
You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or
stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

Puzzle input range = 240920-789857
'''

#check for repeating digits
def doubledigit(num):
    for digit in list(str(num)):
        my_regex = str(digit)
        if bool(re.search(my_regex+my_regex, str(num)))==True:
            if bool(re.search(my_regex+my_regex+my_regex, str(num)))==True:
                return False
            return True
        
#check if any digits are less than preceding digits in number
def nodecrease(num):
    for digit in range(1,6):
        if list(str(num))[digit]<list(str(num))[digit-1]:
            return False
    return True
    
#2nd pass
def doubledigit2(num):
    for digit in list(str(num))[::-1]:
        my_regex = str(digit)
        if bool(re.search(my_regex+my_regex, str(num)))==True:
            if bool(re.search(my_regex+my_regex+my_regex, str(num)))==True:
                return False
            return True

passwords=[]
for i in range(240920,789857):
    if doubledigit(i):
        if nodecrease(i):
            passwords.append(i)
    if doubledigit2(i):
        if nodecrease(i) and i not in passwords:
            passwords.append(i)
print(len(passwords))
##passwords=[]
##for i in range(240920,789857):
##    if doubledigit(i):
##        if nodecrease(i):
##            passwords.append(i)
##print(len(passwords))


        



        
