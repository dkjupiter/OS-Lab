import random
from Model.model_database import write_csv, update_csv

import random
from Model.model_database import write_csv, update_csv

def totalkmilk(Cowid, Cowold_y, Cowold_m, Cowudder):
    Cowold_y = int(Cowold_y)
    Cowold_m = int(Cowold_m)
    Cowudder = int(Cowudder)

    # คำนวณปริมาณนม
    if Cowudder == 4:
        if random.random() < 0.05:
            update_csv(Cowid, 3)
        return Cowold_y + Cowold_m
    else:
        if random.random() < 0.20:
            update_csv(Cowid, 4)
        return 0
