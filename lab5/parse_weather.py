#!/usr/bin/env python3

# Import necessary modules
import requests
import statistics

# Fetch METAR data from the provided URL
url = "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"
response = requests.get(url)
data = response.json()

# Task 1: Print first six receiptTime values (creatively using slicing)
print("Receipt Times:")
for entry in data[:6]:
    print(entry['receiptTime'])

# Task 2: Extract temperatures and calculate average
temperatures = [entry['temp'] for entry in data if entry['temp'] is not None]

if temperatures:
    average_temp = statistics.mean(temperatures)
    print(f"Average Temperature: {average_temp:.2f} °C")
else:
    print("Average Temperature: No temperature data available")

# Task 3: Determine if majority of observations were cloudy
total_cloud_entries = 0
cloudy_entries = 0

for entry in data:
    clouds = entry.get('clouds', [])
    for cloud in clouds:
        total_cloud_entries += 1
        if cloud['cover'] != "CLR":
            cloudy_entries += 1

mostly_cloudy = cloudy_entries > (total_cloud_entries / 2)
print(f"Mostly Cloudy: {mostly_cloudy}")
