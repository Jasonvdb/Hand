#!/usr/bin/python

import time
from PCA9685 import PCA9685
from hand_config import *
from relax import relax_hand

# Initialize PCA9685
pwm = PCA9685(PCA9685_ADDRESS, debug=False)
pwm.setPWMFreq(PWM_FREQUENCY)

print("Starting mechanical hand test - controlling 5 finger servos")

# Test each finger individually
for channel in ALL_FINGERS:
    finger = FINGER_NAMES[channel]
    print(f"\nTesting {finger} (channel {channel})")
    
    # Get appropriate pulse values based on finger configuration
    open_pulse = get_open_pulse(channel)
    closed_pulse = get_closed_pulse(channel)
    neutral_pulse = get_neutral_pulse(channel)
    
    # Describe the logic for clarity
    logic_type = "reversed" if is_reversed(channel) else "normal"
    print(f"  Using {logic_type} servo logic")
    
    print(f"  {finger}: Opening")
    pwm.setServoPulse(channel, open_pulse)
    time.sleep(MOVEMENT_DELAY)
    
    print(f"  {finger}: Closing")
    pwm.setServoPulse(channel, closed_pulse)
    time.sleep(MOVEMENT_DELAY)
    
    print(f"  {finger}: Neutral")
    pwm.setServoPulse(channel, neutral_pulse)
    time.sleep(MOVEMENT_DELAY)

# Relax hand to release servo tension
relax_hand(pwm)
print("Hand test complete")