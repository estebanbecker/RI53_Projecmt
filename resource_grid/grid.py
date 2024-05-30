#An allocation grid for LTE communication resources in downlink

try:
    from .slot import Slot  # Try to import with relative import
except ImportError:
    from slot import Slot

import numpy as np

class Ressource_grid:

    slot_grid=[]
    def __init__(self, nb_prb):
        """Creates a resource grid
        nb_prb: number of usable PRBs
        """
        self.nb_prb = nb_prb
        self.slot_grid = [[Slot(0,i) for i in range(0, nb_prb)]]

    def add_slot(self):
        """
        Adds a slot to the resource grid
        """
        position=len(self.slot_grid)
        self.slot_grid.append([Slot(position,i) for i in range(0, self.nb_prb)])

    def add_multiple_slots(self, nb_slots):
        """
        Adds multiple slots to the resource grid
        nb_slots: number of slots to add
        """
        for i in range(0, nb_slots):
            self.add_slot()
    
    def print_all(self):
        """
        Prints all slots in the resource grid
        """
        for i in range(0, len(self.slot_grid)):
            for j in range(0, self.nb_prb):
                print("Slot ", i, " PRB ", j)
                self.slot_grid[i][j].print()

    def assign_user(self, user, prb, slot, nb_bits_per_symbol=4):
        """
        Allocates a slot to a user
        user: the user to allocate the slot to
        prb: the PRB to allocate
        slot: the slot to allocate
        """
        self.slot_grid[slot][prb].allocate(user, nb_bits_per_symbol)

    def print_allocation(self):
        """
        Prints the users allocated to each slot
        """
        for i in range(0, len(self.slot_grid)):
            for j in range(0, self.nb_prb):
                print("Slot ", i, " PRB ", j)
                print("User ", self.slot_grid[i][j].user)

    def get_slot(self, slot,prb):
        """
        Returns a slot from the resource grid
        slot: the slot to return
        prb: the PRB to return
        """
        return self.slot_grid[slot][prb]
    
    def get_size_slot(self, slot, prb):
        """
        Returns the size of a slot
        slot: the slot to return
        prb: the PRB to return
        """
        return self.slot_grid[slot][prb].size()
    
    def get_user_slot(self, slot, prb):
        """
        Returns the user assigned to a slot
        slot: the slot to return
        prb: the PRB to return
        """
        return self.slot_grid[slot][prb].user
    
    def get_allocation_grid(self):
        """
        Returns the allocation grid simplified by slot
        """
        grid = []
        for i in range(0, len(self.slot_grid)):
            grid.append([self.slot_grid[i][j].user for j in range(0, self.nb_prb)])
        return grid
    
    def print_allocation_grid(self):
        """
        Prints the allocation grid simplified by slot
        """
        grid = self.get_allocation_grid()
        self.print_grid(grid)

    def print_grid(self, grid):
        """
        Prints a resource grid.
        
        Args:
            grid (list): The resource grid to be printed.
        """

        for i in range(0, len(grid[0])):
            for j in range(0, len(grid)):
                print(grid[j][i], end=' ')
            print()
    
    def get_full_allocation_grid(self):
        """
        Returns the complete resource grid
        """
        grid = []
        for i in range(0, len(self.slot_grid)*7):
            row= []
            for j in range(0, self.nb_prb*12):
                row.append(self.slot_grid[i//7][j//12].subcarriers[i%7][j%12])
            grid.append(row)
        return grid
    
    def get_full_allocation_grid_np(self):
        """
        Return the complete resource grid as a numpy array
        """
        grid = np.array(self.get_full_allocation_grid(), dtype=int)

        return np.flipud(grid.T)
    
    def print_full_allocation_grid(self):
        """
        Prints the complete resource grid
        """
        grid = self.get_full_allocation_grid()
        self.print_grid(grid)
    
    def get_allocation_grid(self):
        """
        Returns the allocation grid simplified by slot
        """
        grid = []
        for i in range(0, len(self.slot_grid)):
            grid.append([self.slot_grid[i][j].user for j in range(0, self.nb_prb)])
        return grid
    
    def print_allocation_grid(self):
        """
        Prints the allocation grid simplified by slot
        """
        grid = self.get_allocation_grid()
        self.print_grid(grid)

    def print_grid(self, grid):
        """
        Prints a resource grid.
        
        Args:
            grid (list): The resource grid to be printed.
        """

        for i in range(0, len(grid[0])):
            for j in range(0, len(grid)):
                print(grid[j][i], end=' ')
            print()
    
    def get_full_allocation_grid(self):
        """
        Returns the complete resource grid
        """
        grid = []
        for i in range(0, len(self.slot_grid)*7):
            row= []
            for j in range(0, self.nb_prb*12):
                row.append(self.slot_grid[i//7][j//12].subcarriers[i%7][j%12])
            grid.append(row)
        return grid
    
    def get_full_allocation_grid_np(self):
        """
        Retourne la grille de ressources complète sous forme de tableau numpy
        """
        grid = np.array(self.get_full_allocation_grid(), dtype=int)

        return np.flipud(grid.T)
    
    def print_full_allocation_grid(self):
        """
        Prints the complete resource grid
        """
        grid = self.get_full_allocation_grid()
        self.print_grid(grid)
    
def random_allocation(grid, nb_assignations, nb_users):
    """
    Assign random users to slots
    grid : the resource grid to assign users to
    nb_assignations : the number of assignations to make
    nb_users : the number of users to assign
    """
    import random
    for i in range(0, nb_assignations):
        user = random.randint(1, nb_users)
        prb = random.randint(0, grid.nb_prb-1)
        slot = random.randint(0, len(grid.slot_grid)-1)
        grid.assign_user(user, prb, slot, random.randint(1, 6))
    return grid
    

    
def generate():
    """
    Generate a resource grid for testing purposes
    """
    grid = Ressource_grid(5)
    grid.add_multiple_slots(19)
    grid= random_allocation(grid,300, 7)
    
    return grid.get_full_allocation_grid_np()

    

if __name__ == "__main__":
    # Create a resource grid object
    grid = Ressource_grid(5)

    # Add slots to the grid
    grid.add_multiple_slots(3)

    # Assign a user to a slot
    grid.assign_user(5, 1, 1, 5)

    # Assign more users to slots
    grid.assign_user(10, 0, 2, 4)
    grid.assign_user(15, 2, 0, 2)
    grid.assign_user(20, 1, 3, 1)
    grid.assign_user(25, 3, 1, 3)

    # Print all slots in the grid
    grid.print_all()

    # Print the allocation of users to slots
    grid.print_allocation()

    # Get a specific slot from the grid
    slot = grid.get_slot(0, 2)
    print("Slot 0 PRB 2:", slot)

    slot = grid.get_slot(1, 1)
    print("Slot 1 PRB 1:", slot)

    # Get the size of a slot
    size = grid.get_size_slot(0, 2)
    print("Size of Slot 0 PRB 2:", size)

    size = grid.get_size_slot(1, 1)
    print("Size of Slot 1 PRB 1:", size)

    # Get the user assigned to a slot
    user = grid.get_user_slot(0, 2)
    print("User assigned to Slot 0 PRB 2:", user)
    
    user = grid.get_user_slot(1, 1)
    print("User assigned to Slot 1 PRB 1:", user)

    # Get the simplified allocation grid
    allocation_grid = grid.get_allocation_grid()
    print("Simplified Allocation Grid:")
    grid.print_allocation_grid()

    # Get the full allocation grid
    full_allocation_grid = grid.get_full_allocation_grid()
    print("Full Allocation Grid:")
    grid.print_full_allocation_grid()