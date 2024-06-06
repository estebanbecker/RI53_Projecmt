from comm_generation.com import GenListeCom
from GUI import settings, table
from resource_grid import grid


if __name__ == "__main__":
    setting_values = settings.settings()

    # generate values with settings values
    #
    # ...
    #

    # temporary values for test

    table.plot_resource_grid(grid.generate())
    print("Generating communications")
    ListeOfAllCom = GenListeCom()

    for com in ListeOfAllCom:
        print("Com Num:", com["Com_Num"], "| Size:", com["Size_Kbits"],"Kbits"," | Com quality:",com["Quality_bits_per_symbol"], "bits/symbol | Spawning Time:", com["Spawning_Time_s"],"s", "| Sleep Time:", com["Sleep_Time_s"],"s")
