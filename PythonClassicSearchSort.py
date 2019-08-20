"""Binary Search avg,wst O(logn), bst O(1), space O(1), sorted values"""
import random
ints = []
for i in range(40):
    num = random.randint(1,100)
    ints.append(num)
print(ints)
sortid = sorted(ints)
print(sortid)  

num_list = [2, 3, 4, 7, 8, 8, 9, 10, 11, 12, 18, 23, 26, 27, 28, 36, 40, 40, 41, 42, 43, 50, 57, 61, 63, 64, 68, 69, 75, 76, 77, 77, 86, 86, 87, 87, 87, 93, 93, 99]

def binary_search(n, lst):
    mid = len(lst)//2
    if n == lst[mid]:
        return n
    elif n > lst[mid]:
        #return lst[mid +1:]
        return binary_search(n, lst[mid +1:])
    elif n < lst[mid]:
        #return lst[:mid]
        return binary_search(n, lst[:mid]) 

print(binary_search(23, num_list))


"""Linear Search avg wst O(n), space O(1)"""


nums_list = [2, 3, 4, 7, 8, 8, 9, 10, 11, 12, 18, 23, 26, 27, 28, 36, 40, 40, 41, 42, 43, 50, 57, 61, 63, 64, 68, 69, 75, 76, 77, 77, 86, 86, 87, 87, 87, 93, 93, 99]
def linear_search(n, lst):
    for i in range(len(lst)):
        if lst[i] == n:
            return "The number you are looking for is at index: " + i
        else:
            return "The number you are looking for is not in this list."    
print(linear_search(23, nums_list))


"""Bubble Sort avg wst O(n^2), space O(1)"""
ints = []
for i in range(40):
    num = random.randint(1,100)
    ints.append(num)
print(ints)
print()

def bubble_sort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(0, l-i-1):
            if lst[j] > lst[j+1]:
               lst[j],lst[j+1] = lst[j+1], lst[j]
               
    return lst
print(bubble_sort(ints))
print()

"""Selection Sort avg wst O(n^2), space O(1)"""
def selection_sort(lst):
    for i in range(0,len(lst)-1):
        minimum_index = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] < minimum_index:
                minimum_index = lst[j]
    return lst
print(selection_sort(ints))    
print()

"""Insertion Sort avg wst O(n^2), space O(1)"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i-1, 0, -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
print(insertion_sort(ints))
print()

"""Quick Sort avg wst O(nlogn) O(n^2), space O(logn)"""
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    left, mid_pivot, right = [],[],[]
    pivot = lst[random.randint(0,len(lst)-1)]

    for i in lst:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            mid_pivot.append(i)
        else:
            right.append(i) 
    return quicksort(left) + mid_pivot + quicksort(right)  
print(quicksort(ints))


"""Merge Sort avg wst O(nlogn) O(nlogn), space O(n)"""

def merge(l1,l2): # Helper function
    l3 = []
    l1_index, l2_index = 0,0
    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            l3.append(l1[l1_index])
            l1_index += 1
        else:
            l3.append(l2[l2_index])
            l2_index += 1   
    if l1_index == len(l1): 
        l3.extend(l2[l2_index:]) 
    else:
        l3.extend(l1[l1_index:])            
    return l3


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left, right = merge_sort(lst[:len(lst)/2]),merge_sort(lst[len(lst)/2:])  
    return merge(left, right)  