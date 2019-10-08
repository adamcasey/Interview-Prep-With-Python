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

