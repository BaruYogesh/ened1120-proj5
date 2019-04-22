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
    elif(test=="done"):
        running = False
    