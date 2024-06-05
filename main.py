from comm_generation.com import GenListeCom

if __name__ == "__main__":
    print("Generating communications")
    ListeOfAllCom = GenListeCom()

    for com in ListeOfAllCom:
        print("Com Num:", com["Com_Num"], "| Size:", com["Size_Kbits"],"Kbits"," | Com quality:",com["Quality_bits_per_symbol"], "bits/symbol | Spawning Time:", com["Spawning_Time_s"],"s", "| Sleep Time:", com["Sleep_Time_s"],"s")
