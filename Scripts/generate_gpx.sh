#!/bin/bash

# Define paths
# Assumes script is running from the Project Root (Xcode default)
CONFIG_FILE="Poofy/Configuration.swift"
OUTPUT_FILE="Poofy/SimulatedLocation.gpx"

# Check if Config exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Configuration file not found at $CONFIG_FILE"
    exit 1
fi

# Extract values using simple text parsing
# Trims spaces and commas
LAT=$(grep "static let centerLatitude" "$CONFIG_FILE" | awk -F'=' '{print $2}' | tr -d ' ,')
LON=$(grep "static let centerLongitude" "$CONFIG_FILE" | awk -F'=' '{print $2}' | tr -d ' ,')
RADIUS=$(grep "static let radiusInMeters" "$CONFIG_FILE" | awk -F'=' '{print $2}' | tr -d ' ,')

# Use Python to generate a valid GPX file
# We effectively "simulate" the random generator here in the build script
python3 -c "
import math
import random

lat = float($LAT)
lon = float($LON)
radius = float($RADIUS)

# Convert radius from meters to degrees (approx)
radiusInDegrees = radius / 111000.0

u = random.random()
v = random.random()
w = radiusInDegrees * math.sqrt(u)
t = 2 * math.pi * v
x = w * math.cos(t)
y = w * math.sin(t)

newLat = lat + y
newLon = lon + x

gpx_content = f'''<?xml version=\"1.0\"?>
<gpx version=\"1.1\" creator=\"Poofy\">
    <wpt lat=\"{newLat:.6f}\" lon=\"{newLon:.6f}\">
        <name>Poofy Random Location</name>
        <time>2024-01-01T00:00:00Z</time>
    </wpt>
</gpx>
'''

print(gpx_content)
" > "$OUTPUT_FILE"

echo "✅ Generated $OUTPUT_FILE from Configuration: Center($LAT, $LON) Radius($RADIUS)m"
