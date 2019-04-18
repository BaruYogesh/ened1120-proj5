#!/usr/bin/env python3

from subtask_3 import toggleClaw, move

dist = float(input("Input distance to move"))

move(dist, True)
toggleClaw()
move(3,True)
toggleClaw()
move(dist, False)

