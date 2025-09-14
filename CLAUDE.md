# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Raspberry Pi-based mechanical hand control system that uses servo motors to control 5 fingers through a PCA9685 PWM driver.

## Hardware Configuration

- **Platform**: Raspberry Pi
- **Servo Controller**: PCA9685 PWM driver at I2C address 0x40
- **Servos**: 5 servos controlling individual fingers
  - Channel 0: Thumb
  - Channel 1: Index finger
  - Channel 2: Middle finger
  - Channel 3: Ring finger
  - Channel 4: Pinky finger

## Development Workflow

### Deploying Code to the Pi

**IMPORTANT: Run the sync script after every Python code change to deploy to the Pi:**

```bash
./sync_with_pi.sh
```

This script:
- Uses rsync to copy all `.py` files to `hand.local:~/Hand`
- Preserves directory structure
- Shows progress during transfer
- Should be run automatically after any Python file modification

### Running Scripts on the Pi

Scripts should be run directly on the Raspberry Pi after syncing:

1. Sync files: `./sync_with_pi.sh`
2. SSH to Pi: `ssh jason@hand.local`
3. Run script: `python ~/Hand/test.py`

### Auto-run on File Changes

For development, use the watch_and_run.sh script on the Pi to automatically run a Python file whenever it changes:

1. SSH to Pi: `ssh jason@hand.local`
2. Start watching: `./watch_and_run.sh test.py`
3. In another terminal, run `./sync_with_pi.sh` after each code change
4. The script will automatically detect changes and re-run the Python file

This enables a rapid development cycle where code changes are automatically executed on the Pi.

## Code Architecture

### Servo Control

The PCA9685 library is included locally in this repository. Import it directly:

```python
from PCA9685 import PCA9685
```

Standard servo pulse widths:
- MIN_PULSE: 500 microseconds (finger open/extended)
- MID_PULSE: 1500 microseconds (finger neutral)
- MAX_PULSE: 2500 microseconds (finger closed/flexed)

### Using hand_config.py

When creating new scripts, always import and use the hand_config module for consistent configuration:

```python
#!/usr/bin/python
from PCA9685 import PCA9685
from hand_config import *

# Initialize the PCA9685
pwm = PCA9685(PCA9685_ADDRESS)
pwm.setPWMFreq(PWM_FREQUENCY)

# Use predefined finger channels
pwm.setServoPulse(THUMB, get_open_pulse(THUMB))
pwm.setServoPulse(INDEX, get_closed_pulse(INDEX))

# Work with all fingers
for finger in ALL_FINGERS:
    pulse = get_neutral_pulse(finger)
    pwm.setServoPulse(finger, pulse)
```

Key configuration features:
- **Finger Constants**: Use `THUMB`, `INDEX`, `MIDDLE`, `RING`, `PINKY` instead of raw channel numbers
- **Pulse Functions**: Use `get_open_pulse()`, `get_closed_pulse()`, `get_neutral_pulse()` to handle reversed servo logic automatically
- **Reversed Logic**: Thumb, Index, Middle, Ring use reversed logic (MAX=open, MIN=closed). Pinky uses normal logic
- **Finger Offsets**: Pinky has a 100μs offset from fully open position for optimal positioning
- **Timing**: Use `MOVEMENT_DELAY` (1 second) between servo movements

## Important Notes

- All Python scripts must include the shebang `#!/usr/bin/python` for execution on the Pi
- The PCA9685 library is only available on the Pi, not in local development
- Use 50Hz PWM frequency for servo control
- Allow 1 second delay between servo movements for smooth operation
- **IMPORTANT**: Always call the `relax_hand()` function from `relax.py` at the end of each script to release servo tension:
  ```python
  from relax import relax_hand
  # ... your code ...
  relax_hand(pwm)  # Pass your pwm instance, or None to create a new one
  ```