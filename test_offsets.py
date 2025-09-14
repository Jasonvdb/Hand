#!/usr/bin/python

"""
Test the updated finger offsets.
Opens all fingers to their fully open position with offsets applied.
"""

from PCA9685 import PCA9685
from hand_config import *
import time

# Initialize the PCA9685
pwm = PCA9685(PCA9685_ADDRESS)
pwm.setPWMFreq(PWM_FREQUENCY)

print("Testing finger offsets...")
print("Opening all fingers with configured offsets:\n")

# Open each finger and display its pulse width
for finger in ALL_FINGERS:
    pulse = get_open_pulse(finger)
    offset = FINGER_OFFSETS[finger]
    
    print(f"{FINGER_NAMES[finger]}:")
    print(f"  Offset: {offset}μs")
    print(f"  Open pulse: {pulse}μs")
    
    pwm.setServoPulse(finger, pulse)
    time.sleep(0.5)  # Small delay between each finger

print("\nAll fingers opened with offsets applied.")
print("\nIndex finger has 200μs offset (more inward)")
print("Middle and Pinky have 100μs offset (slightly inward)")
print("Thumb and Ring have no offset (fully open)")

# Relax hand at the end
from relax import relax_hand
time.sleep(2)
relax_hand(pwm)