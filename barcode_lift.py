#!/usr/bin/env python3

from subtask_3 import move, turn90, barcode, debug_print, toggleClaw, claw, td
from ev3dev2.motor import SpeedPercent

boxType = int(input("Input box type"))

move(20,True)
turn90(False)
move(20,True)

found = False
count = 0

while found == False:
    turn90(True)
    box = barcode()

    if(box == boxType):
        found == True
    else:
        count = count+1
        turn90(False)
        move(20,True)

claw.on_for_rotations(SpeedPercent(80),2.55)
td.on_for_rotations(20,20,0.0588235*6)
claw.on_for_rotations(SpeedPercent(80),-2.55)
td.on_for_rotations(20,20,0.0588235*-6)

turn90(True)
move(20*count, True)
turn90(False)
move(20,False)



