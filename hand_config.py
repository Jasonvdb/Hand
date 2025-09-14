#!/usr/bin/python

"""
Configuration constants for the mechanical hand control system.
Contains all servo channel mappings, pulse widths, and timing constants.
"""

# I2C Configuration
PCA9685_ADDRESS = 0x40
PWM_FREQUENCY = 50  # Hz for servo control

# Servo pulse widths (in microseconds)
MIN_PULSE = 500   # Minimum pulse width (0.5ms)
MID_PULSE = 1500  # Middle position (1.5ms)
MAX_PULSE = 2500  # Maximum pulse width (2.5ms)

# Finger channel mapping
THUMB = 0
INDEX = 1
MIDDLE = 2
RING = 3
PINKY = 4

# Finger names dictionary
FINGER_NAMES = {
    THUMB: "Thumb",
    INDEX: "Index",
    MIDDLE: "Middle",
    RING: "Ring",
    PINKY: "Pinky"
}

# List of all finger channels
ALL_FINGERS = [THUMB, INDEX, MIDDLE, RING, PINKY]

# Reversed fingers (MAX pulse = open, MIN pulse = closed)
# All fingers except pinky use reversed logic
REVERSED_FINGERS = [THUMB, INDEX, MIDDLE, RING]

# Normal fingers (MIN pulse = open, MAX pulse = closed)
NORMAL_FINGERS = [PINKY]

# Timing delays
MOVEMENT_DELAY = 1  # seconds between servo movements


def is_reversed(channel):
    """Check if a finger channel uses reversed servo logic."""
    return channel in REVERSED_FINGERS


def get_open_pulse(channel):
    """Get the pulse width for open/extended position for a given finger."""
    return MAX_PULSE if is_reversed(channel) else MIN_PULSE


def get_closed_pulse(channel):
    """Get the pulse width for closed/flexed position for a given finger."""
    return MIN_PULSE if is_reversed(channel) else MAX_PULSE


def get_neutral_pulse(channel):
    """Get the pulse width for neutral position for any finger."""
    return MID_PULSE