import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("OFDMA downlink simulation")

# Define the column headings for the table
headings = ['Time Slot', 'Frequency Subcarrier', 'User ID', 'Packet Data']
data = [
    [1, 'Subcarrier 1', 'User A', 'Packet 1'],
    [1, 'Subcarrier 2', 'User B', 'Packet 2'],
    [2, 'Subcarrier 1', 'User C', 'Packet 3'],
    [2, 'Subcarrier 2', 'User A', 'Packet 4']
]

def add_column():
    new_column_heading = column_entry.get()
    table["columns"] += (new_column_heading,)
    table.heading(new_column_heading, text=new_column_heading)

# Define parameter inputs
param_frame = tk.Frame(root)
param_frame.pack(side=tk.LEFT, padx=10)

tk.Label(param_frame, text="frequence").grid(row=0, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=0, column=1, padx=5)
tk.Label(param_frame, text="communication").grid(row=1, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=1, column=1, padx=5)
tk.Label(param_frame, text="moyenne d'arrivée").grid(row=2, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=2, column=1, padx=5)
tk.Label(param_frame, text="Ecart-type").grid(row=3, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=3, column=1, padx=5)
tk.Label(param_frame, text="tailles des communication").grid(row=4, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=4, column=1, padx=5)
tk.Label(param_frame, text="taille moyenne").grid(row=5, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=5, column=1, padx=5)
tk.Label(param_frame, text="ecart-Type").grid(row=6, column=0, sticky="w")
tk.Entry(param_frame, width=4).grid(row=6, column=1, padx=5)

# Define table
table_frame = tk.Frame(root)
table_frame.pack(side=tk.RIGHT, padx=10, pady=10)

table = ttk.Treeview(table_frame, columns=headings, show="headings")
for col in headings:
    table.heading(col, text=col)
table.pack(side=tk.LEFT, fill=tk.BOTH)

# Insert data into the table
for row in data:
    table.insert("", "end", values=row)

column_frame = tk.Frame(root)
column_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

column_entry = tk.Entry(column_frame)
column_entry.pack(side=tk.LEFT, padx=5)

add_column_button = tk.Button(column_frame, text="Add Column", command=add_column)
add_column_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
