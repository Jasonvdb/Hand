#!/bin/bash

# Check if a file argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_file>"
    echo "Example: $0 test.py"
    exit 1
fi

PYTHON_FILE="$1"

# Check if the file exists
if [ ! -f "$PYTHON_FILE" ]; then
    echo "Error: File '$PYTHON_FILE' not found"
    exit 1
fi

# Check if it's a Python file
if [[ ! "$PYTHON_FILE" =~ \.py$ ]]; then
    echo "Warning: '$PYTHON_FILE' doesn't have .py extension"
fi

echo "Watching '$PYTHON_FILE' for changes..."
echo "Press Ctrl+C to stop"
echo "----------------------------------------"

# Store the last modification time
LAST_MOD=$(stat -c %Y "$PYTHON_FILE" 2>/dev/null || stat -f %m "$PYTHON_FILE" 2>/dev/null)

# Initial run
echo "[$(date '+%H:%M:%S')] Running $PYTHON_FILE..."
python "$PYTHON_FILE"
echo "----------------------------------------"

# Watch for changes
while true; do
    # Get current modification time
    CURRENT_MOD=$(stat -c %Y "$PYTHON_FILE" 2>/dev/null || stat -f %m "$PYTHON_FILE" 2>/dev/null)
    
    # Check if file has been modified
    if [ "$CURRENT_MOD" != "$LAST_MOD" ]; then
        LAST_MOD=$CURRENT_MOD
        echo "[$(date '+%H:%M:%S')] File changed, running $PYTHON_FILE..."
        python "$PYTHON_FILE"
        echo "----------------------------------------"
    fi
    
    # Sleep for a short interval before checking again
    sleep 1
done