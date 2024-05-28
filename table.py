import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Define dimensions
num_subframes = 10
num_slots_per_subframe = 2
num_symbols_per_slot = 7
num_prbs = 6
total_slots = num_subframes * num_slots_per_subframe
total_symbols = total_slots * num_symbols_per_slot

# Example state grid (this would be based on actual data in a real scenario)
states = np.random.choice(['idle', 'occupied', 'scheduled', 'error'], 
                          size=(num_prbs, total_symbols))

# Define colors for each state
state_colors = {
    'idle': 'white',
    'occupied': 'green',
    'scheduled': 'blue',
    'error': 'red'
}

# Create the figure and axis
fig, ax = plt.subplots(figsize=(15, 6))

# Draw the grid
for i in range(num_prbs):
    for j in range(total_symbols):
        cell_state = states[i, j]
        rect = plt.Rectangle((j, i), 1, 1, facecolor=state_colors[cell_state], edgecolor='black')
        ax.add_patch(rect)

# Set the ticks and labels
ax.set_xticks([])
# ax.set_yticks(np.arange(num_prbs) + 0.5)
ax.set_xticklabels([])
ax.set_yticklabels([f'PRB {num_prbs - i - 1}' for i in range(num_prbs)])

# Add subframe and slot labels
for subframe in range(num_subframes):
    subframe_label = f'Subframe {subframe}'
    subframe_x_pos = subframe * num_symbols_per_slot * num_slots_per_subframe + num_symbols_per_slot * num_slots_per_subframe / 2
    ax.text(subframe_x_pos, num_prbs + 1, subframe_label, ha='center', va='bottom', fontsize=10, weight='bold')
    for slot in range(num_slots_per_subframe):
        slot_index = subframe * num_slots_per_subframe + slot
        slot_label = f'Slot {slot}'
        slot_x_pos = slot_index * num_symbols_per_slot + num_symbols_per_slot / 2
        ax.text(slot_x_pos, num_prbs + 0.5, slot_label, ha='center', va='bottom', fontsize=8)

# Shading alternate slots for clearer visual separation
for slot in range(total_slots):
    if slot % 2 == 1:  # Alternate shading for slots
        ax.add_patch(plt.Rectangle((slot * num_symbols_per_slot, 0), num_symbols_per_slot, num_prbs, facecolor='lightgray', alpha=0.5))

# Draw thicker lines to separate subframes and slots
for subframe in range(num_subframes + 1):
    ax.axvline(x=subframe * num_symbols_per_slot * num_slots_per_subframe, color='black', linewidth=2)

# Set the limits and grid
ax.set_xlim(0, total_symbols//2)  # Initial zoom level
ax.set_ylim(0, num_prbs)
ax.set_aspect('equal')
ax.grid(True, which='both', axis='both', linestyle='--', color='gray')

# Add a legend
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in state_colors.values()]
labels = state_colors.keys()
ax.legend(handles, labels, loc='upper right')

# Title and labels
plt.title('OFDMA Downlink Resource Grid')
plt.xlabel('Symbols')
plt.ylabel('PRBs')

# Slider
ax_slider = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'X-Axis', 0, total_symbols, valinit=0, valstep=1)

# Update plot function
def update(val):
    start = int(slider.val)
    end = start + total_symbols//2  # Adjust this value to control the zoom level
    ax.set_xlim(start, end)
    fig.canvas.draw_idle()

slider.on_changed(update)

# Show the plot
plt.gca().invert_yaxis()
plt.show()
