# Heapsort Complexity:
# Best/Worst/Average Case: O(n * log(n))
# Binary Heaps are complete trees: 
#   A Binary Tree is complete Binary Tree if all levels are completely \
#   filled except possibly the last level and the last level has all keys \ 
#   as left as possible.

# To get the mapping of a binary tree from an array/list:
#   Parent: (i - 1) / 2  --> Where 'i' is the index of the element
#   leftChild: 2 * p + 1  --> Where 'p' is the index of the parent
#   rightChild: 2 * p + 2

import random

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(size-1)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

arr = [random.randint(0,100) for x in range(10)] 
print("arr before heap: {}".format(arr))
insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
print ("Max-Heap array: " + str(arr))
deleteNode(arr, 4)
print("After deleting an element: " + str(arr))


