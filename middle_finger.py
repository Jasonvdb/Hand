#!/usr/bin/python

from hand_control import HandController

# Initialize hand controller
hand = HandController(debug=True)

print("Making pointing gesture - closing all fingers except middle")

# Make pointing gesture with middle finger
hand.point_middle()

# Relax hand to release servo tension
hand.relax()
print("Pointing gesture complete")