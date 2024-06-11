from resource_grid import grid
from comm_generation import com

def round_robin(communications, nb_prb):
    time = 0
    queue = []
    completed_communications = []
    communications = sorted(communications, key=lambda x: x['Spawning_Time_s'])
    allocation_grid = grid.Ressource_grid(nb_prb)
    current_slot = 0
    current_prb = 0

    while communications or queue:
        # Ajouter les paquets arrivés à la file d'attente
        while communications and communications[0]['Spawning_Time_s'] <= time:
            queue.append(communications.pop(0))
        
        if queue:
            current_comm = queue.pop(0)
            execution_time = min(current_comm['Size_Kbits'], 3)
            current_comm['Size_Kbits'] -= execution_time
            time += execution_time

            # Convertir Kbits en bits et assigner l'utilisateur dans la grille
            size_in_bits = execution_time * 1000
            bits_per_symbol = current_comm['Quality_bits_per_symbol']
            bits_allocated = 0

            while bits_allocated < size_in_bits:
                if current_prb >= nb_prb:
                    current_prb = 0
                    current_slot += 1
                    allocation_grid.add_slot()

                remaining_bits = size_in_bits - bits_allocated
                bits_in_current_prb = min(remaining_bits, bits_per_symbol * 12)
                allocation_grid.assign_user(current_comm['Com_Num'], current_prb, current_slot, bits_per_symbol)
                bits_allocated += bits_in_current_prb
                current_prb += 1

            if current_comm['Size_Kbits'] > 0:
                queue.append(current_comm)
            else:
                completed_communications.append(current_comm)
        else:
            time += 1  # Si la file d'attente est vide, avancez le temps

    return allocation_grid