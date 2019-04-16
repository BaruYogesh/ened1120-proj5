from ev3dev2.sound import Sound
from time import sleep
import math
import os
import sys
import time

# state constants
ON = True
OFF = False
#functions from hello program
def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)
def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')
def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')
def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


'''
Calculates the coordinates of the intersecting points of two circles along the same axis
Uses a third point to select the closer of the two.
equation used:
http://paulbourke.net/geometry/circlesphere/
'''
def Point_Select(P0x, P0y, r0, P1x, P1y, r1 ,P4x, P4y, r4):
    d = abs(P0x-P1x)
    #make sure it isn't broke
    if d > r0 + r1:
        print("no sol")
    elif d < abs(r0-r1):
        print("no sol- contained circle")
    elif d == 0 and r0 == r1:
        print("coincident circle")
    #mathematical bullshit
    a = (r0**2 - r1**2 + d**2) / (2*d)
    h = (r0**2 - a**2) ** (0.5)
    P2x = P0x + a * (P1x - P0x) / d
    P2y = P0y + a * (P1y - P0y) / d
    #two sets because two circles have two intersecting points
    P3x_Neg = P2x - a * (P1y - P0y) / d
    P3y_Neg = P2y - h * (P1x - P0x) / d
    P3x_Pos = P2x + a * (P1y - P0y) / d
    P3y_Pos = P2y + h * (P1x - P0x) / d
     #closest point to Tower D get picked via distance formula
    Dist_Neg = abs(r4 - ((P4x-P3x_Neg)**2 + (P4y-P3y_Neg)**2)**0.5)
    Dist_Pos = abs(r4 - ((P4x-P3x_Pos)**2 + (P4y-P3y_Pos)**2)**0.5)
    if Dist_Neg <= Dist_Pos:
        return (P3x_Neg,P3y_Neg)
    else:
        return (P3x_Pos,P3y_Pos)


""" Takes in distances for the three towers and outputs the best fit for an x,y, coord.
Assumes numbers are mathematically correct but they aren't get really innacurate really quick.
Tower A and D are at an angle from each other so the Point_select() function cannot generate a 
third intersecting point. With a third intersecting point a triangle can be formed and from that,
the centroid, or center mass of the triangle would give a more accurate, error resistant answer.
https://brilliant.org/wiki/triangles-centroid/  """

def iGPS(rA, rC, rD):#tower a, b, c distances
    #Tower A
    Ax = 6.0
    Ay = -6.0
    #Tower C
    Cx = 6.0
    Cy = 114.0
    #Tower D
    Dx = 102.0
    Dy = 114.0
    
    #4th point is the selector
    P1 = Point_Select(Cy,Cx,rC, Ay,Ax,rA, Dy, Dx, rD)
    j, i = P1
    P1 = i,j#gets flipped because Tower C to A is along the y axis
    P2 = Point_Select(Cx,Cy,rC, Dx,Dy,rD, Ax, Ay, rA)
    screen = P1[1], P2[0]#y from P1 and x from P2--intersecting lines
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')
    # print something to the screen of the device, needs updating to clear screen between values
    print('Distance from a: ', q)
    print('Distance from b: ', w)
    print('Distance from c: ', e)
    print('X = ',screen[0], 'Y = ', screen[1])
    # print something to the output panel in VS Code
    debug_print('Displaying values')
    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)
    Sound.beep #to be replaced with a click sound

#test distances that would normally be inputted via ssh, to be added later... x = 0 y = 0
q = (72.)**(1/2)
w = (6.**2+114.**2)**(1/2)
e = (102.**2+114.**2)**(1/2)
iGPS(q,w,e)
