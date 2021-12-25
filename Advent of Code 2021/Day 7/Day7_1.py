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

crabs.sort()
# print(crabs)
# print("length = ", len(crabs))
# print("middle = ", crabs[int(len(crabs)/2)])
median_crab = 349
fuel_cost = 0
for crab in crabs:
    fuel_cost += abs(median_crab-crab)
print(fuel_cost)