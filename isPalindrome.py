'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    Example 1:
        Input: 121
        Output: true
    Example 2:
        Input: -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
        Therefore it is not a palindrome.
    Example 3:
        Input: 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

import math 

class IsPalindrome_Solution:
    
    def isPalindrome_brute(self, x: int) -> bool:
        # First check if negative number
        if x < 0:
            return False
        
        numString = str(x)
        # Next check for odd/even length input
        if len(numString) % 2 == 0:
            leftIndex = rightIndex = math.floor(len(numString) // 2)
            leftIndex -= 1
        else:
            # Everything starts in the middle of the list
            middleIndex = math.floor(len(numString) // 2)
            leftIndex = middleIndex - 1
            rightIndex = middleIndex + 1
            
        # Make an array of each digit
        digitList  = []
        for eachNum in numString:
            digitList.append(eachNum)

        # Start at the middle index and go 'outwards' to check that each number matches
        while leftIndex >= 0 and rightIndex <= len(numString) - 1:
            if numString[leftIndex] != numString[rightIndex]:
                return False
            else:
                leftIndex -= 1
                rightIndex += 1
        return True
    
    def isPalindrome_better(self, x: int) -> bool:
        '''
        Special cases:
            As discussed above, when x < 0, x is not a palindrome.
            Also if the last digit of the number is 0, in order to be a palindrome, \
                the first digit of the number also needs to be 0.
            Only 0 satisfy this property.
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedNum = 0
        while x > revertedNum:
            revertedNum = revertedNum * 10 + x % 10
            # Don't forget to use '//' or else you'll get a decimal
            x //= 10
        '''
        When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        For example when the input is 12321, at the end of the while loop we get x = 12, \ 
            revertedNumber = 123, since the middle digit doesn't matter in palidrome(it will \ 
            always equal to itself), we can simply get rid of it.
        If either of these are True, it returns True
        If both are False, it returns False
        '''
        return x == revertedNum or x == revertedNum // 10
    
palindromeConst = IsPalindrome_Solution()

test_Num = 12345654321

print("{} is a Palindrome: {}".format(test_Num, palindromeConst.isPalindrome_brute(test_Num)))
print("{} is a Palindrome: {}".format(test_Num, palindromeConst.isPalindrome_better(test_Num)))
