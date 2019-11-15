# Largest Range

# Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.

# Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# Sample output: [0, 7]

# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    # Dictionary/hashmap to store numbers in array at first and then to help reduce 
    # checking duplicates
    nums = {}
    # Just put the number in the dictionary and mark it True for existing in the array
    for num in array:
        nums[num] = True
    # Now go trhough the array again
    for num in array:
        if not nums[num]:
            continue
        # Change to False so that we don't test its range again later on
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        # Go left and right from num as long as either direction gives you a valid number
        # meaning that directional number is in our original array\
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        # Did we find a better solution?
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange




test_case_1 = [1]  #[1,1]
test_case_2 = [1, 2]  #[1, 2])
test_case_3 = [4, 2, 1, 3] #[1, 4])
test_case_4 = [4, 2, 1, 3, 6]  #[1, 4])

test_case_5 = [8, 4, 2, 10, 3, 6, 7, 9, 1]  #[6, 10])
test_case_6 = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] #[0, 7])
test_case_7 =[19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14] #[10, 19])
test_case_8 =[0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14] #[-1, 19])
test_case_9 =[0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2] # [-7, 7])
test_case_10 = [0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2] #[-7, 7])
test_case_11 = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2] #[-8, 19]

print(largestRange(test_case_1))
print(largestRange(test_case_2))
print(largestRange(test_case_3))
print(largestRange(test_case_4))
print(largestRange(test_case_5))
print(largestRange(test_case_6))
print(largestRange(test_case_7))
print(largestRange(test_case_8))
print(largestRange(test_case_9))
print(largestRange(test_case_10))
print(largestRange(test_case_11))