from utils import generate_packets

def round_robin(packets, quantum):
    time = 0
    queue = []
    completed_packets = []
    packets = sorted(packets, key=lambda x: x.arrival_time)
    current_packet_index = 0

    while packets or queue:
        # Ajouter les paquets arrivés à la file d'attente
        while packets and packets[0].arrival_time <= time:
            queue.append(packets.pop(0))
        
        if queue:
            current_packet = queue.pop(0)
            execution_time = min(current_packet.remaining_time, quantum)
            current_packet.remaining_time -= execution_time
            time += execution_time

            if current_packet.remaining_time > 0:
                queue.append(current_packet)
            else:
                completed_packets.append(current_packet)
        else:
            time += 1  # Si la file d'attente est vide, avancez le temps

    return completed_packets

if __name__ == "__main__":
    quantum = 3
    packets = generate_packets(10)
    round_robin(packets, quantum)
