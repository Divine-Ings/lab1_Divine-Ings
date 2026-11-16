#!/bin/bash
# analyze_log.sh
# Reads transit_session.log and prints a short summary

# use the file given as the first argument, or transit_session.log if none
if [ -n "$1" ]; then
    LOG_FILE="$1"
else
    LOG_FILE="transit_session.log"
fi

# if the file does not exist, print an error and stop
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: log file '$LOG_FILE' not found."
    exit 1
fi

echo "===== LOG ANALYSER ====="
echo "File: $LOG_FILE"
echo ""

# count how many sessions (runs) the log contains
sessions=$(grep -c "New session started" "$LOG_FILE")
echo "Sessions (runs)     : $sessions"

# count zebra crossing stops and lane changes
zebras=$(grep -c "Zebra crossing!" "$LOG_FILE")
lanes=$(grep -c "Changing lane:" "$LOG_FILE")
echo "Zebra stops         : $zebras"
echo "Lane changes        : $lanes"
echo ""

# show the driver name and top speed of the latest trip
echo "----- Latest trip -----"

# get the last "Driver : ..." line from the trip report
driver=$(grep "Driver            :" "$LOG_FILE" | tail -n 1)
if [ -z "$driver" ]; then
    # fall back to the "begins the journey" line if report is missing
    driver=$(grep "begins the journey" "$LOG_FILE" | tail -n 1)
    if [ -z "$driver" ]; then
        echo "Driver name         : (not found)"
    else
        # pull the name from the start of that sentence
        name=$(echo "$driver" | sed 's/.*] //' | sed 's/ begins the journey.*//')
        echo "Driver name         : $name"
    fi
else
    # strip the timestamp and label, keep the name
    name=$(echo "$driver" | sed 's/.*Driver            : //')
    echo "Driver name         : $name"
fi

top_speed=$(grep "Top speed" "$LOG_FILE" | tail -n 1)
if [ -z "$top_speed" ]; then
    echo "Top speed           : (not found)"
else
    speed=$(echo "$top_speed" | sed 's/.*Top speed         : //')
    echo "Top speed           : $speed"
fi

echo "========================"
