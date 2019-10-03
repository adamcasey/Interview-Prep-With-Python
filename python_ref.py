# Quicksort

# Mergesort

# Make change using least amount of coins
def min_coins(cents):
	if cents < 1:
		return 0
	coins = [25, 10, 5, 1]
	num_of_coins = 0
	for coin in coins:
		num_of_coins += cents // coins #python3 --> use //
		cents = cents % coins
		if cents == 0:
			break
	return num_of_coins

min_coins(31)#3
min_coins(33)#5
min_coins(1)#1
min_coins(0)#3


# Reverse a string
# Space Complexity = O(n)
# Time Complexity = O(n^2)
class ReverseString:
  def __init__(self):
    self.string_to_reverse = ""
    print(f"This is a test: {self.string_to_reverse}")
    #print("This is a test: {}".format(self.string_to_reverse))

  def reverse_string(self, string_param):
    for char in string_param:
      self.string_to_reverse = char + self.string_to_reverse
    return (self.string_to_reverse)

if __name__ == '__main__':
  reverse_me = ReverseString()
  print(reverse_me.reverse_string("Adam"))

# Sort a Python Dictionary by values
def sort_dict_by_value(dict_param):
  sorted_dict = sorted(dict_param.items(), key=lambda x: x[1])
  return sorted_dict

if __name__ == '__main__':
  print(sort_dict_by_value({'a': 4, 'b': 3, 'c': 2, 'd': 1}))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


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
