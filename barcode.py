#!/usr/bin/env python3

from subtask_3 import barcode, debug_print
from sound import speech_output
import random
import time


boxType = barcode()
debug_print(boxType)

if(boxType<0):
    speech_output(str(random.randint(1,4)))
else:
    speech_output(str(boxType))


#print(random.randint(1,4))
time.sleep(10)