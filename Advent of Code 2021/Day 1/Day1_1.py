sonar_scans = []
with open('day1_input.txt', 'r') as infile:
    for row in infile:
        row = int(row.strip('\n'))
        sonar_scans.append(row)

increased_value_count = 0

for i in range(len(sonar_scans)-1):
    if sonar_scans[i+1] > sonar_scans[i]:
        increased_value_count += 1

print(increased_value_count)

