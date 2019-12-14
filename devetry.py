#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'priceCheck' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY products
#  2. FLOAT_ARRAY productPrices
#  3. STRING_ARRAY productSold
#  4. FLOAT_ARRAY soldPrice
#

def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    # Keep track of errors
    errors = 0
    # Make dictionary of products for constant lookup
    productMap = {}
    for index, item in enumerate(products):
        # Get the price for each product using the index
        productMap[item] = productPrices[index]
    #print("productMap: ", productMap)

    # Now check the prices of productsSold
    for index, itemSold in enumerate(productSold):
        realPrice = productMap[itemSold]
        # Check if the real price is different than the price of the sold product
        if realPrice != soldPrice[index]:
            # Found and error so increment count
            errors += 1

    return errors
if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from itertools import combinations
# Note: I keep getting a memory error on larger input?

def shortestSubstring(s):
    # Write your code here

    # Get all the substrings
    #subStringList = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    # Get all substrings using combinations
    #subStringList = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]
    for letter in range(0, len(s)):

    # Make a set out of s to find out if we have all the characters
    stringSet = set(s)
    
    validSubStrings = []

    # Make a set  of each subString and get difference with stringSet to see if it has all the letters
    for eachWord in subStringList:
        # If the difference is 0 then eachWord has all the letters
        setWord = set(eachWord)
        difference = stringSet.difference(setWord)

        if len(difference) == 0:
            # Add to the list of valid subStrings
            validSubStrings.append(eachWord)

    shortestSubString = min(validSubStrings, key=len)
    print("Shortest substring is: ", min(validSubStrings, key=len))
    return len(shortestSubString)
if __name__ == '__main__':
