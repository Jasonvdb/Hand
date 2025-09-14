#!/usr/bin/python

from hand_control import HandController

# Initialize hand controller
hand = HandController(debug=True)

print("Making a fist - closing all fingers")

# Make a fist and hold
hand.make_fist()

# Relax hand to release servo tension
hand.relax()
print("Grip complete")