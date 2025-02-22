import pandas as pd
import json
import os

# Load the cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Limit the data to 500 rows for performance
df = df.head(500)

# Select relevant columns for the Nutrient Galaxy
galaxy_data = df[[
    'description', 'category', 'brand',
    'calories', 'protein', 'fat', 'carbs',
    'calories_per_protein', 'calories_per_fat', 'calories_per_carb'
]]

# Convert the data to a dictionary format suitable for JSON export
data_dict = galaxy_data.to_dict(orient='records')

# Ensure the output directory exists
os.makedirs('data', exist_ok=True)

# Write the data to a JSON file
json_path = 'data/nutrient_data.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)

print(f"✅ JSON data generated and saved as '{json_path}'")