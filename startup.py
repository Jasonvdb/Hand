#!/usr/bin/python

"""
Startup script that performs a wave movement for 2 cycles with pinky down,
then a pointing gesture for 3 seconds before relaxing.
"""

import time
from hand_control import HandController
from hand_config import *

def main():
    print("Starting hand startup sequence...")

    # Initialize hand controller
    hand = HandController(debug=True)

    try:
        # Custom wave with pinky down for 2 cycles
        print("Performing wave movement with pinky down for 2 cycles...")

        for cycle in range(2):
            print(f"Wave cycle {cycle + 1}/2")

            # Close fingers in sequence (thumb to ring, skip pinky)
            for channel in [THUMB, INDEX, MIDDLE, RING]:
                hand.close_finger(channel)
                time.sleep(0.3)

            # Keep pinky closed for 1 second
            hand.close_finger(PINKY)
            time.sleep(1.0)

            # Open fingers in reverse sequence (ring to thumb, skip pinky)
            for channel in [RING, MIDDLE, INDEX, THUMB]:
                hand.open_finger(channel)
                time.sleep(0.3)

            # Open pinky last
            hand.open_finger(PINKY)
            time.sleep(0.3)

        print("Wave completed. Making pointing gesture...")

        # Point gesture for 3 seconds
        hand.point_middle(hold_time=3.0)

        print("Startup sequence completed. Relaxing hand...")

        # Relax all fingers
        hand.relax()

        print("Hand startup sequence finished successfully")

    except KeyboardInterrupt:
        print("\nStartup sequence interrupted by user")
        hand.relax()
    except Exception as e:
        print(f"Error during startup sequence: {e}")
        hand.relax()

if __name__ == "__main__":
    main()