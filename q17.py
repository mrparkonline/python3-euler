"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numToWord(n):
    """ Converts Num to Word -- Only for [1,999]
    --param
    n : int
    --return
    string : word of num
    """
    ones = ['zero','one','two','three','four','five','six','seven','eight','nine']
    tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tensSpecial = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    hundred = ' hundred and '

    strNum = str(n)

    if len(strNum) == 1:
        return ones[n]
    elif len(strNum) == 2:
        if strNum[0] == '1':
            return tens[int(strNum[1])]
        else:
            if strNum[1] == '0':
                return tensSpecial[int(strNum[0])-2]
            else:
                return tensSpecial[int(strNum[0])-2] + " " + ones[int(strNum[1])]
    else:
        if strNum[-1] == '0' and strNum[-2] == '0':
            return ones[int(strNum[0])] + ' hundred'
        else:
            return ones[int(strNum[0])] + hundred + numToWord(int(strNum[1:]))
# end of numToWord

wordNums = []
for i in range(1,1000):
    wordNums.append(numToWord(i))
wordNums += ['one thousand']

characterLength = 0
for i in wordNums:
    temp = i.replace(' ','')
    characterLength += len(temp)

print(characterLength) # 21124
