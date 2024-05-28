import numpy as np
import time

def GenListeCom():
    """
    Generate a list of communications with random sizes and random time between communications (Poisson law)

    Returns:
        None
    
    """
    ComTimeStamp=0
    for com_num in range(1, 11):
        com_num += 1
        
        communication_sizes= np.random.poisson(10, 1)  # Average size of 10 Kbits

        sleeptimerandom= np.random.uniform(0,1)
        ComTimeStamp+=sleeptimerandom

        print("Com Num:", com_num, "| Size:", communication_sizes,"Kbits"," | Spawning Time:", round(ComTimeStamp,2),"s", "| Sleep Time:", round(sleeptimerandom,2),"s")
        print("--------------------------------------")
        # time.sleep(sleeptimerandom)

if __name__ == "__main__":
    GenListeCom()