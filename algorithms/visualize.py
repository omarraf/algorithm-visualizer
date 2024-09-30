import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, radix_sort

# Function to time sorting algos
def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    return elapsed_time

fig, ax = plt.subplots()

def animate(i, data_size):
    algorithms = [bubble_sort, merge_sort, quick_sort, radix_sort]
    data = [random.randint(0, 10000) for _ in range(data_size)]  
    labels = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort']
    times = [time_sorting_algorithm(algorithm, data.copy()) for algorithm in algorithms]

    ax.clear()
    ax.bar(labels, times, color=['red', 'green', 'orange', 'blue'])

    if data_size > 100:
        ax.set_yscale('log')
        ax.set_ylabel('Time (log scale, ms)')
    else:
        ax.set_ylabel('Time (ms)')

    ax.set_xlabel('Algorithms')
    ax.set_title(f'Sorting Algorithms Performance for Data Size {data_size}')

def run_animation(data_size):
    ani = animation.FuncAnimation(fig, animate, frames=4, fargs=(data_size,), interval=1000, blit=False, repeat=False)
    plt.show()


# For some reason when you change data_size to input() the graph doesnt show up, 
# at least on my end 
#data_size = int(input("prompt: "))    works for me- Eduardo
data_size = 1000
run_animation(data_size)
