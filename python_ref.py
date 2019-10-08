'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# General Info:
# Algorithm run-times (best -> worst):
#	O(1)
#	O(log(n))
#	O(n)
#	O(n * log(n))
#	O(n^2)
#	O(n^3)
#	etc.

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Find the k'th largest element in a list
import random

# The 1st largest element is the largest element
# The kth largest element is n - k after the array is logically sorted
def findKthLargest(arr, k):
	
  # Keep track of the 'left' and 'right' space in which the k'th largest element
  # can possibly be, we will use these bounds to know what section to actually partition \
  # around a chosen pivot.
  n = len(arr)
  left = 0
  right = n - 1

	# While the bounds stay valid continue doing directed partitioning
  while left <= right:
    # Pick a random pivot --> except for the final index position the first time the loop is run
    choosenPivotIndex = random.randint(left , right)
    #print("choosenPivotIndex: {}".format(choosenPivotIndex))
		
    # Execute the actual partitioning and get back the final position \
    # of the pivot we choose after partitioning is over.
    finalIndexOfChoosePivot = partition(arr, left, right, choosenPivotIndex)
    
		# The pivot is index on index n - k. This is literally its final position if the list we were given had \
		# been sorted. Don't need to sort the whole list, just each portion of the list that hold's the kth element.
    if (finalIndexOfChoosePivot == n - k):
      return arr[finalIndexOfChoosePivot]
    elif (finalIndexOfChoosePivot > n - k):
      right = finalIndexOfChoosePivot - 1
    else:
      left = finalIndexOfChoosePivot + 1

  return - 1
# Basically just doing Quicksort
def partition(arr, left, right, pivotIndex):
  pivotValue = arr[pivotIndex]
  #print("pivotValue: {}".format(pivotValue))
  lesserItemsTailIndex = left
  #print("lesserItemsTailIndex: {}".format(lesserItemsTailIndex))
  swap_help(arr, pivotIndex, right)

	# Iterate from the left bound to 1 index right before the right bound (where \
	# the chosen pivot value is not sitting safely).
  for i in range(left, right, 1):
		# If this item is less than the 'pivotValue' then we need to move this item \
		# to the section of items "less than the pivot".
    if arr[i] < pivotValue:
      swap_help(arr, i, lesserItemsTailIndex)
      lesserItemsTailIndex += 1
	# Partitioning is done so swap the pivot item BACK into the space we just partitioned at the \
	# 'lesserItemsTailIndex' because that's where the pivot item belongs.
	# In the middle of the "sandwich"
  swap_help(arr, right, lesserItemsTailIndex)
	# Return the index of where we just put the pivot so that the caller knows its final resting place \
	# and the caller can make the decisions it needs.
  return lesserItemsTailIndex

def swap_help(arr, first, second):
  temp = arr[first]
  arr[first] = arr[second]
  arr[second] = temp

  #print("arr: {}".format(arr))

temp_list = [3, 2, 1, 5, 6, 4]
k = 2

# for _ in range(0, 100000):
#   if findKthLargest(temp_list, k) != 5:
#     print("failed somewhere")

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Knapsack
# Complexity:
# Time: O(n * k) where n is the number of types of cakes and k is the capacity \
# of the bad
# Space: O(k)
# If you cared more about time, it might be worth using a faster algorithm \
# that gives you a 'good' answer, even if it's not always the 'optimal' answer

