#!/usr/bin/python

import time
from PCA9685 import PCA9685
from hand_config import *
from relax import relax_hand

# Initialize PCA9685
pwm = PCA9685(PCA9685_ADDRESS, debug=False)
pwm.setPWMFreq(PWM_FREQUENCY)

print("Making pointing gesture - closing all fingers except middle")

# Close all fingers except middle finger
for channel in ALL_FINGERS:
    finger = FINGER_NAMES[channel]
    
    if channel == MIDDLE:
        # Keep middle finger extended
        open_pulse = get_open_pulse(channel)
        print(f"  Keeping {finger} extended")
        pwm.setServoPulse(channel, open_pulse)
    else:
        # Close other fingers
        closed_pulse = get_closed_pulse(channel)
        print(f"  Closing {finger}")
        pwm.setServoPulse(channel, closed_pulse)

# Hold the pointing position
time.sleep(MOVEMENT_DELAY * 2)

# Relax hand to release servo tension
relax_hand(pwm)
print("Pointing gesture complete")