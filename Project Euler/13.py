# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# [see input]

num_arr = []
with open('13_input.txt','r') as infile:
    for row in infile:
        row = list(row.strip('\n'))
        arr_row = []
        for digit in row:
            arr_row.append(int(digit))
        arr_row.insert(0,0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        arr_row.insert(0, 0)
        num_arr.append(arr_row)
print(num_arr)

def add_rows(row1,row2):
    for i in range(len(row1)-1,-1,-1):
        if row2[i] + row1[i] > 9:
            row2[i] = (row2[i]+row1[i])-10
            row2[i-1] += 1
        else:
            row2[i] = row2[i] + row1[i]
    return row2

for i in range(len(num_arr)-1):

    num_arr[i+1] = add_rows(num_arr[i],num_arr[i+1])

print(num_arr[-1])
