from resource_grid import grid
from comm_generation import com

def round_robin(communications, nb_prb):
    """Proceeds the round robin algorithm
        communications: communications previously created with poisson law
        nb_prb: number of usable PRBs
        """

    # Tri des communications par temps d'arrivée
    communications = sorted(communications, key=lambda x: x['Spawning_Time_s'])

    allocation_grid = grid.Ressource_grid(nb_prb)

    current_slot = 0
    current_prb = 0
    current_time = 0

    # File d'attente temporaire pour les communications en cours
    temp_queue = []

    while communications or temp_queue:
        # Ajouter les nouvelles communications qui arrivent au slot courant
        while communications and communications[0]['Spawning_Time_s'] < current_time + 1:
            temp_queue.append(communications.pop(0))

        # Si la file temporaire est vide, on passe au slot suivant
        if not temp_queue:
            current_slot += 1
            current_time += 1
            current_prb = 0
            allocation_grid.add_slot()
            continue

        # Récupérer la communication de la file temporaire
        current_comm = temp_queue.pop(0)
        bits_per_symbol = current_comm['Quality_bits_per_symbol']

        # Changement de PRB si on arrive au bout du slot
        if current_prb >= nb_prb:
            current_prb = 0
            current_slot += 1
            current_time += 1
            allocation_grid.add_slot()

        # Allocation des communications à la grille
        size_before_allocation = current_comm['Size_bits']
        size_after_allocation = size_before_allocation - allocation_grid.assign_user(current_comm['Com_Num'], current_prb, current_slot, bits_per_symbol)
        current_comm['Size_bits'] = max(size_after_allocation, 0) 
        current_prb += 1

        # Remise dans la queue temporaire d'une communication pas totalement allouée
        if current_comm['Size_bits'] > 0:
            temp_queue.append(current_comm)

    return allocation_grid