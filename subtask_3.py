#!/usr/bin/env python3
#line 1 is very important! make sure you have that on the top of all of your robot files

#import statements
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.led import Leds
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time
import sys

'''
object construction
td is my tankdrive that uses motor outputs A and D
claw is a single motor that uses output B
cs is a color sensor, you don't need to choose an input
us is an ultrasonic sensor (the one with the eyes), dont need to choose input
'''
td = MoveTank(OUTPUT_A,OUTPUT_D)
claw = MediumMotor(OUTPUT_B)
cs = ColorSensor()
us = UltrasonicSensor()

'''
globals cuz i'm a noob
global_power is what both my drive motors run off of. making a global makes it easier to change power across the whole program.
openClaw is used to toggle the claw open and shut
'''
global_power = 35
openClaw = True

#debug function, copied from the example files. very helpful!
def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

"""
Move function
Used for moving back and forth as needed for task 2a
"""
def move(travel,dir):

    travel = travel * 0.0588235
    if(dir):
        td.on_for_rotations(global_power,global_power,travel)
        print("moving forward for " + str(travel))
    
    else:
        td.on_for_rotations(-1*global_power,-1*global_power,travel)
        print("moving backward for " + str(travel))
    time.sleep(1.0)

#turns 90 degrees left or right
#true is ccw, false cw
def turn90(dir):
    
    if(dir):
        td.on_for_rotations(global_power*.6,-1*global_power*.6,1.065/2.0)
        print("Turned counterclockwise")
    else:
        td.on_for_rotations(-1*global_power*.6,global_power*.6,1.065/2.0)
        print("Turned clockwise")
    time.sleep(1.0)

#toggles claw open and shut.
def toggleClaw():
    global openClaw
    if(openClaw):
        claw.on_for_rotations(SpeedPercent(50),-.85)
        openClaw=False
    else:
        claw.on_for_rotations(SpeedPercent(50),.85)
        openClaw=True

    time.sleep(1)

#WIP iGPS
def iGPS(a,b,d):
    Display.text_pixels(0,a + " " + b + " " + d,30,30)
    Sound.play_note(0,'D4',2)


#WIP barcode scanning. will be used to get the type of box from reading the barcode.
def barcode():
    
    vals = [0,0,0,0]

    #close claw and move sensor to left.
    toggleClaw()
    for x in range(4):
        claw.on_for_degrees(30,100)
        time.sleep(1)
        
        vals[x] = cs.color
        debug_print(str(vals[x]) + ", ")

    #square 1 is black
    if(vals[0]==1):
        #square 2 is white
        if(vals[1]==6):
            #square 3 is white
            if(vals[2]==6):
                return 2
            else:
            #square 3 is black
                return 4
        #square 2 is black
        elif(vals[1]==1):
            return 3
        else:
            return 1
    else: 
        return -1

        
#gets color from color sensor
def getColor():
    return cs.color

#just runs the US sensor 10 times and gets values.
def testUltraSonicSensor():
    for x in range(10):
        debug_print(us.distance_centimeters)
        time.sleep(1)

'''
debug_print(barcode())
time.sleep(5)


toggleClaw()
toggleClaw()

for x in range(6):
    s = input("input s")
    print(s)
'''