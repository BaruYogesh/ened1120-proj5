#!/usr/bin/env python3

from subtask_3 import toggleClaw, move, openClaw, claw, SpeedPercent, td


dist = float(input("Input distance to move"))

dist = dist-11
#openClaw = True

move(dist, True)

td.on_for_rotations(20,20,0.0588235*6)

claw.on_for_rotations(SpeedPercent(80),-1.75)
move(dist+6, False)



