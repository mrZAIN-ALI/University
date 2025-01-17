import json
import os

# List of JSON file paths to combine
json_files = [
    "file1.json",
    "file2.json",
    "file3.json",
    "file4.json",
    "file5.json"
]

combined_data = []

# Loop through each file, load its data and add to the combined_data list
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        combined_data.extend(data)  # Add the contents of each file to the combined list

# Write the combined data to a new JSON file
with open('combined.json', 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print("Combined JSON file saved as 'combined.json'")
