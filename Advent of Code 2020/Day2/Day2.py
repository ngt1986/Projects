import re
pi = []
with open('day2input.txt', 'r') as infile:
    for row in infile:
        pi.append(row[0:-1])
pi_mod = []

for row in pi:
    pi_mod.append(re.split("\-| ", row))
print(pi_mod)
count_good_pass = 0

# PART 1:
# for row in pi_mod:
#     if row[3].count(row[2][0]) >= int(row[0]) and row[3].count(row[2][0]) <= int(row[1]):
#         print(row)
#         count_good_pass += 1

# PART 2:
for row in pi_mod:
    if row[2][0] not in row[3][int(row[0])-1] and row[2][0] not in row[3][int(row[1])-1]:
        continue
    elif row[2][0] in row[3][int(row[0])-1] and row[2][0] in row[3][int(row[1])-1]:
        continue
    elif row[2][0] in row[3][int(row[0])-1] or row[2][0] in row[3][int(row[1])-1]:
        count_good_pass += 1
# print(len(pi_mod))
print(count_good_pass)