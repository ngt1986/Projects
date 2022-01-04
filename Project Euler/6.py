# The sum of the squares of the first ten natural numbers is, 385
#
# The square of the sum of the first ten natural numbers is, 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = 0
sum = 0
for i in range(1,101):
    sum_squares += i**2
    sum += i

print(sum_squares, sum)
print(sum**2-sum_squares)

# 338350 5050
# 25164150