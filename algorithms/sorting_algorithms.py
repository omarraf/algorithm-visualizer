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
    #Outer loop ensures every element is proccessed 
    for i in range(n):
        #inner loop ensures first element is moved to the end of the list
        #if element is less than adjacent element
        for k in range(0, n-i-1):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr

#Merge sort algorithm function
def merge_sort(arr):
    #recursive condition that turns arrays into 2 subarrys if the length
    #is greater than 1
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
    #recursivly calls merge_sort on sub arrays
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
    #loop to compare elements in subarrays and place them in order in an array 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
    #loop to add any remaining elements of left_half subarry into arr
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
    #loop to add any remaining elements of right_half subarry into arr
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#Quick sort algorithm function
def quick_sort(arr):
    #recursive condition 
    if len(arr) <= 1:
        return arr
    #pivot will always be the last item in array
    else:
        pivot = arr.pop()

    greater_nums = []
    lower_nums = []
    #check to see if elements in array are greater or less than pivot
    #adds them to approporate subarrays to sort
    for i in arr:
        if i > pivot:
            greater_nums.append(i)

        else:
            lower_nums.append(i)
    #pivot element turned to list
    pivot = [pivot]
    #recursivly call quick_sort on sub arrays/lists
    return quick_sort(lower_nums) + pivot + quick_sort(greater_nums)
    
#Radix sort algorithm function
#create a counting sort function to help sort for a specific digit
def counting_sort(arr, place):
    n = len(arr)
    #output that will store the sorted array
    output = [0] * n
    count = [0] * 10
    
    #stores the count of occurences 
    for i in range(n):
        index = arr[i] // place
        count[index % 10] += 1
        
    #determines the positions in the output array
    for i in range(1, 10):
        count[i] += count[i-1] 

    #builds the output array
    i = n-1
    while i>=0:
        index = arr[i] // place
        output[count[index % 10 ] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    #copies the output array to the actual array
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    #finds the maximum number to know the number of digits
    max_val = max(arr)

    #use the counting sort to help sort elements based on place value
    place = 1
    while max_val // place > 0: 
        counting_sort(arr, place)
        place *= 10
    return arr

#Linear search algorithm function
def linear_search(arr, target):
    indexes = []
    
    #loop to look through all elements in arry for target
    #if found index added to indexes list
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    return indexes

def generate_list(lower_bound, upper_bound, size):
    return [random.randint(lower_bound, upper_bound) for i in range(size)]
    
arr = generate_list(int(input("lower bound: ")), int(input("upper bound: ")), int(input("size: ")))
print(arr)
print(radix_sort(arr))
print(quick_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(merge_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(bubble_sort([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31]))
print(linear_search([123, 34, 5, 74, 235, 43, 63, 5, 9, 27, 83, 31],5))

