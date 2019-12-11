'''
Leetcode: 345 Reverse Vowels In A String:
  Runtime: 80 ms, faster than 23.75% of Python3 online submissions for Reverse Vowels of a String.
  Memory Usage: 13.8 MB, less than 93.33% of Python3 online submissions for Reverse Vowels of a String.

Write a function that takes a string as input and reverse only the vowels of a string.
  Example 1:
    Input: "hello"
    Output: "holle"
  Example 2:
    Input: "leetcode"
    Output: "leotcede"
  Note:
    The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        vowelList = ['a', 'e', 'i', 'o', 'u']
        newString = [""] * len(s)
        answerString = ""
        # Use two pointers (one at start and one at end of string)
        startIndex = 0
        endIndex = len(s) - 1
        
        # While the two pointers have not met
        while startIndex <= endIndex:
            # If current letter is a vowel
            if s[startIndex].lower() in vowelList:
                #print(f's[startIndex]: {s[startIndex]}')
                # Find vowel from other end to swap with
                if s[endIndex].lower() not in vowelList:
                    while s[endIndex].lower() not in vowelList:
                        # Current letter isn't a vowel so add it to the new string at its current location
                        newString[endIndex] = s[endIndex]
                        #print(f's[endIndex]: {s[endIndex]}')
                        # Decrement index
                        endIndex -= 1
                # Perform the swap with two vowels
                newString[endIndex] = s[startIndex]
                newString[startIndex] = s[endIndex]
                endIndex -= 1
            # Not a vowel so leave it in place
            else:
                newString[startIndex] = s[startIndex]
                newString[endIndex] = s[endIndex]
            # Increment index
            startIndex += 1
            #print(f'newString: {newString}')

        #answerString = "".join(newString)
        # Concatenate new string
        for letter in newString:
            #print(f'letter: {letter}')
            if letter == "":
                answerString += " "
            else:
                answerString += letter
      
        return answerString
