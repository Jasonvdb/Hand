#!/usr/bin/python

from PCA9685 import PCA9685
from hand_config import *

# Initialize PCA9685
pwm = PCA9685(PCA9685_ADDRESS, debug=False)
pwm.setPWMFreq(PWM_FREQUENCY)

print("Relaxing all fingers to open position...")

for channel in ALL_FINGERS:
    open_pulse = get_open_pulse(channel)
    pwm.setServoPulse(channel, open_pulse)

print("All fingers relaxed and extended")