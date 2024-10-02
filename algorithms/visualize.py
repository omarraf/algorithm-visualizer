import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, radix_sort
from matplotlib.widgets import TextBox, Button

# Function to time sorting algorithms
def time_sorting_algorithm(algorithm, arr):
    start_time = time.perf_counter()
    algorithm(arr)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    return elapsed_time

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust to make space for buttons

# Global flag and variable to control animation
is_paused = False
data_size = None  # Initially None, waiting for user input
ani = None  # Global reference to the animation object

# Function to animate the algorithms
def animate(i):
    if is_paused:
        return  # Skip frame update if paused

    algorithms = [bubble_sort, merge_sort, quick_sort, radix_sort]
    data = [random.randint(0, 10000) for _ in range(data_size)]  
    labels = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort']
    times = [time_sorting_algorithm(algorithm, data.copy()) for algorithm in algorithms]

    ax.clear()
    bars = ax.bar(labels, times, color=['red', 'green', 'orange', 'blue'])

    for i in range(len(bars)):
        bar = bars[i]
        time = times[i]
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,f'{time:.3f}')


    if data_size > 100:
        ax.set_yscale('log')
        ax.set_ylabel('Time (log scale, ms)')
    else:
        ax.set_ylabel('Time (ms)')

    ax.set_xlabel('Algorithms')
    ax.set_title(f'Sorting Algorithms Performance for Data Size {data_size}')

# Function to start or restart the animation
def run_animation():
    global ani, is_paused
    is_paused = False  # Reset pause status when starting a new animation
    if ani is not None and ani.event_source is not None:
        ani.event_source.stop()  # Stop any previous animation only if it's running

    # Start a new animation, using 100 frames (non-repeating)
    ani = animation.FuncAnimation(fig, animate, frames=100, interval=1000, blit=False, repeat=False)
    plt.draw()  # Make sure the plot updates

# For pausing/resuming the animation
def toggle_pause(event):
    global is_paused
    is_paused = not is_paused  # Toggle pause
    if ani is not None:
        if is_paused:
            ani.event_source.stop()  # Stop updating frames when paused
        else:
            ani.event_source.start()  # Resume updating frames when unpaused

# Reset function
def reset_animation(event):
    global ani, is_paused
    is_paused = False
    if ani is not None and ani.event_source is not None:
        ani.event_source.stop()  # Stop the animation only if it's running
    ax.clear()
    ax.set_title("Sorting Algorithms Performance")  # Clear the plot
    plt.draw()

# For TextBox submit callback
def submit(text):
    global data_size, start_button
    try:
        data_size = int(text)
        start_button.color = '0.85'  # Enable the button (visually)
        #start_button.hovercolor = '0.95'
        start_button.on_clicked(lambda event: run_animation())  # Activate callback
        plt.draw()  # Update button appearance
    except ValueError:
        data_size = None  # Reset if input is invalid

# For delarcing what algortithms to run
def run_bubble(event):
    global bubble
    bubble = True

def run_merge(event):
    global merge
    merge = True

def run_quick(event):
    global quick
    quick = True

def run_radix(event):
    global radix
    radix = True

def run_linear(event):
    global linear
    linear = True

# Create TextBox to get user input for data size
axbox = plt.axes([0.2, 0.01, 0.4, 0.05])  # Position of the textbox
text_box = TextBox(axbox, "Enter Data Size: ")
text_box.on_submit(submit)

# Buttons for selecting which algorithms to run
axstart= plt.axes([0.015, 0.14, 0.14, 0.05])  # Position of bubble sort button
bubble_button = Button(axstart, 'Bubble Sort') 
bubble_button.on_clicked(run_bubble)

axmerge= plt.axes([0.163, 0.14, 0.14, 0.05]) # Position of merge sort button
merge_button = Button(axmerge, 'Merge Sort')
merge_button.on_clicked(run_merge)

axquick= plt.axes([0.31, 0.14, 0.14, 0.05])# Position of quick sort button
quick_button = Button(axquick, 'Quick Sort')
quick_button.on_clicked(run_quick)

axradix= plt.axes([0.163, 0.08, 0.14, 0.05])# Position of radix sort button
radix_button = Button(axradix, 'Radix Sort')
radix_button.on_clicked(run_radix)

axlinear= plt.axes([0.31, 0.08, 0.16, 0.05])# Position of linear search button
linear_button = Button(axlinear, 'Linear Search')
linear_button.on_clicked(run_linear)

# Start, Pause, and Reset Buttons
axstart = plt.axes([0.7, 0.1, 0.1, 0.075])  # Position of Start button
start_button = Button(axstart, 'Start')

# Initially, disable the "Start" button (grayed out)
start_button.color = '#FFFFFF'  # Grayed out color
#start_button.hovercolor = '0.75'
start_button.on_clicked(lambda event: None)  # Initially no action

axpause = plt.axes([0.81, 0.1, 0.1, 0.075])  # Position of Pause button
pause_button = Button(axpause, 'Pause')
pause_button.on_clicked(toggle_pause)

axreset = plt.axes([0.59, 0.1, 0.1, 0.075])  # Position of Reset button
reset_button = Button(axreset, 'Reset')
reset_button.on_clicked(reset_animation)

plt.show()
