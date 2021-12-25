diagnostic_report = []
with open('day3_input.txt', 'r') as infile:
    for row in infile:

        row= (row.strip('\n'))
        diagnostic_report.append(row)

print(diagnostic_report)  # len = 1000

gamma_rate = [0]*len(diagnostic_report[0])
epsilon_rate = [0]*len(diagnostic_report[0])
print(gamma_rate)
for num in diagnostic_report:
    for i in range(len(num)):
        gamma_rate[i] += int(num[i])
for i in range(len(gamma_rate)):
    if gamma_rate[i] > 500:
        gamma_rate[i] = 1
        epsilon_rate[i] = 0
    else:
        gamma_rate[i] = 0
        epsilon_rate[i] = 1
gamma_converted = 0
epsilon_converted = 0
i = len(gamma_rate)
while i > 0:
    if gamma_rate[12-i]==1:
        gamma_converted += 2**(i-1)
    else:
        epsilon_converted += 2 **(i-1)
    i -= 1
print(gamma_rate, gamma_converted)
print(epsilon_rate,epsilon_converted)

print(gamma_converted*epsilon_converted)