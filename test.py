#!/usr/bin/python

import time
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
    
    # Reverse logic for all fingers except pinky (channel 4)
    if channel != PINKY:
        # Reversed: MAX pulse = open, MIN pulse = closed
        print(f"  {finger}: Opening (MAX position - reversed)")
        pwm.setServoPulse(channel, MAX_PULSE)
        time.sleep(1)
        
        print(f"  {finger}: Closing (MIN position - reversed)")
        pwm.setServoPulse(channel, MIN_PULSE)
        time.sleep(1)
        
        print(f"  {finger}: Neutral (CENTER position)")
        pwm.setServoPulse(channel, MID_PULSE)
        time.sleep(1)
    else:
        # Normal: MIN pulse = open, MAX pulse = closed
        print(f"  {finger}: Opening (MIN position)")
        pwm.setServoPulse(channel, MIN_PULSE)
        time.sleep(1)
        
        print(f"  {finger}: Closing (MAX position)")
        pwm.setServoPulse(channel, MAX_PULSE)
        time.sleep(1)
        
        print(f"  {finger}: Neutral (CENTER position)")
        pwm.setServoPulse(channel, MID_PULSE)
        time.sleep(1)

print("\nRelaxing all fingers to open position...")
for channel in range(5):
    if channel != PINKY:
        # Reversed fingers: MAX pulse = open
        pwm.setServoPulse(channel, MAX_PULSE)
    else:
        # Normal pinky: MIN pulse = open
        pwm.setServoPulse(channel, MIN_PULSE)
    
print("Hand test complete - all fingers relaxed and extended")