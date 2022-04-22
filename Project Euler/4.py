# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    str_n = str(n)
    if str_n[0:3] == str_n[-1:2:-1]:
        return True
    return False
max = 0
for i in range(999,800,-1):
    for j in range(999,800,-1):
        if i*j > max and is_palindrome(i*j):
            max = i*j

print(max)
#906609