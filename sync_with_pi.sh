#!/bin/bash

# Configuration
PI_USER="jason"
PI_HOST="hand.local"
PI_PATH="~/Hand"
LOCAL_PATH="/Users/jason/Documents/Repositories/Hand"

# Copy Python files and shell scripts to Pi
echo "Copying .py and .sh files to $PI_USER@$PI_HOST:$PI_PATH"
rsync -avz --progress \
    --include='*.py' \
    --include='*.sh' \
    --include='*/' \
    --exclude='*' \
    "$LOCAL_PATH/" "$PI_USER@$PI_HOST:$PI_PATH/"

if [ $? -eq 0 ]; then
    echo "✓ Python and shell files copied successfully"
else
    echo "✗ Copy failed"
    exit 1
fi