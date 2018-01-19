# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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
        return [n]
    else:
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # end of while

        for i in range(3,math.floor(math.sqrt(n))+1,2):
            while n % i == 0:
                factors.append(i)
                n //= i
            # end of while
        # end of for
        if not(factors):
            factors = [n]

        return factors
# end of primeFactors

print(primeFactors(600851475143)[-1])
