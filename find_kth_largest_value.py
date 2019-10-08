import random

# The 1st largest element is the largest element
def findKthLargest(arr, k):
  # Keep track of the 'left' and 'right' space in which the k'th largest element
  # can possibly be, we will use these bounds to know what section to actually partition \
  # around a chosen pivot. 

  n = len(arr)
  left = 0
  right = n - 1

  # Random object to use later repeatedly to choose random pivots
  #ranom_piv = random.randint(0, len(arr))

  while left <= right:
    # Pick a random pivot
    #choosenPivotIndex = random.randint(0 , (right - left + 1)) + left
    choosenPivotIndex = random.randint(left , right)
    #print("choosenPivotIndex: {}".format(choosenPivotIndex))
    # Execute the actual partitioning and get back the final position \
    # of the pivot we choose after partitioning is over
    finalIndexOfChoosePivot = partition(arr, left, right, choosenPivotIndex)
    
    if (finalIndexOfChoosePivot == n - k):
      return arr[finalIndexOfChoosePivot]
    elif (finalIndexOfChoosePivot > n - k):
      right = finalIndexOfChoosePivot - 1
    else:
      left = finalIndexOfChoosePivot + 1

  return - 1

def partition(arr, left, right, pivotIndex):
  pivotValue = arr[pivotIndex]
  #print("pivotValue: {}".format(pivotValue))
  lesserItemsTailIndex = left
  #print("lesserItemsTailIndex: {}".format(lesserItemsTailIndex))
  swap_help(arr, pivotIndex, right)

  for i in range(left, right, 1):
    if arr[i] < pivotValue:
      swap_help(arr, i, lesserItemsTailIndex)
      lesserItemsTailIndex += 1

  swap_help(arr, right, lesserItemsTailIndex)

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
