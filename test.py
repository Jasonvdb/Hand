#!/usr/bin/python

from hand_control import HandController

# Initialize hand controller
hand = HandController(debug=True)

print("Starting mechanical hand test - bending each finger fully")

# Test all fingers individually
hand.test_all_fingers()

# Relax hand to release servo tension
hand.relax()
print("Hand test complete")