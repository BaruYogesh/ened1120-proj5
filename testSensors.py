#!/usr/bin/env python3

from subtask_3 import testColorSensor, testUltraSonicSensor, testRotationSensor, claw, toggleClaw, td

running = True

while(running):
    test = input("Input test: ")

    if(test=="color"):
        testColorSensor()
    elif(test=="ultra"):
        testUltraSonicSensor()
    elif(test=="claw"):
        toggleClaw()
        toggleClaw()
    elif(test=="rotation"):
        testRotationSensor()
    elif(test=="box"):
        vals = [0,0,0,0]
        for x in range(4):
            vals[x] = int(input("input: "))
        #square 1 is black
        if(vals[0]==1):
            #square 2 is white
            if(vals[1]==0):
                #square 3 is white
                if(vals[2]==6):
                    print(str(2))
                else:
                #square 3 is black
                    print(str(4))
            #square 2 is black
            elif(vals[1]==1):
                print(str(3))
            else:
                print(str(1))
        else: 
            print(str(-1))
    elif(test=="done"):
        running = False
    