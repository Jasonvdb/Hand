#!/usr/bin/python

import time
import sys
sys.path.append('/home/jason/Bot/example_code/python')
from PCA9685 import PCA9685

# Initialize PCA9685
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)  # Set frequency to 50Hz for servos

# Define servo positions (in microseconds)
MIN_PULSE = 500   # Minimum pulse width (0.5ms)
MID_PULSE = 1500  # Middle position (1.5ms)
MAX_PULSE = 2500  # Maximum pulse width (2.5ms)

# Finger channel mapping
THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4

finger_names = {
    THUMB: "Thumb",
    INDEX: "Index",
    MIDDLE: "Middle",
    RING: "Ring",
    PINKY: "Pinky"
}

print("Starting mechanical hand test - controlling 5 finger servos")

# Test each finger individually
for channel in range(5):
    finger = finger_names[channel]
    print(f"\nTesting {finger} (channel {channel})")
    
    # Move to minimum position (finger open)
    print(f"  {finger}: Opening (MIN position)")
    pwm.setServoPulse(channel, MIN_PULSE)
    time.sleep(1)
    
    # Move to maximum position (finger closed)
    print(f"  {finger}: Closing (MAX position)")
    pwm.setServoPulse(channel, MAX_PULSE)
    time.sleep(1)
    
    # Return to center position (finger neutral)
    print(f"  {finger}: Neutral (CENTER position)")
    pwm.setServoPulse(channel, MID_PULSE)
    time.sleep(1)

print("\nHand test complete - all 5 fingers have been tested")