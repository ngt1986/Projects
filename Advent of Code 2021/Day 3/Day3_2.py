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
diagnostic_report.sort()
# print(diagnostic_report)

# diagnostic_report = ['00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010']
# diagnostic_report.sort()

#Oxygen gen. rating, most common value
def oxy_gen(report, digit):
    if len(report) == 1:
        return report
    for i in range(len(report)):
        if int(report[i][digit]) == 1:
            if i <= len(report)/2:
                report = report[i::]
                return oxy_gen(report,digit+1)

            else:
                report = report[0:i]
                return oxy_gen(report, digit+1)
oxy_gen_binary = oxy_gen(diagnostic_report,0)

#co2 scrub rating, least common value
def co2_scrub(report, digit):
    if len(report) == 1:
        return report
    for i in range(len(report)):
        if int(report[i][digit]) == 1:
            if i <= len(report)/2:
                report = report[0:i]
                return co2_scrub(report,digit+1)

            else:
                report = report[i::]
                return co2_scrub(report, digit+1)
co2_scrub_binary = co2_scrub(diagnostic_report,0)


oxy_gen_converted = 0
co2_scrub_converted = 0
i = len(oxy_gen_binary[0])
while i > 0:
    if int(oxy_gen_binary[0][len(oxy_gen_binary[0])-i])==1:
        oxy_gen_converted += 2**(i-1)
    if int(co2_scrub_binary[0][len(co2_scrub_binary[0])-i]) == 1:
        co2_scrub_converted += 2 **(i-1)
    i -= 1

print(oxy_gen_converted,co2_scrub_converted,oxy_gen_converted*co2_scrub_converted)

