import numpy as np

def pascal(n):
    arr = np.ones((n+1,n+1))
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr

print(pascal(20))
# print(a[-1][-1])
