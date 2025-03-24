#!/usr/bin/env python3

import json
import pandas as pd

# Step i: Read JSON file
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# Step ii: Extract the four fields clearly
extracted_data = []
for entry in data:
    name = entry['name']
    html_url = entry['html_url']
    updated_at = entry['updated_at']
    visibility = entry['visibility']
    extracted_data.append([name, html_url, updated_at, visibility])

# Step iii: Create DataFrame and clearly export first 5 lines to CSV
df = pd.DataFrame(extracted_data, columns=['name', 'html_url', 'updated_at', 'visibility'])

# Export only first 5 rows
df.head(5).to_csv('chacon.csv', index=False, header=False)
