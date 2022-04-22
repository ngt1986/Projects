# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

factors = []
def pf(n):
    for i in range(2,math.floor(n**(1/2))):
        if n % i == 0 and is_prime(i):
            factors.append(i)

pf(600851475143)
print(factors)

#[71, 839, 1471, 6857]