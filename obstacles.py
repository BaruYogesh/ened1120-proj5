#!/usr/bin/env python3

from subtask_3 import turn90, move, td, us, global_power,time

dist = int(input("Input distance: "))


while True:
    
    td.on(global_power, global_power)
    if(us.distance_centimeters_continuous < 30):

        td.off()
        #static object
        time.sleep(3)
        while(us.distance_centimeters_ping<30):
            turn90(True)
            move(20, True)
            turn90(False)
            time.sleep(2)
    

        

        
            




