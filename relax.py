#!/usr/bin/python

from PCA9685 import PCA9685

# Initialize PCA9685
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)  # Set frequency to 50Hz for servos

# Define servo positions (in microseconds)
MIN_PULSE = 500   # Minimum pulse width (0.5ms)
MAX_PULSE = 2500  # Maximum pulse width (2.5ms)

# Finger channel mapping
PINKY = 4

print("Relaxing all fingers to open position...")

for channel in range(5):
    if channel != PINKY:
        # Reversed fingers: MAX pulse = open
        pwm.setServoPulse(channel, MAX_PULSE)
    else:
        # Normal pinky: MIN pulse = open
        pwm.setServoPulse(channel, MIN_PULSE)

print("All fingers relaxed and extended")