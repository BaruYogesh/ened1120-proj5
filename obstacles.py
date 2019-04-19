#!/usr/bin/env python3

from subtask_3 import turn90, move, td, us, global_power,time

dist = int(input("Input distance: "))

obst = False

while True:
    
    td.on(global_power, global_power)
    if(us.distance_centimeters_continuous < 15):

        td.off()
        #static object
        time.sleep(3)
        while(us.distance_centimeters_ping<15):
            obst = True
            turn90(True)
            move(25, True)
            turn90(False)
            time.sleep(2)

        if(obst):
            while(obst):
                move(20, True)
                turn90(False)
                if(us.distance_centimeters_ping<10):
                    obst = False
                else:
                    turn90(True)
                
            
            move(25,True)
            turn90(True)
            obst= False
