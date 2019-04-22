#!/usr/bin/env python3
#line 1 is very important! make sure you have that on the top of all of your robot files

#import statements
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank, Motor
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
#gs = GyroSensor()



'''
globals cuz i'm a noob
global_power is what both my drive motors run off of. making a global makes it easier to change power across the whole program.
openClaw is used to toggle the claw open and shut
'''
global_power = 35
openClaw = False

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
        claw.on_for_degrees(SpeedPercent(80),-300)
        openClaw=False
    else:
        claw.on_for_degrees(SpeedPercent(80),300)
        openClaw=True

    time.sleep(1)



#WIP barcode scanning. will be used to get the type of box from reading the barcode.
def barcode():
    
    vals = [0,0,0,0]

    #close claw and move sensor to left.
    toggleClaw()
    claw.on_for_degrees(SpeedPercent(30),-65)
    for x in range(4):
        
        time.sleep(3)
        

        if(cs.ambient_light_intensity <= 3):
            vals[x] = 0
            debug_print("black: " + str(cs.ambient_light_intensity))
        else:
            vals[x] = 1
            debug_print("white: " + str(cs.ambient_light_intensity))
        #vals[x] = cs.ambient_light_intensity
        #debug_print(str(vals[x]) + ", ")
        claw.on_for_degrees(SpeedPercent(30),-75)
        
    '''
    #square 1 is black
    if(vals[0]==0):
        #square 2 is white
        if(vals[1]==1):
            #square 3 is white
            if(vals[2]==1):
                return 2
            else:
            #square 3 is black
                return 4
        #square 2 is black
        elif(vals[1]==0):
            return 3
        else:
            return 1
    else: 
        return -1
    '''
    claw.off()
    
    #old code reads from left to right, new will read bottom to top

    #0 IS BLACK, 1 IS WHITE
    if(vals[0]==0):
        return 4
    else:
        if(vals[1]==0):
            return 2
        else:
            if(vals[2]==0):
                return 3
            else:
                return 1
    
    return -1

def iGPS(a,b,d):
    Sound.beep(0)
    
        
#gets color from color sensor
def getColor():
    return cs.ambient_light_intensity

def testColorSensor():
    for x in range(20):
        debug_print(getColor())
        time.sleep(1)

#just runs the US sensor 10 times and gets values.
def testUltraSonicSensor():
    for x in range(10):
        debug_print(us.distance_centimeters)
        time.sleep(1)
def testRotationSensor():
    a = Motor(OUTPUT_A)
    d = Motor(OUTPUT_D)
    b = Motor(OUTPUT_B)

    for x in range(10):
        debug_print("A:" + str(a.position))
        debug_print("D:" + str(d.position))
        debug_print("B:" + str(b.position))
        #td.on_for_rotations(global_power,global_power,1)

        time.sleep(1)  
    
'''
a = float(input("Input A: "))
b = float(input("Input B: "))
d = float(input("Input D: "))

iGPS(a,b,d)

toggleClaw()   
toggleClaw()
'''
