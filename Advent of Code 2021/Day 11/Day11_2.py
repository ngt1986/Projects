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
                return incomplete_score(stack)
            else:
                return 0
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

def incomplete_score(stack, score = None):
    char = stack.pop()
    if score is None:
        score = 0

    if char == '(':
        score = score*5
        score += 1
    elif char == '[':
        score = score*5
        score += 2
    elif char == '{':
        score = score * 5
        score += 3
    elif char == '<':
        score = score * 5
        score += 4
    if len(stack) == 0:
        return score
    return incomplete_score(stack, score)


syntax_score = []
for line in lines:
    symbol = check_corrupt(line)
    syntax_score.append(symbol)
syntax_score.sort()
complete = False
while not complete:
    if syntax_score[0] == 0:
        syntax_score.pop(0)
    else:
        complete = True
print(syntax_score[26])
print(len(syntax_score))






