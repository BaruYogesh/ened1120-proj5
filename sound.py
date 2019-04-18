#!/usr/bin/env python3
 
from ev3dev2.sound import Sound

#just a silly speech program, doesn't do anything too useful.
speech = input("Input speech")
sound = Sound()
str_en = "Hello. My name is baru"


sound.speak(speech, espeak_opts='-a 200 -s 130 -ven+m1')