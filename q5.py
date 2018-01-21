# 2520 is the smallest number
# that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

import math
def primeFactors(n):
    """ This function returns a list of prime factors for n
    --param
    n : integer
    --return
    list : prime factors of n
    """
    if n < 2:
        return []
    elif n in {2,3}:
        return [(n,1)]
    else:
        factors = []
        exponent = 0
        while n % 2 == 0:
            exponent += 1
            n //= 2
        # end of while
        if exponent != 0:
            factors.append((2,exponent))
        # end of 2
        for i in range(3,n+1,2):
            exponent = 0
            while n % i == 0:
                #factors.append(i)
                exponent += 1
                n //= i
            # end of while
            if exponent != 0:
                factors.append((i,exponent))
        else:
            if not(factors):
                factors.append((n,1))
        return factors
#end of primeFactors

def smallestProduct(upperLimit):
    """ The function determines the smallest positive number that is evenly
    divisible by [1,upperLimit]
    --param
    upperLimit : int
    --return
    integer : smallest product
    """

    # Creating a set of prime factorization with no duplicates factors
    primeSet = set()
    for i in range(2,upperLimit+1):
        for j in primeFactors(i):
            primeSet.add(j)
    # end of for

    # Creating a dictionary of prime factorization with greatest exponents
    greatestExponent = {}
    for (x,y) in primeSet:
        if x not in greatestExponent.keys():
            greatestExponent[x] = y
        else:
            if y > greatestExponent[x]:
                greatestExponent[x] = y

    # Creating a total product of the prime factor with its greatest exponent
    total = 1
    for key in greatestExponent:
        total *= (key**greatestExponent[key])

    # Fail Safe Check, returns -1 if the total product is not divisible by [1,upperLimit]
    for i in range(2,upperLimit+1):
        if total % i != 0:
            print("%d: Fail" % i)
            return -1
    else:
        return total

# end of smallestProduct

print(smallestProduct(10))
