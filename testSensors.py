#!/usr/bin/env python3

from subtask_3 import testColorSensor, testUltraSonicSensor

running = True

while(running):
    test = input("Input test: ")

    if(test=="color"):
        testColorSensor()
    elif(test=="ultra"):
        testUltraSonicSensor()
    elif(test=="done"):
        running = False
    