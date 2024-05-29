import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def plot_resource_grid(states: np.ndarray):
    """Draws a table of the resource_values
    
    expects a numpy NDarray with values
    {
        -1: 'gray',  # Reserved
        0: 'white',  # Free
        0 < : other colors used for each user
        }"""
    
    # Infer dimensions from the input states
    num_prbs, total_symbols = states.shape
    num_symbols_per_slot = 7
    num_slots_per_subframe = 2
    num_subframes = total_symbols // (num_symbols_per_slot * num_slots_per_subframe)
    total_slots = num_subframes * num_slots_per_subframe

    # Define colors for each state
    state_colors = {
        -1: 'gray',  # Reserved
        0: 'white',  # Free
    }

    # Generate user-specific colors
    unique_users = np.unique(states[states > 0])
    user_colors = {user: plt.cm.jet(i / len(unique_users)) for i, user in enumerate(unique_users)}
    state_colors.update(user_colors)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(15, 6))

    # Draw the grid
    for i in range(num_prbs):
        for j in range(total_symbols):
            cell_state = states[i, j]
            color = state_colors[cell_state] if cell_state in state_colors else 'black'
            rect = plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black')
            ax.add_patch(rect)

    # Set the ticks and labels
    ax.set_xticks([])
    ax.set_xticklabels([])

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
    ax.set_xlim(0, total_symbols // 2)  # Initial zoom level
    ax.set_ylim(0, num_prbs)
    ax.set_aspect('equal')
    ax.grid(True, which='both', axis='both', linestyle='--', color='gray')

    # Add a legend
    handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in state_colors.values()]
    labels = ['Reserved', 'Free'] + [f'User {user}' for user in unique_users]
    ax.legend(handles, labels, loc='upper right')

    # Title and labels
    plt.title('OFDMA Downlink Resource Grid', y=1.1)
    plt.xlabel('Symbols')
    plt.ylabel('PRBs')

    # Slider
    ax_slider = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'X-Axis', 0, total_symbols, valinit=0, valstep=1)

    # Update plot function
    def update(val):
        start = int(slider.val)
        end = start + total_symbols // 2  # Adjust this value to control the zoom level
        ax.set_xlim(start, end)
        fig.canvas.draw_idle()

    slider.on_changed(update)

    # Show the plot
    plt.gca().invert_yaxis()
    plt.show()
