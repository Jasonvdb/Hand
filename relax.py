#!/usr/bin/python

from PCA9685 import PCA9685
from hand_config import *

def relax_hand(pwm=None):
    """Relax all fingers to open position to release servo tension.
    
    Args:
        pwm: Optional PCA9685 instance. If not provided, creates a new one.
    """
    # Create PWM instance if not provided
    if pwm is None:
        pwm = PCA9685(PCA9685_ADDRESS, debug=False)
        pwm.setPWMFreq(PWM_FREQUENCY)
    
    print("Relaxing all fingers to open position...")
    
    for channel in ALL_FINGERS:
        open_pulse = get_open_pulse(channel)
        pwm.setServoPulse(channel, open_pulse)
    
    print("All fingers relaxed and extended")

# If run directly, execute the relax function
if __name__ == "__main__":
    relax_hand()