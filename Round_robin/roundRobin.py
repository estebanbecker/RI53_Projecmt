from resource_grid import grid
from comm_generation import com

def round_robin(communications, nb_prb):
    """Proceeds the round robin algorithm
        communications: communications previously created with poisson law
        nb_prb: number of usable PRBs
        """

    #Tri des communications par temps d'arrivée
    communications = sorted(communications, key=lambda x: x['Spawning_Time_s'])

    allocation_grid = grid.Ressource_grid(nb_prb)

    current_slot = 0
    current_prb = 0

    while communications:
        current_comm = communications.pop(0)
        bits_per_symbol = current_comm['Quality_bits_per_symbol']

        # Changement de PRB si on arrive au bout du slot
        if current_prb >= nb_prb:
            current_prb = 0
            current_slot += 1
            allocation_grid.add_slot()

        size_before_allocation = current_comm['Size_bits']
        size_after_allocation = size_before_allocation - allocation_grid.assign_user(current_comm['Com_Num'], current_prb, current_slot, bits_per_symbol)
        current_comm['Size_bits'] = max(size_after_allocation, 0) 
        current_prb += 1

        # Remise dans la queue d'une communication pas totalement allouée
        if current_comm['Size_bits'] > 0:
            communications.append(current_comm)

    return allocation_grid