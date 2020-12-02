
puzzle_input = []
with open("day1input.txt", 'r') as infile:
    for row in infile:
        puzzle_input.append(int(row[0:4]))

print(puzzle_input)

for num in puzzle_input:
    for i in range(0, len(puzzle_input)):
        if num + puzzle_input[i] > 2020:
            continue
        for j in range(0, len(puzzle_input)):
            if num + puzzle_input[i] + puzzle_input[j] == 2020:
                print(num, puzzle_input[i], puzzle_input[j])
                print(num * puzzle_input[i] * puzzle_input[j])