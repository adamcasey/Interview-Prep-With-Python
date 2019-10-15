'''
The only difference between LIS and LNDS (Longest Non-Decreasing Subsequence) is one change.
We change "nums[i] > nums[j]" to "nums[i] >= nums[j]". We basically just change the conditions that allow us to consider an item for lengthening any longest subsequence already found.
'''

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    
    '''
    Array to store our subproblems, default answer is 1. A single
    item is neither increasing or decreasing, kind of a middle ground.

    Each index records the answer to "what is the longest increasing
    subsequence ending at index i of the original array?"
    '''
    
    maxLength = [1 for _ in range(len(nums))]

    # By default, the best answer is a length of 1
    maxSoFar = 1
    # Test every possible end index of a longest increasing subsequence
    for i in range(1, len(nums)):
        '''
      We aim to see if we can append the item at nums[i]
      to extend the Longest Increasing Subsequence achieved
      from index 0...j (which is what the cache records)

      We want to solve for maxLength[i] if the value at 'i'
      beats 'j'. If we can we see which is greater between
      these then we have our answer:

      1.) maxLength[i]: The best answer so far for the LIS from 0...i

      2.) maxLength[j] + 1: The value of maxLength[j] is the length
      of the LIS from 0...j, we conceptually "append" this item to
      that LIS by adding 1 to that subproblem answer, yielding a
      potentially new answer for LIS[0..i]  
        '''
        for j in range(0, i):
            if nums[i] >= nums[j]:
                maxLength[i] = max(maxLength[i], maxLength[j] + 1)
        # We now have an answer for LIS[0...i] so we compare it against the best LIS length found so far
        maxSoFar = max(maxSoFar, maxLength[i])

    return maxSoFar
                       
if __name__ == '__main__':
    
    numSequence = [-1,3,4,5,2,2,2,2]
                       
    print(lengthOfLIS(numSequence))
