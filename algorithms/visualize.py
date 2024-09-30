import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, radix_sort, linear_search


def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time
