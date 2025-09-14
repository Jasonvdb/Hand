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

The repository includes a sync script that automatically copies Python files to the Raspberry Pi:

```bash
./sync_with_pi.sh
```

This script:
- Uses rsync to copy all `.py` files to `hand.local:~/Hand`
- Preserves directory structure
- Shows progress during transfer

### Running Scripts on the Pi

Scripts should be run directly on the Raspberry Pi after syncing:

1. Sync files: `./sync_with_pi.sh`
2. SSH to Pi: `ssh jason@hand.local`
3. Run script: `python ~/Hand/test.py`

## Code Architecture

### Servo Control

All servo control is done through the PCA9685 library located at `/home/jason/Bot/example_code/python` on the Pi. Scripts must add this to the Python path:

```python
sys.path.append('/home/jason/Bot/example_code/python')
from PCA9685 import PCA9685
```

Standard servo pulse widths:
- MIN_PULSE: 500 microseconds (finger open/extended)
- MID_PULSE: 1500 microseconds (finger neutral)
- MAX_PULSE: 2500 microseconds (finger closed/flexed)

## Important Notes

- All Python scripts must include the shebang `#!/usr/bin/python` for execution on the Pi
- The PCA9685 library is only available on the Pi, not in local development
- Use 50Hz PWM frequency for servo control
- Allow 1 second delay between servo movements for smooth operation