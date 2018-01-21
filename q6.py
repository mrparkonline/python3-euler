#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def sumSquares(upperLimit):
    """ Returns the sum of squares from [1, upperLimit]
    --param
    upperLimit : integer
    --return
    sum of squares : integer
    """
    squares = [x**2 for x in range(1,upperLimit+1)]

    return sum(squares)
# end of sumSquares

def squareSum(upperLimit):
    """ Returns the square of the sum of [1,upperLimit]
    --param
    upperLimit : integer
    --return
    square of sums : integer
    """
    totalSum = sum(list(range(1,upperLimit+1)))

    return (totalSum ** 2)
# end of squareSum

def differenceSolver(upperLimit):
    """ Returns the difference between squareSum(upperLimit) and sumSquares(upperLimit)
    --param
    upperLimit : integer
    --return
    difference : integer
    """

    return (squareSum(upperLimit) - sumSquares(upperLimit))
# end of differenceSolver

print(differenceSolver(10))
print(differenceSolver(100))
