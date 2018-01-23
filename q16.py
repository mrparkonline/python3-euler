# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def powerDigitSum(base, exp):
    """ Determines the digit sum of a power.
    --param
    base : int
    exp : int
    --return
    integer : digit sum
    """
    tempNum = base ** exp
    digits = [int(x) for x in str(tempNum)]

    return sum(digits)
# end of powerDigitSum

print(powerDigitSum(2,15))
print(powerDigitSum(2,1000))
