# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
c = 0
triplet = []
for a in range(1,1000):
    for b in range(1,1000):
        if a + b < 1000:
            c = 1000- (a + b)
            if a**2 + b**2 == c**2:
                triplet.append((a,b,c))
print(triplet)
print(triplet[0][0]*triplet[0][1]*triplet[0][2])