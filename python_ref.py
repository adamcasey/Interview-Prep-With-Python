'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Longest Common Substring

# Brute force solution:
# For each substring of 'X' check if the substring exists in 'Y'.
# The longest existing substring is the answer.

# For each characters at indexes i and j from s1 and s2 we want to find the
# longest common substrings ending at those indexes. If the characters are
# same, we check if their neighboring characters are same as well. We do this
# until the characters are different. The overall time complexity of this will
# be O(mn^2).

# However, we can optimize this using dynamic programming. Instead of having to
# check the longest substring ending at neighboring characters at index i-1 and
# j-1, we could have stored longest substring for i-1 and j-1 in an array. This
# would bring down the complexity of O(nm)

# Dynamic programming solution
#   |   | a | b | c | d | x | y
# ------------------------------
#   | 0 | 0 | 0 | 0 | 0 | 0 | 0
# ------------------------------
# x | 0 | 0 | 0 | 0 | 0 | 1 | 0  
# ------------------------------
# z | 0 | 0 | 0 | 0 | 0 | 0 | 0
# ------------------------------
# b | 0 | 0 | 1 | 0 | 0 | 0 | 0
# ------------------------------
# c | 0 | 0 | 0 | 2 | 0 | 0 | 0
# ------------------------------
# d | 0 | 0 | 0 | 0 | 3 | 0 | 0
# ------------------------------

def longest_common_substring(x, y):
  # Get x and y lengths
  x_len, y_len = len(x), len(y)
  # Build the matrix
  dp = [[0 for _ in range(y_len+1)] for _ in range(x_len+1)]
  longest_subs_length = 0
  # Answer will be in lower right hand corner
  for i in range(1, x_len+1):
    for j in range(1, y_len+1):
      if x[i-1] == y[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
        if dp[i][j]  > longest_subs_length:
          longest_subs_length = dp[i][j]
  for row in dp:
    print(row)
  return longest_subs_length

print(longest_common_substring('zxabcdezy', 'yzabcdezx'))
print(longest_common_substring('abcdxyz', 'xyzabcd'))
print(longest_common_substring('GeeksforGeeks', 'GeeksQuiz'))
print(longest_common_substring("AdamAdamAdam", "MadamMadamMadam"))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#Backpack/knapsack problem

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Fibonacci Numbers

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Quicksort
# Best Case: O(n log n)
# Worst Case: O(n^2)
from random import randrange, random
import random

def partition(unsorted_list, start, end, pivot):
    unsorted_list[pivot], unsorted_list[end] = unsorted_list[end], unsorted_list[pivot]
    store_index = start
    for i in range(start, end):
        if unsorted_list[i] < unsorted_list[end]:
            unsorted_list[i], unsorted_list[store_index] = unsorted_list[store_index], unsorted_list[i]
            store_index += 1
    unsorted_list[store_index], unsorted_list[end] = unsorted_list[end], unsorted_list[store_index]
    return store_index

def quick_sort(unsorted_list, start, end):
    if start >= end:
        return unsorted_list
    pivot = randrange(start, end + 1)
    new_pivot = partition(unsorted_list, start, end, pivot)
    quick_sort(unsorted_list, start, new_pivot - 1)
    quick_sort(unsorted_list, new_pivot + 1, end)

def sort(unsorted_list):
    quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    return unsorted_list

list_to_sort = [random.randint(0,100) for x in range(10)]
#print("list_to_sort: {}".format(list_to_sort))
print (sort([]))
print (sort([1, 3, 4, 2]))
print (sort([5, 3, 22, 3, -19, 5]))
print(sort(list_to_sort))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Mergesort
# The merge function does a O(1)O(1) (constant) number of operations for each element in the list. 
# The list size is O(n)O(n) since there are nn elements. 
# Merge does a constant amount of work O(n)O(n) times, so merge runs in O(n)O(n) time.

# import random

# def merge(ls1, ls2):
#     '''
#     Helper function for MergeSort
#     This function assumes both source arrays are sorted,
#     then builds a result array by comparing the first
#     elements from each and storing the lower one
#     '''
#     result = []
#     while ls1 and ls2:
#         if ls1[0] < ls2[0]:
#             result.append(ls1.pop(0))
#         else:
#             result.append(ls2.pop(0))
#     return result + ls1 + ls2

# def MergeSort(ls):
#     '''
#     Sorts the input list using a recursive mergesort algorithm
#     '''
#     if len(ls) > 1:
#         mid = len(ls) // 2
#         return merge(MergeSort(ls[:mid]),MergeSort(ls[mid:]))
#     else:
#         return ls

# #print(merge([3,5,7,9],[2,4,6,8,10,12]))    
# print(MergeSort([7,13,2,9,17,4,6,1]))
# print(MergeSort([]))

# random_list = [random.randint(0,100) for x in range(10)]


# print(MergeSort(random_list))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

import random
random_list = [random.randint(0,100) for x in range(10)]
print("Before sorting: {}".format(random_list))
print("After sorting: {}".format(merge_sort(random_list)))

print("Empty list: {}".format(merge_sort([])))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Make change using least amount of coins
def min_coins(cents):
	if cents < 1:
		return 0
	coins = [25, 10, 5, 1]
	num_of_coins = 0
	for coin in coins:
		num_of_coins += cents // coin #python3 --> use //
		cents = cents % coin
		if cents == 0:
			break
	return num_of_coins

print(min_coins(31))#3
print(min_coins(33))#5
print(min_coins(1))#1
print(min_coins(0))#0

# Make change using least amount of coins --> Dynamic Programming
def min_coins_dp(cents)"
num_of_coins = [0] * (cents * 1)
num_of_coins[0] = 0
coins = [25, 10, 5, 1]
for i in range(1, cents + 1):
	temp = cents + 1
	for j in coins :
		coins_j = i // j
		if coins_j != 0:
			temp = min(temp, coins_j + num_of_coins[cents - coins_j * j])
	num_of_coins[i] = temp
return num_of_coins[cents]

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

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

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
