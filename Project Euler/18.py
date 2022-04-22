cache = [1, 2]

n = 32
for i in range(2,n):
    cache.append(cache[i-1]+cache[i-2])
sum_even_fibs = 0
for digit in cache:
    if digit %2 == 0:
        sum_even_fibs+=digit
print(sum_even_fibs)

