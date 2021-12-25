# get lines
crabs = []
# with open('day7_input_sample.txt', 'r') as infile:
#     for row in infile:
#         row = row.split(',')
#         for digit in row:
#             crabs.append(int(digit))
# print(crabs)
with open('day7_input.txt', 'r') as infile:
    for row in infile:
        row = row.split(',')
        for digit in row:
            crabs.append(int(digit))
average = 491
fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)
average = round(sum(crabs)/len(crabs))
print(average)


fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)
average = 489
fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)
average = 488
fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)
average = 487
fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)
average = 486
fuel_cost = 0
for crab in crabs:
    fuel_cost += (abs(average-crab)*(abs(average-crab)+1))/2
print(fuel_cost)