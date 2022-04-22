# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million

import math
primes = [2,3,5,7,11,13]
i=13

def is_prime(n):
    for i in range(2,math.floor(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

while i < 2000000:
    i +=1
    if is_prime(i):
        primes.append(i)

print(sum(primes))
#142913828922