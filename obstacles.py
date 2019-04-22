#!/usr/bin/env python3

from subtask_3 import turn90, move, td, us, global_power,time

dist = int(input("Input distance: "))

#global
obst = False

while True:
    
    #runs infinitely (does not stop at a given distance)
    td.on(global_power, global_power)
    #object detected directly ahead
    if(us.distance_centimeters_continuous < 15):

        #stop and wait
        td.off()
        time.sleep(3)

        #static object, object is detected in front of robot after 3 seconds
        while(us.distance_centimeters_ping<15):
            #turns and goes around the obstacle
            obst = True
            turn90(True)
            move(25, True)
            turn90(False)
            time.sleep(2)

        
        if(obst):
            while(obst):
                #faces the obstacles and checks to see if it can move forward. otherwise, turns back to straight and keeps moving
                move(20, True)
                turn90(False)
                if(us.distance_centimeters_ping<10):
                    obst = False
                else:
                    turn90(True)
                
            #gets back inline
            move(25,True)
            turn90(True)
            obst= False
