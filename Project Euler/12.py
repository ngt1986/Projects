
# DID NOT COMPLETE

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

import math
import numpy as np

def primes(n):
    array = [1]*(n+1)
    primes_to_divide_by = []
    for i in range(2,n+1):
        if array[i] == 1:
            j = i**2
            k = 1
            while j <= n:
                array[j] = 0
                j = i**2 + k * i
                k +=1

    primes_to_divide_by = [i for i in range(len(array)) if array[i] == 1]
    primes_to_divide_by.remove(0)
    primes_to_divide_by.remove(1)
    return primes_to_divide_by

def div_by_primes(n,prime, count = None):
    if count is None:
        count = 0
    if n % prime ==0:
        if n / prime == prime:
            count+=1
            return count
        else:
            count+=2
            return div_by_primes(n/prime, prime, count)
    return count

found = False
i = 8
sum = 28
while not found:
    sum=76576500 #did not complete
    i+=1
    divisors = 2
    primes_to_divide_by = primes(math.ceil(sum ** (1 / 2)))
    for prime in primes_to_divide_by:
        divisors += div_by_primes(sum, prime)
    if divisors>30:
        found = True
print(sum,i-1, divisors)