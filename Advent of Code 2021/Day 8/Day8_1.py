# get lines
signals = []
# with open('day8_input_sample.txt', 'r') as infile:
#     for row in infile:
#         row = row.strip('\n').split('|')
#         pattern = row[0].split(' ')
#         if pattern[-1] == '':
#             pattern.pop()
#         output = row[1].split(' ')
#         if output[0] == '':
#             output.remove('')
#         signals.append((pattern, output))
# print(signals)
with open('day8_input.txt', 'r') as infile:
    for row in infile:
        row = row.strip('\n').split('|')
        pattern = row[0].split(' ')
        if pattern[-1] == '':
            pattern.pop()
        output = row[1].split(' ')
        if output[0] == '':
            output.remove('')
        signals.append((pattern, output))
print(signals)
unique_digit_lengths = [2,3,4,7]
digits_1478 = 0
for i in range(len(signals)):
    for output in signals[i][1]:
        if len(output) in unique_digit_lengths:
            digits_1478 +=1

print(digits_1478)