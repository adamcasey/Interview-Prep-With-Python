# Find two numbers in a list of whole positive integers whose sum is equal to the target: https://www.youtube.com/watch?v=wBXZD436JAg
# Optimized for speed/time but not for space: Complexity is O(n)
# Questions to ask: 
# 	Can you assume that the list will always have a valid answer?
# 	Is the goal to save space or time?
# 	Do you want multiple valid answers?
# 	Will '0' be in the list?
# 	Should I return 'null' or 'false' or just an empty string if not found?

def find_pairs(values, target):
	if target > 1:
		value_dict = {}
		for value in values:
			if value in value_dictr:
				value_dict[value] += 1
			else:
				value_dict[value] = 0
		
		for value in values:
			target_comp = target - value
			if target_comp in value_dict:
				if target_comp == value:
						if not value_dict[target_comp] > 0
								continue
				return str(value) + " and " + str(target_comp)
	
	return "No valid pairs"


print(find_pairs([14, 13, 6, 7, 8, 10, 1, 2], 3) == "1 and 2") #True, general
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 3) == "No valid pairs") #True, no matching pair exists
print(find_pairs([2, 2], 4) == "2 and 2") #True, duplicate numbers
print(find_pairs([2], 4) == "No valid pairs") #True, only one item in the list
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 0) == "No valid pairs") #True, target is 0
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 1) == "No valid pairs") #True, '1' requires two positive compliments
print(find_pairs([2], -1) == "No valid pairs") #True, negative target
print(find_pairs([], 4) == "No valid pairs") #True, empty list
