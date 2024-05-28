import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb

def plot_ofdma_table(data):
    # Define the colors for the different cell types
    cmap = { 
        -1: 'black',  # Reserved
        0: 'white',   # Free
        1: 'blue',    # User 1
        2: 'green',   # User 2
        3: 'red',     # User 3
        # Add more colors as needed for more users
    }
    
    # Determine the dimensions of the data
    num_rows = len(data)
    num_cols = len(data[0]) if num_rows > 0 else 0
    print(num_rows, num_cols)

    # Create a color array based on the data
    color_array = np.zeros((num_rows, num_cols, 3))
    
    for i in range(num_rows):
        for j in range(num_cols):
            color_array[i, j] = to_rgb(cmap[data[i][j]])

    plt.pcolormesh(color_array, edgecolors='k', linewidth=2)
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.invert_yaxis()
    
    plt.show()

# Example data
data = [
    [0, -1, 1, 2, 3],
    [0, 0, 0, -1, 1],
    [2, 2, 0, 1, 3],
    [-1, -1, 0, 0, 1],
    [3, 0, 0, 0, 2]
]

plot_ofdma_table(data)
