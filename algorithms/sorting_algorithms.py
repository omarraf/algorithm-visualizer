"""
CPSC 355 Group project 1
This project will serve to implement 4 sorting and 1 linear search algorithm(s)
and visually depict their runtime behavior specifically the speed
of which each algorithm takes with the same amount of data
"""

import random

#Bubble sort algorithm function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0, n-i-1):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr

#Merge sort algorithm function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#Quick sort algorithm function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater_nums = []
    lower_nums = []

    for i in arr:
        if i > pivot:
            greater_nums.append(i)

        else:
            lower_nums.append(i)
    pivot = [pivot]
    return quick_sort(lower_nums) + pivot + quick_sort(greater_nums)
    

#Radix sort algorithm function
#def radix_sort(arr)

#Linear search algorithm function
def linear_search(arr, target):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    return indexes

def generate_list(lower_bound, upper_bound, size):
    return [random.randint(lower_bound, upper_bound) for i in range(size)]
    
arr = generate_list(int(input("lower bound: ")), int(input("upper bound: ")), int(input("size: ")))
print(arr)
print(quick_sort(arr))
print(quick_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(merge_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(bubble_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(linear_search([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31],5))






"""
CPSC 355 Group project 1
This project will serve to implement 4 sorting and 1 linear search algorithm(s)
and visually depict their runtime behavior specifically the speed
of which each algorithm takes with the same amount of data
"""

import random

#Bubble sort algorithm function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0, n-i-1):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr

#Merge sort algorithm function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#Quick sort algorithm function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater_nums = []
    lower_nums = []

    for i in arr:
        if i > pivot:
            greater_nums.append(i)

        else:
            lower_nums.append(i)
    pivot = [pivot]
    return quick_sort(lower_nums) + pivot + quick_sort(greater_nums)
    

#Radix sort algorithm function
#def radix_sort(arr)

#Linear search algorithm function
def linear_search(arr, target):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    return indexes

def generate_list(lower_bound, upper_bound, size):
    return [random.randint(lower_bound, upper_bound) for i in range(size)]
    
arr = generate_list(int(input("lower bound: ")), int(input("upper bound: ")), int(input("size: ")))
print(arr)
print(quick_sort(arr))
print(quick_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(merge_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(bubble_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(linear_search([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31],5))
