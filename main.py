from comm_generation.com import GenListeCom
from GUI import settings, table
from resource_grid import grid
from Round_robin import roundRobin


if __name__ == "__main__":
    setting_values = settings.settings()

    list_com = GenListeCom(settings_values=setting_values)

    allocation_grid = roundRobin.round_robin(list_com, int(setting_values[0]))

    for com in list_com:
        print("Com Num:", com["Com_Num"], "| Size:", com["Size_Kbits"],"Kbits"," | Com quality:",com["Quality_bits_per_symbol"], "bits/symbol | Spawning Time:", com["Spawning_Time_s"],"s", "| Sleep Time:", com["Sleep_Time_s"],"s")

    resource_grid = roundRobin.round_robin(list_com, len(setting_values))

    table.plot_resource_grid(resource_grid.get_full_allocation_grid_np())
    # print("Generating communications")
