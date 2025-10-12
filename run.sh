#!/bin/bash

# Quick start script for Burokrat.site

echo "🚀 Starting Burokrat.site..."
echo ""

# Function to kill processes on a specific port
kill_port() {
    local port=$1
    echo "Checking for processes on port $port..."
    
    # Find processes using the port
    pids=$(lsof -ti:$port 2>/dev/null)
    
    if [ ! -z "$pids" ]; then
        echo "Found processes on port $port: $pids"
        echo "Killing existing processes..."
        kill -9 $pids 2>/dev/null
        sleep 1
        echo "✅ Cleaned up port $port"
    else
        echo "✅ Port $port is free"
    fi
}

# Clean up ports that might be in use
kill_port 8080
kill_port 5001

echo ""
echo "Installing dependencies..."
pip3 install -q -r requirements.txt

echo ""
echo "Starting FastHTML server..."
echo "Open your browser at: http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
