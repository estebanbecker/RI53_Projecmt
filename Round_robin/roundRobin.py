from resource_grid import grid
from comm_generation import com

def round_robin(communications, nb_prb):
    time = 0
    queue = []
    completed_communications = []
    communications = sorted(communications, key=lambda x: x['Spawning_Time_s'])
    allocation_grid=grid.Ressource_grid(nb_prb)

    while communications or queue:
        # Ajouter les paquets arrivés à la file d'attente
        while communications and communications[0]['Spawning_Time_s'] <= time:
            queue.append(communications.pop(0))
        
        if queue:
            current_comm = queue.pop(0)
            execution_time = min(current_comm['Size_Kbits'], 3)
            current_comm['Size_Kbits'] -= execution_time
            time += execution_time

            if current_comm['Size_Kbits'] > 0:
                queue.append(current_comm)
            else:
                completed_communications.append(current_comm)
        else:
            time += 1  # Si la file d'attente est vide, avancez le temps

    return allocation_grid