def max_bag_value(cake_tuples, weight_cap):
  # Make a list to hold the max possible value at every bag weight capacity \
  # from 0 to weight_cap starting each index with value 0
  max_values_at_cap = [0] * (weight_cap +1)
  for current_capacity in range(weight_cap + 1):
    # Set a varaible to hold the max monetary valu so far for current_capacity
    current_max_value = 0

    for cake_weight, cake_value in cake_tuples:
      # If a cake weighs 0 and has a positive value the value of our \
      # bag is infinite!
      if cake_weight == 0 and cake_value != 0:
        # Advantage of using this way to return infinity is we get the 'behavior' \
        # of infinity. Compared to any other integer, float('inf') will be great.
        # And it's a nubmer, which can be an advantage or disadvantage --> \
        # You might want the result to always be the same type, but without manually \
        # checking you don't know if you mean an actual value or the special case of inf.
        return float('inf')

      # If the current cake weighs as much or less than the current weight capacity it's \
      # possible taking the cake would get a better value
      if cake_weight <= current_capacity:

        # So we  check: should we use the cake or not?
        # If we use the cake, the most kilograms we can include in addiiton \
        # to the cake we're adding is the current capacity minus the cake's \
        # weight. We find th emax value at that integer capacity in our list \
        # max_values_at_cap
        max_value_using_cake= (cake_value + max_values_at_cap[current_capacity - cake_weight])

        # Now we see if it's worth taking the cake. How does the value with the \
        # cake compare to the current_max_value?
        current_max_value = max(max_value_using_cake, current_max_value)

      # Add each capacity's max value to our list so we can use them 
      # when calculating all the remaining capacities
    max_values_at_cap[current_capacity] = current_max_value

  return max_values_at_cap[weight_cap]

# Test Case 1
cake_tuples_param = [(3, 40), (5, 70)]
capacity_param = 9
# Test Case 2
#cake_tuples_param = [(7, 160), (3, 90), (2,15)]
#capacity_param = 20
#Test Case 3
#cake_tuples_param = [(7, 160), (3, 90), (2,15)]
#capacity_param = 20

print(max_bag_value(cake_tuples_param, capacity_param))

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Compare Two Strings (case insensitive, not optimal)
# Time (always-case): O(n)
# Space: O(n)
def case_insensitive_compare(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_iter = iter(s1)
    s2_iter = iter(s2)
    # '_' means it's a variable meant to be discarded
    for _ in range(len(s1)):
        # grab the char on each string
        s1_c = next(s1_iter)
        #print(f's1_c: {s1_c}')
        s2_c = next(s2_iter)
        #print(f's1_c: {s2_c}')

        if not s1_c.upper() == s2_c.upper():
            return False
        
    return True

print(case_insensitive_compare("adam", "ADAM"))
print(case_insensitive_compare("adam", "Casey"))
print(case_insensitive_compare("adam", ""))
print(case_insensitive_compare("", ""))


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

# Fibonacci Numbers

def fibonacci(n):
  if n == 1 or n == 2: return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memoization(n):
  fibo = dict()
  def rec(n):
    if n in fibo: return fibo[n]

    if n == 1 or n == 2:
      fibo[n] = 1
    else:
      fibo[n] = rec(n - 1) + rec(n - 2)
    return fibo[n]
  return rec(n)

def fibonacci_bottom_up(n):
  if n == 1 or n == 2: return 1

  fib0 = 1
  fib1 = 1
  for i in range(3, n+1):
    new_fib = fib0 + fib1
    fib0 = fib1
    fib1 = new_fib
  return fib1

n = 10
print(fibonacci_memoization(n))
print(fibonacci_bottom_up(n))

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
def dpMakeChange(coinValueList, change ,minCoins, coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 31
    clist = [25, 10, 1]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
	
# Reverse a string
# Space Complexity = O(n)
# Time Complexity = O(n^2)
class ReverseString:
  def __init__(self):
    self.string_to_reverse = ""
    print(f"This is a test: {self.string_to_reverse}")
    #print("This is a test: {}".format(self.string_to_reverse))

  def reverse_string(self, string_param):
    string_list = [None] * (len(string_param))
    for index, char in enumerate(string_param):
      self.string_to_reverse = char + self.string_to_reverse
      print("index: {}".format(index))
      print("char: {}".format(char))
      string_list[index] = char
      #print(index)
    return (self.string_to_reverse, string_list)

if __name__ == '__main__':
  reverse_me = ReverseString()
  print(reverse_me.reverse_string("Adam"))
	

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

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
