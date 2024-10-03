import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, radix_sort, linear_search
from matplotlib.widgets import TextBox, Button, CheckButtons

# Function to time sorting algorithms
def time_sorting_algorithm(algorithm, arr, target=None):
    start_time = time.perf_counter()
    if algorithm == linear_search:
        algorithm(arr, target)
    else:
        algorithm(arr)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    return elapsed_time

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3, bottom=0.25, top=0.95, right=0.95)  # Adjust to make space for buttons

# Global flag and variable to control animation
is_paused = False
data_size = None  
target_value = None 
custom_list = None
ani = None  

# Algorithm selection flags
algorithm_flags = {
    'Bubble sort': False,
    'Merge sort': False,
    'Quick sort': False,
    'Radix sort': False,
    'Linear search': False
}

# Function to animate the algorithms
def animate(i):
    global ani
    if is_paused:
        return  # Skip frame update if paused
    algorithms = []
    labels = []
    colors = []
    if algorithm_flags['Bubble sort']:
        algorithms.append(bubble_sort)
        labels.append('Bubble sort')
        colors.append('red')
    if algorithm_flags['Merge sort']:
        algorithms.append(merge_sort)
        labels.append('Merge sort')
        colors.append('green')
    if algorithm_flags['Quick sort']:
        algorithms.append(quick_sort)
        labels.append('Quick sort')
        colors.append('orange')
    if algorithm_flags['Radix sort']:
        algorithms.append(radix_sort)
        labels.append('Radix sort')
        colors.append('blue')
    if algorithm_flags['Linear search']:
        algorithms.append(linear_search)
        labels.append('Linear search')
        colors.append('purple')

    if not algorithms:
        return  # No algorithms selected, nothing to animate

    if custom_list is not None:
        data = custom_list
    else:
        data = [random.randint(0, 10000) for _ in range(data_size)]
    
    times = [time_sorting_algorithm(algorithm, data.copy(), target_value) for algorithm in algorithms]

    ax.clear()
    bar_width = 0.4  # Fixed width for bars
    bars = ax.bar(labels, times, color=colors, width=bar_width)
    for i in range(len(bars)):
        bar = bars[i]
        time = times[i]
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{time:.3f}', ha='center')

    if data_size > 100:
        ax.set_yscale('log')
        ax.set_ylabel('Time (log scale, ms)')
    else:
        ax.set_ylabel('Time (ms)')

    ax.set_xlabel('Algorithms')
    ax.set_title(f'Sorting Algorithms Performance for Data Size {data_size}')

    # Adjust x-axis limits to provide padding
    ax.set_xlim(-0.5, len(labels) - 0.5)

# Function to start or restart the animation
def run_animation():
    global ani, is_paused
    is_paused = False  # Reset pause status when starting a new animation
    if ani is not None and ani.event_source is not None:
        ani.event_source.stop()  # Stop any previous animation only if it's running

    # Start a new animation, using 100 frames (non-repeating)
    ani = animation.FuncAnimation(fig, animate, frames=60, interval=1000, blit=False, repeat=False)
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
    global ani, is_paused, custom_list
    is_paused = False
    custom_list = None  # Reset custom list
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
        start_button.on_clicked(lambda event: run_animation())  # Activate callback
        plt.draw()  # Update button appearance
    except ValueError:
        data_size = None  # Reset if input is invalid

# For TextBox submit callback for target value
def submit_target(text):
    global target_value
    try:
        target_value = int(text)
    except ValueError:
        target_value = None  # Reset if input is invalid

# For TextBox submit callback for custom list
def submit_custom_list(text):
    global custom_list, data_size, start_button
    try:
        custom_list = [int(x) for x in text.split(',')]
        data_size = len(custom_list)
        start_button.color = '0.85'  # Enable the button (visually)
        start_button.on_clicked(lambda event: run_animation())  # Activate callback
        plt.draw()  # Update button appearance
    except ValueError:
        custom_list = None  # Reset if input is invalid

# For CheckButtons callback
def update_algorithm_flags(label):
    algorithm_flags[label] = not algorithm_flags[label]
    if label == 'Linear search' and algorithm_flags[label]:
        target_box.set_active(True)
    else:
        target_box.set_active(False)

# Create TextBox to get user input for data size
axbox = plt.axes([0.1, 0.01, 0.2, 0.05])  # Position of the textbox
text_box = TextBox(axbox, "Enter Data Size: ")
text_box.label.set_color('blue')
text_box.on_submit(submit)

# Create TextBox to get user input for target value (initially hidden)
axtarget = plt.axes([0.1, 0.07, 0.2, 0.05])  # Position of the target textbox
target_box = TextBox(axtarget, "Enter Target Value: ")
target_box.label.set_color('blue')
target_box.on_submit(submit_target)
target_box.set_active(False)  # Initially hidden

# Create TextBox to get user input for custom list
axcustom = plt.axes([0.1, 0.13, 0.2, 0.05])  # Position of the custom list textbox
custom_box = TextBox(axcustom, "Enter Custom List: ")
custom_box.label.set_color('blue')
custom_box.on_submit(submit_custom_list)

# CheckButtons for selecting which algorithms to run
rax = plt.axes([0.01, 0.4, 0.25, 0.5], frameon = False)  # Increase the width and height of the check buttons
check = CheckButtons(rax, algorithm_flags.keys(), algorithm_flags.values())
check.on_clicked(update_algorithm_flags)

# Start, Pause, and Reset Buttons
axstart = plt.axes([0.7, 0.1, 0.1, 0.075])  # Position of Start button
start_button = Button(axstart, 'Start', color='lightgreen', hovercolor='green')

# Initially, disable the "Start" button (grayed out)
start_button.color = '#FFFFFF'  # Grayed out color
start_button.on_clicked(lambda event: None)  # Initially no action

axpause = plt.axes([0.81, 0.1, 0.1, 0.075])  # Position of Pause button
pause_button = Button(axpause, 'Pause', color='lightblue', hovercolor='blue')
pause_button.on_clicked(toggle_pause)

axreset = plt.axes([0.59, 0.1, 0.1, 0.075])  # Position of Reset button
reset_button = Button(axreset, 'Reset', color='lightcoral', hovercolor='red')
reset_button.on_clicked(reset_animation)

plt.show()
