# get bingo numbers as list
with open('day4_input1.txt', 'r') as infile:
    for row in infile:
        row = row.split(',')
        numbers_called = [int(row[i]) for i in range(len(row))]


# print(numbers_called)  # len = 100
boards = [[]]
boards_marked = [[]]
board_num = 0
row_count = 0

#get boards as list of matrices
with open('day4_input2.txt','r') as infile:
    for row in infile:
        row_count += 1
        row = row.strip('\n').split(' ')
        board_row = []
        board_marked_row = []
        for i in range(len(row)):
            if row[i] != '':
                board_row.append(int(row[i]))
                board_marked_row.append(0)
        if row_count % 6 == 0:
            board_num +=1
            boards.append([])
            boards_marked.append([])
        else:
            boards[board_num].append(board_row)
            boards_marked[board_num].append(board_marked_row)

# #sample case
# numbers_called = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# boards = [[]]
# boards_marked = [[]]
# board_num = 0
# row_count = 0
#
# #get boards as list of matrices
# with open('day4_input2_sample.txt','r') as infile:
#     for row in infile:
#         row_count += 1
#         row = row.strip('\n').split(' ')
#         board_row = []
#         board_marked_row = []
#         for i in range(len(row)):
#             if row[i] != '':
#                 board_row.append(int(row[i]))
#                 board_marked_row.append(0)
#         if row_count % 6 == 0:
#             board_num +=1
#             boards.append([])
#             boards_marked.append([])
#         else:
#             boards[board_num].append(board_row)
#             boards_marked[board_num].append(board_marked_row)


def mark_boards(boards, boards_marked, num):
    for k in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[k][i][j] == num:
                    boards_marked[k][i][j] = 1

def check_bingo(board, board_marked):
    #check rows
    for row in board_marked:
        if sum(row) == 5:
            return True

    #check columns
    for j in range(5):
        sum_column = 0
        for i in range(5):
            if board_marked[i][j] == 1:
                sum_column+=1
        if sum_column == 5:
            return True
    return False

def get_score(board, board_marked,num):
    score = 0
    for i in range(5):
        for j in range(5):
            if board_marked[i][j] == 0:
                score += board[i][j]

    return score*num

bingoed_boards = [0]*len(boards)
print(bingoed_boards)
if sum(bingoed_boards) < len(boards):
    for i in range(len(numbers_called)):
        mark_boards(boards,boards_marked,numbers_called[i])
        if i > 3:
            bingos = 0
            for j in range(len(boards)):

                if check_bingo(boards[j],boards_marked[j]):
                    bingoed_boards[j] = 1
                    # print(bingoed_boards)
                    if sum(bingoed_boards) == len(boards)-1:
                        last_board_index = bingoed_boards.index(0)
                        score = get_score(boards[last_board_index], boards_marked[last_board_index], numbers_called[i])
                        print(score)