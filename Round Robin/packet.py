class Packet:
    def __init__(self, packet_id, size, arrival_time):
        self.packet_id = packet_id
        self.size = size
        self.arrival_time = arrival_time
        self.remaining_time = size

    def __repr__(self):
        return f"Packet(ID={self.packet_id}, size={self.size}, arrival={self.arrival_time}, remaining={self.remaining_time})"
