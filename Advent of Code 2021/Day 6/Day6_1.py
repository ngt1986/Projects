# get lines
fishes = []
# with open('day6_input.txt', 'r') as infile:
#     for row in infile:
#         row = row.split(',')
#         for digit in row:
#             fish.append(int(digit))

def lanternfish(fish, days):
    day = 0
    while day < days:
        day += 1
        j = len(fish)
        i = 0
        while i < j:
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
                i+=1
            else:
                fish[i] -= 1
                i +=1
        # print(fish)
    return len(fish)
for i in range(0,9):
    print("i = ",i, ":", lanternfish([i],4), lanternfish([i],16),lanternfish([i], 32), lanternfish([i], 64),lanternfish([i], 128))
