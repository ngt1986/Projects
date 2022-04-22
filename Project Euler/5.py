# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

spn_not_found = True
i = 0

def div_1_thru_20(n):
    for i in range(1,21):
        if n%i != 0:
            return False
    return True

while spn_not_found:
    i+=20
    if div_1_thru_20(i):
        spn_not_found = False

print(i)
#232792560