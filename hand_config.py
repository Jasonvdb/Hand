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

# Finger offsets from fully open position (in microseconds)
# Positive values move the finger slightly inward from fully open
FINGER_OFFSETS = {
    THUMB: 0,     # No offset
    INDEX: 0,   # No offset
    MIDDLE: 300,  # Slight inward position (~5 degrees)
    RING: 0,      # No offset
    PINKY: 100    # Slight inward position (~5 degrees)
}

# Finger closed position offsets (in microseconds)
# For fingers that need extra pull to fully close
FINGER_CLOSED_OFFSETS = {
    THUMB: 0,     # No offset
    INDEX: 300,   # Less pull (300μs back from fully closed)
    MIDDLE: -200, # Extra pull for full closure
    RING: 200,    # Less pull (200μs back from fully closed)
    PINKY: -400   # Less pull (400μs back from fully closed for normal logic)
}

# Timing delays
MOVEMENT_DELAY = 1  # seconds between servo movements


def is_reversed(channel):
    """Check if a finger channel uses reversed servo logic."""
    return channel in REVERSED_FINGERS


def get_open_pulse(channel):
    """Get the pulse width for open/extended position for a given finger."""
    base_pulse = MAX_PULSE if is_reversed(channel) else MIN_PULSE
    offset = FINGER_OFFSETS.get(channel, 0)
    
    # Apply offset in the correct direction
    if is_reversed(channel):
        # For reversed fingers, subtract offset to move inward
        return base_pulse - offset
    else:
        # For normal fingers, add offset to move inward
        return base_pulse + offset


def get_closed_pulse(channel):
    """Get the pulse width for closed/flexed position for a given finger."""
    base_pulse = MIN_PULSE if is_reversed(channel) else MAX_PULSE
    offset = FINGER_CLOSED_OFFSETS.get(channel, 0)
    
    # Apply offset (negative values pull harder/further)
    return base_pulse + offset


def get_neutral_pulse(channel):
    """Get the pulse width for neutral position for any finger."""
    return MID_PULSE