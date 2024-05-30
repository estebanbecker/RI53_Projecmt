import numpy as np
import time

def GenListeCom():
    """
    Generate a list of communications with random sizes and random time between communications (Poisson law)

    Returns:
        None
    
    """
    ComTimeStamp=0
    for com_num in range(0, 10): # Generate 10 communications
        com_num += 1
        communication_sizes= np.random.poisson(10, 1)  # Average size of 10 Kbits
        sleeptimerandom= np.random.uniform(0,1) # Random sleep time between 0 and 1 second 
        ComTimeStamp+=sleeptimerandom # Add the sleep time to the timestamp, next com will be spawned after the sleep time + the previous timestamp
        communication_quality = np.random.choice([1, 2, 4, 5, 6, 8], 1)[0] # Random quality between BPSK, QPSK, 16QAM, 32QAM, 64QAM, 256QAM

        print("Com Num:", com_num, "| Size:", communication_sizes,"Kbits"," | Com quality:",communication_quality, "bits/symbol | Spawning Time:", round(ComTimeStamp,2),"s", "| Sleep Time:", round(sleeptimerandom,2),"s")
        print("--------------------------------------")
        # time.sleep(sleeptimerandom)

if __name__ == "__main__":
    GenListeCom()