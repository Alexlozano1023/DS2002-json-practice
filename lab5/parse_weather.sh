#!/bin/bash

# Fetch fresh METAR data from provided URL
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" -o aviation.json

# Task 4: Output first six receiptTime values (creative way using a loop)
echo "Receipt Times:"
receipt_times=$(jq -r '.[].receiptTime' aviation.json)
counter=0
echo "$receipt_times" | while read -r line && [ $counter -lt 6 ]; do
    echo "$line"
    ((counter++))
done

# Task 5 & 6: Calculate average temperature using the correct field 'temp'
temps=$(jq '[.[].temp | select(. != null)]' aviation.json)
temp_count=$(echo "$temps" | jq 'length')

if [ "$temp_count" -eq 0 ]; then
    echo "Average Temperature: No temperature data available"
else
    avg_temp=$(echo "$temps" | jq 'add / length')
    echo "Average Temperature: $avg_temp"
fi

# Task 7 & 8: Determine if majority of observations were cloudy (not "CLR")
cloudy_count=$(jq '[.[].clouds[].cover != "CLR"] | map(select(.==true)) | length' aviation.json)
total_entries=$(jq '[.[].clouds[].cover] | length' aviation.json)

if [ "$cloudy_count" -gt $((total_entries / 2)) ]; then
    echo "Mostly Cloudy: true"
else
    echo "Mostly Cloudy: false"
fi



