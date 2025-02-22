import pandas as pd

# Load the cleaned normalized data CSV
df = pd.read_csv('data/clean_normalized_data.csv')

# Extract unique descriptions from the 'description' column
unique_descriptions = df['description'].unique()

# Save the unique descriptions to a text file
output_file = 'unique_descriptions.txt'
with open(output_file, 'w') as f:
    for description in unique_descriptions:
        f.write(description + '\n')

print(f"✅ Unique descriptions have been saved to '{output_file}'")