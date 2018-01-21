# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math
def isPrime(n):
    """ Made to check if n is a prime number
    --param
    n : integer
    --return
    boolean : True if n is prime , False if not or < 2
    """

    if n < 2:
        return False
    elif n in {2,3}:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,math.floor(math.sqrt(n))+1,2):
            if n % i == 0:
                return False
        else:
            return True
# end of isPrime

def nPrime(n):
    """ Made to determine the nth prime number
    --param
    n : integer
    --return
    nth prime : integer
    """

    start = 1
    while n != 1:
        start += 2
        if isPrime(start):
            n -= 1
        # end of if

    return start
# end of nPrime

print(nPrime(6))
print(nPrime(10001))
