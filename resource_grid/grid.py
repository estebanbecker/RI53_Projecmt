#An allocation grid for LTE communication resources in downlink

from slot import slot

class ressource_grid:

    slot_grid=[]
    def __init__(self, nb_prb):
        """Créé une grille de ressources
        nb_prb : nombre de PRB utilisable
        """
        self.nb_prb = nb_prb
        self.slot_grid = [[slot(0,i) for i in range(0, nb_prb)]]

    def add_slot(self):
        """
        Ajoute un slot à la grille de ressources
        """
        position=len(self.slot_grid)
        self.slot_grid.append([slot(position,i) for i in range(0, self.nb_prb)])
    
    def print_all(self):
        """
        Affiche tous les slot de la grille de ressources
        """
        for i in range(0, len(self.slot_grid)):
            for j in range(0, self.nb_prb):
                print("Slot ", i, " PRB ", j)
                self.slot_grid[i][j].print()

    def assign_user(self, user, prb, slot):
        """
        Alloue un slot à un utilisateur
        user : l'utilisateur à qui allouer le slot
        prb : le PRB à allouer
        slot : le slot à allouer
        """
        self.slot_grid[slot][prb].allocate(user)

    def print_allocation(self):
        """
        Affiche les utilisateurs alloués à chaque slot
        """
        for i in range(0, len(self.slot_grid)):
            for j in range(0, self.nb_prb):
                print("Slot ", i, " PRB ", j)
                print("User ", self.slot_grid[i][j].user)

    def get_slot(self, slot,prb):
        """
        Retourne un slot de la grille de ressources
        slot : le slot à retourner
        prb : le PRB à retourner
        """
        return self.slot_grid[slot][prb]
    
    def get_allocation_grid(self):
        """
        Retourne la grille de ressources simplifié par slot
        """
        grid = []
        for i in range(0, len(self.slot_grid)):
            grid.append([self.slot_grid[i][j].user for j in range(0, self.nb_prb)])
        return grid
    
    def print_allocation_grid(self):
        """
        Affiche la grille de ressources simplifié par slot
        """
        grid = self.get_allocation_grid()
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid)):
                print(grid[j][i], end=' ')
            print()
        


    
                

if __name__ == "__main__":
    rg=ressource_grid(5)

    rg.add_slot()

    rg.assign_user(1, 0, 0)
    rg.assign_user(2, 1, 0)
    rg.assign_user(3, 2, 0)
    rg.assign_user(4, 0, 1)
    rg.assign_user(5, 1, 1)
    
    rg.print_allocation()

    rg.print_all()

    grid = rg.get_allocation_grid()
    rg.print_allocation_grid()

    print(rg.get_slot(0,0).size(3))
    print(grid)