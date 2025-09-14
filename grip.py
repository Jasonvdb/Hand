#!/usr/bin/python

import time
from PCA9685 import PCA9685
from hand_config import *
from relax import relax_hand

# Initialize PCA9685
pwm = PCA9685(PCA9685_ADDRESS, debug=False)
pwm.setPWMFreq(PWM_FREQUENCY)

print("Making a fist - closing all fingers")

# Close all fingers simultaneously to make a fist
for channel in ALL_FINGERS:
    finger = FINGER_NAMES[channel]
    closed_pulse = get_closed_pulse(channel)
    print(f"  Closing {finger}")
    pwm.setServoPulse(channel, closed_pulse)

# Hold the fist position
time.sleep(MOVEMENT_DELAY * 2)

# Relax hand to release servo tension
relax_hand(pwm)
print("Grip complete")