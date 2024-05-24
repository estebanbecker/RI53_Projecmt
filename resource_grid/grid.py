#An allocation grid for LTE communication resources in downlink

import slot

class ressource_grid:
    slot_grid = []
    def init(self, nb_prb):
        self.nb_prb = nb_prb
        self.slot_grid[0] = [slot(0) for i in range(0, nb_prb)]

    def add_slot(self):
        position=self.slot_grid.len()
        self.slot_grid.append(slot(position))
    



