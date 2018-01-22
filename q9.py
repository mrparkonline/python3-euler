# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a*b*c.

import math

# Idea 3
# Rule 1: a < b
# Rule 2 square root (a^2 + b^2) must be not a decimal number

triplets = []
for a in range(3,997):
    for b in range(a+1,998):
        c = a**2 + b**2
        if math.sqrt(c) % 1 == 0:
            triplets.append((a,b,math.floor(math.sqrt(c))))

answer = 0
for (a,b,c) in triplets:
    if a+b+c == 1000:
        print((a,b,c))
        answer = a*b*c

print(answer) # 31875000
