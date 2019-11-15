#---------------------------------------
# Merge Sort
#---------------------------------------

import random

def merge(ls1, ls2):
    '''
    Helper function for MergeSort
    This function assumes both source arrays are sorted,
    then builds a result array by comparing the first
    elements from each and storing the lower one
    '''
    result = []
    # While both lists have an item
    while ls1 and ls2:
        print("ls1: {}".format(ls1))
        print("ls2: {}".format(ls2))
        # if ls1 element is less than ls2 element it goes into the final list first
        if ls1[0] < ls2[0]:
            result.append(ls1.pop(0))
        # ls2 element is smaller so it goes into the final list
        else:
            result.append(ls2.pop(0))
    print(f'result: {result} + ls1: {ls1} + ls2: {ls1}')
    combined = result + ls1 + ls2
    print(f'combined: {combined}')
    return combined

def MergeSort(ls):
    '''
    Sorts the input list using a recursive mergesort algorithm
    '''
    print(f'MergeSort call with ls: {ls}')
    if len(ls) > 1:
        mid = len(ls) // 2
        temp = merge(MergeSort(ls[:mid]),MergeSort(ls[mid:]))
        print(f'temp: {temp}')
        return temp
    else:
        return ls

random_list = [random.randint(0,100) for x in range(10)]
print("Unsorted: {}".format(random_list))
print("Sorted: {}".format(MergeSort(random_list)))
#print(MergeSort([]))
