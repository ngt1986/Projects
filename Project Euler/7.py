# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import math
primes = [2,3,5,7,11,13]
i=13

def is_prime(n):
    for i in range(2,math.floor(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

# while len(primes)<20:
while len(primes)<10001:
    i +=1
    if is_prime(i):
        primes.append(i)


print(primes[-1])
#104743