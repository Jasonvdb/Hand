#!/usr/bin/python

"""
Command-line interface for controlling the mechanical hand.
Provides easy access to all hand control functions without needing separate scripts.
"""

import sys
import argparse
from hand_control import HandController

def main():
    parser = argparse.ArgumentParser(description='Control the mechanical hand')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Relax command
    relax_parser = subparsers.add_parser('relax', help='Relax all fingers to open position')
    
    # Test commands
    test_parser = subparsers.add_parser('test', help='Test finger movements')
    test_parser.add_argument('--finger', type=int, choices=[0,1,2,3,4], 
                           help='Test specific finger (0=thumb, 1=index, 2=middle, 3=ring, 4=pinky)')
    test_parser.add_argument('--delay', type=float, default=1.0, help='Delay between movements (seconds)')
    
    # Gesture commands
    gesture_parser = subparsers.add_parser('gesture', help='Make hand gestures')
    gesture_parser.add_argument('type', choices=['fist', 'point', 'wave'], help='Gesture type')
    gesture_parser.add_argument('--hold', type=float, help='Hold time for fist/point gestures')
    gesture_parser.add_argument('--cycles', type=int, default=3, help='Number of wave cycles')
    gesture_parser.add_argument('--delay', type=float, default=0.3, help='Wave delay between fingers')
    
    # Individual finger control
    finger_parser = subparsers.add_parser('finger', help='Control individual fingers')
    finger_parser.add_argument('channel', type=int, choices=[0,1,2,3,4], 
                             help='Finger channel (0=thumb, 1=index, 2=middle, 3=ring, 4=pinky)')
    finger_parser.add_argument('action', choices=['open', 'close', 'neutral'], help='Finger action')
    
    # All fingers control
    all_parser = subparsers.add_parser('all', help='Control all fingers')
    all_parser.add_argument('action', choices=['open', 'close'], help='Action for all fingers')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize hand controller
    hand = HandController(debug=args.debug)
    
    try:
        if args.command == 'relax':
            print("Relaxing all fingers to open position...")
            hand.relax()
            
        elif args.command == 'test':
            if args.finger is not None:
                finger_names = ['thumb', 'index', 'middle', 'ring', 'pinky']
                print(f"Testing {finger_names[args.finger]} finger...")
                hand.test_finger(args.finger, args.delay)
            else:
                print("Testing all fingers...")
                hand.test_all_fingers(args.delay)
            hand.relax()
            
        elif args.command == 'gesture':
            if args.type == 'fist':
                print("Making a fist...")
                hand.make_fist(args.hold)
            elif args.type == 'point':
                print("Making pointing gesture...")
                hand.point_middle(args.hold)
            elif args.type == 'wave':
                print(f"Waving {args.cycles} times...")
                hand.wave(args.cycles, args.delay)
            hand.relax()
            
        elif args.command == 'finger':
            finger_names = ['thumb', 'index', 'middle', 'ring', 'pinky']
            print(f"{args.action.capitalize()}ing {finger_names[args.channel]} finger...")
            if args.action == 'open':
                hand.open_finger(args.channel)
            elif args.action == 'close':
                hand.close_finger(args.channel)
            elif args.action == 'neutral':
                hand.neutral_finger(args.channel)
                
        elif args.command == 'all':
            print(f"{args.action.capitalize()}ing all fingers...")
            if args.action == 'open':
                hand.open_all()
            elif args.action == 'close':
                hand.close_all()
                
        print("Command completed successfully")
        
    except KeyboardInterrupt:
        print("\nOperation interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()