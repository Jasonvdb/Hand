#!/bin/bash

# Configuration
PI_USER="jason"
PI_HOST="hand.local"
PI_PATH="~/Hand"
LOCAL_PATH="/Users/jason/Documents/Repositories/Hand"

# Copy Python files to Pi
echo "Copying .py files to $PI_USER@$PI_HOST:$PI_PATH"
rsync -avz --progress \
    --include='*.py' \
    --include='*/' \
    --exclude='*' \
    "$LOCAL_PATH/" "$PI_USER@$PI_HOST:$PI_PATH/"

if [ $? -eq 0 ]; then
    echo "✓ Python files copied successfully"
else
    echo "✗ Copy failed"
    exit 1
fi