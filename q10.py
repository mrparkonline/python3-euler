# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

noEvens = [x for x in range(3,2000001) if x % 2 != 0]

# Idea:
# - Remove all evens except 2
# - Make all 2 + odd numbers < two million keys
# - Set all values to True
# 01/21/2017 ... too slow
# 01/22/2017 ... Sieve with Dictionary

primes = {}
for i in noEvens:
    primes[i] = True

for a in primes.keys():
    if primes[a]:
        for b in range(a+a,2000001,a):
            if b in primes.keys():
                if b % a == 0:
                    primes[b] = False


allPrimes = [2] + [x for (x,y) in primes.items() if y]
print(len(allPrimes)) # Number of Primes under 2,000,000 = 148933
# https://primes.utm.edu/howmany.html
print(sum(allPrimes)) # 142913828922
