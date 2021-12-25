# get lines
import math

fishes = [] #1 through 5
with open('day6_input.txt', 'r') as infile:
    for row in infile:
        row = row.split(',')
        for digit in row:
            fishes.append(int(digit))
days = [0]*9
for fish in fishes:
    days[fish] +=1

for i in range(256):
    today = i % len(days)

    days[(today+7)%len(days) ] += days[today]

print(sum(days))