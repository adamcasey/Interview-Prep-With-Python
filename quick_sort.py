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