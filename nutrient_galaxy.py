import pandas as pd
import json
import os

# Load the cleaned normalized data CSV
df = pd.read_csv('data/clean_normalized_data.csv')

# Drop duplicate descriptions while keeping the first occurrence
df_unique = df.drop_duplicates(subset=['description'])

# Define the relevant generic descriptions to filter
relevant_descriptions = [
    'soda', 'chips', 'fries', 'candy', 'snacks',
    'pizza', 'burger', 'ice cream', 'energy drinks', 'sandwich'
]

# Filter the data to include only rows with relevant descriptions (case insensitive)
filtered_data = df_unique[df_unique['description'].str.lower().isin(relevant_descriptions)]

# Select only the relevant columns for the Nutrient Galaxy
galaxy_data = filtered_data[[
    'description', 'category', 'brand',
    'calories', 'protein', 'fat', 'carbs'
]]

# Convert the data to a dictionary format suitable for JSON export
data_dict = galaxy_data.to_dict(orient='records')

# Ensure the output directory exists
os.makedirs('data', exist_ok=True)

# Write the data to a JSON file
json_path = 'data/planet_data.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)

print(f'✅ JSON data with specific descriptions generated and saved as {json_path}')
