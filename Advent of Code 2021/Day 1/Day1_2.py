sonar_scans = []
with open('day1_input.txt', 'r') as infile:
    for row in infile:
        row = int(row.strip('\n'))
        sonar_scans.append(row)

increased_value_count = 0

def get_window(sonar_scans, pos):
    if pos < len(sonar_scans)-2:
        return sonar_scans[pos]+sonar_scans[pos+1]+sonar_scans[pos+2]
    else:
        return 'end'
for i in range(len(sonar_scans)-1):
    if get_window(sonar_scans,i+1) != 'end':
        if get_window(sonar_scans,i+1) > get_window(sonar_scans,i):
           increased_value_count += 1



print(increased_value_count)

