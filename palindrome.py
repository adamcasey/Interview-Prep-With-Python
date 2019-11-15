'''
A permutation is an ordering of a set of items. 
Example: all permutations of 'tom':
    tom 
    tmo 
    omt 
    otm 
    mto 
    mot 
Not to be confused with a combination, which is an unordered set or subset.

Our approach is to check that each character appears an even number of times, \
allowing for only one character to appear an odd number of times (a middle character). 

This is enough to determine if a permutation of the input string is a palindrome. 

We iterate through each character in the input string, keeping track of the \
characters we’ve seen an odd number of times using a set unpaired_characters. 

As we iterate through the characters in the input string: 

If the character is not in unpaired_characters, we add it. 

If the character is already in unpaired_characters, we remove it. 

Finally, we just need to check if less than two characters don’t have a pair

Complexity: O(n) time, since we're making one iteration through the n characters
in the string. 

'''
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1

