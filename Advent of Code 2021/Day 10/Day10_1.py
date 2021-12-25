# get lines
lines = []
# with open('day10_input_sample.txt', 'r') as infile:
#     for row in infile:
#         row = row.strip('\n')
#         lines.append(row)
with open('day10_input.txt', 'r') as infile:
    for row in infile:
        row = row.strip('\n')
        lines.append(row)


def check_corrupt(line, stack = None, wrong_char = None):
    if stack is None:
        stack = []
        for char in line:
            stack.append(char)
    if wrong_char is None:
        wrong_char = ''
    modified = False
    for i in range(len(stack)-1):
        if stack[i] == '[' and stack[i+1] == ']':
            stack.pop(i)
            stack.pop(i)
            modified = True
        elif stack[i] == '(' and stack[i + 1] == ')':
            stack.pop(i)
            stack.pop(i)
            modified = True
        elif stack[i] == '{' and stack[i + 1] == '}':
            stack.pop(i)
            stack.pop(i)
            modified = True
        elif stack[i] == '<' and stack[i + 1] == '>':
            stack.pop(i)
            stack.pop(i)
            modified = True
        if modified:
            break
        if i == len(stack)-2:
            if ']' not in stack and ')' not in stack and '}' not in stack and '>' not in stack:
                wrong_char = "incomplete"
                return wrong_char
            else:
                wrong_char = find_wrong_char(stack)
                return wrong_char
    # print(stack)
    return check_corrupt(line, stack, wrong_char)

endables = [')','}',']','>']
def find_wrong_char(stack):
    for i in range(len(stack)):
        if stack[i] in endables:
            return stack[i]
def add_score(symbol):
    if symbol not in scorables:
        return 0
    else:
        if symbol == ')':
            return 3
        if symbol == ']':
            return 57
        if symbol == '}':
            return 1197
        if symbol == '>':
            return 25137
scorables = [')',']','}','>']
syntax_score = 0
for line in lines:
    symbol = check_corrupt(line)
    syntax_score += add_score(symbol)
print(syntax_score)
