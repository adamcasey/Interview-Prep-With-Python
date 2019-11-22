def canPartitionKSubsets(nums, k):
  '''
  Get the sum of all items in the list, We will use this to divide by k to get the sum that each bucket needs to hit
  '''
  
  totalSum = sum(nums)
  if ( k<= 0 or k > len(nums) or totalSum % k != 0 ):
    return False
	
	used = [0] * len(nums)
	return canPartition(0, nums, used, k, 0, totalSum // k)
	
def canPartition(iterStart, numList, usedList, k, inProgressBucketSum, targetBucketSum):
	if k == 1:
		return True
		
	if inProgressBucketSum == targetBucketSum:
		return canPartition(0, numsList, usedList, k - 1, 0, targetBucketSum)
		
	for index in range(iterStart, len(numList)):
		'''
		If the number hasn't been used yet and the sum of it plus what's already in the bucket is less than \
		the total the bucket can hold
		'''
		if not usedList[index] and ( inProgressBucketSum + numList[index] <= targetBucketSum ):
			# Indicate it's been used
			usedList[index]
			# Recurse ?
			if canPartition(iterStart + 1, numList, usedList, k, inProgressBucketSum + numList[index], targetBucketSum):
				return True
				
			usedList[index] = False
			
	return False
	
	
nums = [10,10,10,7,7,7,7,7,7,6,6,6]
k = 3 # True
nums = [4,3,2,3,5,2,1]
k = 4 # True
print(canPartitionKSubsets(nums, k))
		
