"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatzSet(upperLimit):
    """ The following function creates dataSet of collatz sequence under the upperLimit
    --param:
    upperLimit : int
    --return:
    dictionary
    """

    def collatz(n):
        """ Find the next collatz value dependant on n
        --param:
        n : int
        --return:
        int : the collatz value
        """
        if n % 2 == 0:
            return n // 2
        else:
            return 3*n + 1
    # end of collatz

    data = {} # Initialization
    data[1] = [1] # Base

    def collatzSequence(start):
        """ Creates the collatz sequence
        --param:
        start : int
        --return
        list : collatz sequence
        """
        nextValue = collatz(start)
        if nextValue in data.keys():
            return [start] + data[nextValue]
        else:
            return [start] + collatzSequence(nextValue)

    for i in range(2,upperLimit):
        if i not in data.keys():
            data[i] = collatzSequence(i)

    return data


user_input = int(input('Limit: '))
c_sequence = collatzSet(user_input)
lengthList = [(len(b),a) for a,b in c_sequence.items() if a < user_input]
print(max(lengthList))

# 837799
# Length of 525
# Could be faster
