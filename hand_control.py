#!/usr/bin/python

"""
High-level abstraction for controlling the mechanical hand.
Provides simple methods for common hand operations without directly managing PWM.
"""

import time
from PCA9685 import PCA9685
from hand_config import *


class HandController:
    """Controller class for the mechanical hand with simplified methods."""
    
    def __init__(self, debug=False):
        """Initialize the hand controller with PWM setup."""
        self.pwm = PCA9685(PCA9685_ADDRESS, debug=debug)
        self.pwm.setPWMFreq(PWM_FREQUENCY)
        self.debug = debug
    
    def open_finger(self, channel):
        """Open/extend a single finger."""
        if self.debug:
            print(f"  Opening {FINGER_NAMES[channel]}")
        pulse = get_open_pulse(channel)
        self.pwm.setServoPulse(channel, pulse)
    
    def close_finger(self, channel):
        """Close/flex a single finger."""
        if self.debug:
            print(f"  Closing {FINGER_NAMES[channel]}")
        pulse = get_closed_pulse(channel)
        self.pwm.setServoPulse(channel, pulse)
    
    def neutral_finger(self, channel):
        """Move a single finger to neutral position."""
        if self.debug:
            print(f"  Moving {FINGER_NAMES[channel]} to neutral")
        pulse = get_neutral_pulse(channel)
        self.pwm.setServoPulse(channel, pulse)
    
    def open_all(self):
        """Open all fingers to extended position."""
        if self.debug:
            print("Opening all fingers...")
        for channel in ALL_FINGERS:
            self.open_finger(channel)
    
    def close_all(self):
        """Close all fingers to make a fist."""
        if self.debug:
            print("Closing all fingers...")
        for channel in ALL_FINGERS:
            self.close_finger(channel)
    
    def relax(self):
        """Relax all fingers to open position to release servo tension."""
        if self.debug:
            print("Relaxing all fingers to open position...")
        self.open_all()
        if self.debug:
            print("All fingers relaxed and extended")
    
    def test_finger(self, channel, delay=None):
        """Test a single finger by opening and closing it."""
        if delay is None:
            delay = MOVEMENT_DELAY
        
        finger_name = FINGER_NAMES[channel]
        if self.debug:
            print(f"\nTesting {finger_name}")
        
        self.open_finger(channel)
        time.sleep(delay)
        
        self.close_finger(channel)
        time.sleep(delay)
    
    def test_all_fingers(self, delay=None):
        """Test all fingers individually."""
        if delay is None:
            delay = MOVEMENT_DELAY
        
        for channel in ALL_FINGERS:
            self.test_finger(channel, delay)
    
    def make_fist(self, hold_time=None):
        """Close all fingers to make a fist and hold."""
        if hold_time is None:
            hold_time = MOVEMENT_DELAY * 2
        
        if self.debug:
            print("Making a fist - closing all fingers")
        
        self.close_all()
        time.sleep(hold_time)
    
    def point_middle(self, hold_time=None):
        """Make pointing gesture with middle finger extended."""
        if hold_time is None:
            hold_time = MOVEMENT_DELAY * 2
        
        if self.debug:
            print("Making pointing gesture - closing all fingers except middle")
        
        for channel in ALL_FINGERS:
            if channel == MIDDLE:
                self.open_finger(channel)
            else:
                self.close_finger(channel)
        
        time.sleep(hold_time)
    
    def wave(self, cycles=3, delay=0.3):
        """Wave fingers in sequence."""
        if self.debug:
            print(f"Waving fingers {cycles} times...")
        
        for _ in range(cycles):
            # Close fingers in sequence
            for channel in ALL_FINGERS:
                self.close_finger(channel)
                time.sleep(delay)
            
            # Open fingers in reverse sequence
            for channel in reversed(ALL_FINGERS):
                self.open_finger(channel)
                time.sleep(delay)
    
    def set_finger_position(self, channel, pulse):
        """Set a finger to a specific pulse width (advanced use)."""
        self.pwm.setServoPulse(channel, pulse)


# Convenience functions for backward compatibility and simple scripts
_default_controller = None


def get_hand():
    """Get or create the default hand controller instance."""
    global _default_controller
    if _default_controller is None:
        _default_controller = HandController(debug=True)
    return _default_controller


def open_finger(channel):
    """Open a single finger using default controller."""
    get_hand().open_finger(channel)


def close_finger(channel):
    """Close a single finger using default controller."""
    get_hand().close_finger(channel)


def open_all():
    """Open all fingers using default controller."""
    get_hand().open_all()


def close_all():
    """Close all fingers using default controller."""
    get_hand().close_all()


def relax_hand():
    """Relax all fingers using default controller."""
    get_hand().relax()


def test_finger(channel, delay=None):
    """Test a single finger using default controller."""
    get_hand().test_finger(channel, delay)


def test_all_fingers(delay=None):
    """Test all fingers using default controller."""
    get_hand().test_all_fingers(delay)


def make_fist(hold_time=None):
    """Make a fist using default controller."""
    get_hand().make_fist(hold_time)


def point_middle(hold_time=None):
    """Make pointing gesture using default controller."""
    get_hand().point_middle(hold_time)


def wave(cycles=3, delay=0.3):
    """Wave fingers using default controller."""
    get_hand().wave(cycles, delay)