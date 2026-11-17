#!/bin/bash

# The log file that stores logs from the transit system
LOG_FILE=${1:-transit_session.log}

if [ ! -f "$LOG_FILE" ]; then
    echo "Error: File '$LOG_FILE' not found."
    exit 1
fi

echo "******* LOG ANALYSER *******"
echo "File: $LOG_FILE"
echo ""

# Count transit sessions, zebra stops, and lane changes
sessions=$(grep -c "New session started" "$LOG_FILE")
zebras=$(grep -c "Zebra crossing!" "$LOG_FILE")
lanes=$(grep -c "Changing lane:" "$LOG_FILE")

echo "Transit sessions: $sessions"
echo "Zebra stops: $zebras"
echo "Lane changes: $lanes"
echo ""

# Get the latest driver's name
echo "===== Latest trip ====="

driver=$(grep "Driver:    " "$LOG_FILE" | tail -n 1)

if [ -n "$driver" ]; then
    name=$(echo "$driver" | sed 's/.*Driver:    //')
else
    driver=$(grep "begins the journey" "$LOG_FILE" | tail -n 1)

    if [ -n "$driver" ]; then
        name=$(echo "$driver" | sed 's/.*] //' | sed 's/ begins the journey.*//')
    else
        name="(not found)"
    fi
fi

echo "Driver name    : $name"

speed=$(grep "Top speed" "$LOG_FILE" | tail -n 1)

if [ -n "$speed" ]; then
    speed=$(echo "$speed" | sed 's/.*Top speed     : //')
else
    speed="(not found)"
fi

echo "Top speed      : $speed"
echo "========================"
echo ""


