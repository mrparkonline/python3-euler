# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(item):
    """ This determines if the parameter is a palindrome
    --param
    item : num or string preferred
    --returns
    boolean : true if a palindrome, false otherwise
    """
    item = str(item)
    return item == item[::-1]
# end of isPalindrome

products = [x*y for x in range(100,1000) for y in range(100,1000)]
palindromicNumbers = list(filter(isPalindrome, products))
palindromicNumbers.sort()
print(palindromicNumbers[-1])
