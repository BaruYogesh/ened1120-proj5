#!/usr/bin/env python3
 
from ev3dev2.sound import Sound

sound = Sound()

#started being useful, now it is for outputting via speech
'''
speech = input("Input speech")
str_en = "Hello. My name is baru"
sound.speak(speech, espeak_opts='-a 200 -s 130 -ven+m1')
'''

def speech_output(s):
    sound.speak(s,espeak_opts='-a 200 -s 130 -ven+m1')