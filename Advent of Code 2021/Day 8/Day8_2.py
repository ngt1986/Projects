# get lines
signals = []
# with open('day8_input_sample.txt', 'r') as infile:
#     for row in infile:
#         row = row.strip('\n').split('|')
#         pattern = row[0].split(' ')
#         if pattern[-1] == '':
#             pattern.pop()
#         for i in range(len(pattern)):
#             sorted_chars = sorted(pattern[i])
#             pattern[i] = ''.join(sorted_chars)
#         output = row[1].split(' ')
#         if output[0] == '':
#             output.remove('')
#         for i in range(len(output)):
#             sorted_chars = sorted(output[i])
#             output[i] = ''.join(sorted_chars)
#         signals.append((pattern, output))
# print(signals)
with open('day8_input.txt', 'r') as infile:
    for row in infile:
        row = row.strip('\n').split('|')
        pattern = row[0].split(' ')
        if pattern[-1] == '':
            pattern.pop()
        for i in range(len(pattern)):
            sorted_chars = sorted(pattern[i])
            pattern[i] = ''.join(sorted_chars)
        output = row[1].split(' ')
        if output[0] == '':
            output.remove('')
        for i in range(len(output)):
            sorted_chars = sorted(output[i])
            output[i] = ''.join(sorted_chars)
        signals.append((pattern, output))
# print(signals)

def digits_1478(signals, digits):
    for signal in signals[0]:
        if len(signal) == 2:
            digits[1] = signal
        elif len(signal) == 3:
            digits[7] = signal
        elif len(signal) == 4:
            digits[4] = signal
        elif len(signal) == 7:
            digits[8] = signal
    return digits

def digits_9(signals, digits):
    for signal in signals[0]:
        if len(signal) == 6:
            if digits[1][0] in signal and digits[1][1] in signal and digits[4][0] in signal and digits[4][1] in signal and digits[4][2] in signal and digits[4][3] in signal:
                digits[9] = signal
                return digits

def digits_56(signals, digits):
    sixes = []
    for signal in signals[0]:
        if len(signal) == 6 and signal not in digits:
            sixes.append(signal)
    for signal in signals[0]:
        if len(signal) == 5:
            for six_signal in sixes:
                if string_compare(six_signal, signal) == 1:
                    digits[5] = signal
                    digits[6] = six_signal
                    return digits
def digits_23(signals, digits):
    fives = []
    for signal in signals[0]:
        if len(signal) == 5 and signal not in digits:
            fives.append(signal)
    for fives_signal in fives:
        if digits[1][0] in fives_signal and digits[1][1] in fives_signal:
            digits[3] = fives_signal
        else:
            digits[2] = fives_signal
    return digits

def string_compare(s1, s2):
    uncommons = 0
    for i in range(len(s1)):
        if s1[i] not in s2:
            uncommons += 1
    return uncommons
output_sum = 0
for i in range(len(signals)):
    digits = ['', '', '', '', '', '', '', '', '', '']
    digits = digits_1478(signals[i],digits)
    digits = digits_9(signals[i], digits)
    digits = digits_56(signals[i], digits)


    for signal in signals[i][0]:
        if len(signal) == 6 and signal not in digits:
            digits[0] = signal
            break
    digits = digits_23(signals[i], digits)

    factor = 1000
    signal_output = 0
    for j in range(len(signals[i][1])):
        signal_output += factor*digits.index(signals[i][1][j])
        factor = factor/10
    output_sum += signal_output

print(output_sum)
