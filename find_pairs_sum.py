# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

# Find two numbers in a list of whole positive integers whose sum is equal to the target: https://www.youtube.com/watch?v=wBXZD436JAg
# Optimized for speed/time but not for space: Complexity is O(n)
# Questions to ask: 
#   Can you assume that the list will always have a valid answer?
#   Is the goal to save space or time?
#   Do you want multiple valid answers?
#   Will '0' be in the list?
#   Should I return 'null' or 'false' or just an empty string if not found?

def find_pairs_brute(values, target):
    # target needs to be greater than 1 or else it won't have a positive whole integer compliment
    if target > 1:
        for index, each_value in enumerate(values):
            #print("each_value: {}".format(each_value))
            for next_value in range(index + 1, len(values)):
                #print("values[next_value]: {}".format(values[next_value]))
                if each_value + values[next_value] == target:
                    print("each_value: {} + next_value: {} = {}".format(each_value, values[next_value], target))
    return "No valid pairs"   
            
    


def find_pairs(values, target):
    if target > 1:
        # Create a dictionary (hashmap) to hold all the values
        value_dict = {}
        for value in values:
            # Check for duplicates
            if value in value_dict:
                value_dict[value] += 1
            # No duplicate exists
            else:
                value_dict[value] = 0
        # .items() method is used to return the list with all dictionary keys with values
        #print("value_dict: {}".format(value_dict.items()))

        # Now go through the list of values again to check if a number's compliment exists
        for value in values:
            target_comp = target - value
            # Is that compliment in the dictionary?
            if target_comp in value_dict:
                # Check if it's a duplicate of itself
                if target_comp == value:
                    #print(value_dict[target_comp])
                    # If a duplicate it will have a value of 1
                    # In the case of just one item in the dictionary, the sole key:value
                    # will have a value of 0
                    if not value_dict[target_comp] > 0:
                        continue
                return str(value) + " and " + str(target_comp)

    return "No valid pairs"

print(find_pairs([14, 13, 6, 7, 8, 10, 1, 2], 3)) #True, general
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 3)) #True, no matching pair exists
print(find_pairs([2, 2], 4)) #True, duplicate numbers
print(find_pairs([2], 4)) #True, only one item in the list
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 0)) #True, target is 0
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 1)) #True, '1' requires two positive compliments
print(find_pairs([2], -1)) #True, negative target
print(find_pairs([], 4)) #True, empty list

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(find_pairs_brute([14, 13, 6, 7, 8, 10, 1, 2], 3)) #True, general
print(find_pairs_brute([14, 13, 6, 7, 8, 10, 1], 3)) #True, no matching pair exists
print(find_pairs_brute([2, 2], 4)) #True, duplicate numbers
print(find_pairs_brute([2], 4)) #True, only one item in the list
print(find_pairs_brute([14, 13, 6, 7, 8, 10, 1], 0)) #True, target is 0
print(find_pairs_brute([14, 13, 6, 7, 8, 10, 1], 1)) #True, '1' requires two positive compliments
print(find_pairs_brute([2], -1)) #True, negative target
print(find_pairs_brute([], 4)) #True, empty list
