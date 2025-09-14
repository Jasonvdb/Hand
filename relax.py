#!/usr/bin/python

from hand_control import HandController

def relax_hand(pwm=None):
    """Relax all fingers to open position to release servo tension.
    
    Args:
        pwm: Optional PCA9685 instance. Kept for backward compatibility but ignored.
    """
    hand = HandController(debug=True)
    hand.relax()

# If run directly, execute the relax function
if __name__ == "__main__":
    relax_hand()