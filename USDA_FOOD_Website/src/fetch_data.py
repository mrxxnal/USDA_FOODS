import pandas as pd
import os

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# Define file paths
raw_data_path = "data/raw_data.csv"  # Corrected file path for raw_data.csv
cleaned_data_path = "data/cleaned_data.csv"

# Load the dataset
try:
    print("Loading raw data...")
    df = pd.read_csv(raw_data_path)
    print("Raw data loaded successfully.")
except FileNotFoundError:
    print(f"Error: {raw_data_path} file not found. Please ensure the file is in the 'data' directory.")
    exit()

# Display initial dataset information
print(f"Initial dataset size: {df.shape}")

# Handle missing values
print("Handling missing values...")
default_values = {
    'Calories': 0,
    'Protein': 0,
    'Fat': 0,
    'Carbs': 0,
    'Brand': 'Unknown',
    'Category': 'Uncategorized',
    'Description': 'No Description'
}
df.fillna(default_values, inplace=True)

# Check for duplicates
print("\nChecking for duplicate rows...")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")
if duplicate_count > 0:
    print("Removing duplicate rows...")
    df = df.drop_duplicates()
    print(f"After removing duplicates: {df.shape}")

# Identify and handle outliers using the IQR method
print("\nIdentifying and handling outliers...")
numerical_cols = ['Calories', 'Protein', 'Fat', 'Carbs']
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Remove outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
print(f"After removing outliers: {df.shape}")

# Remove unnecessary columns (e.g., row indices)
print("Checking for unnecessary columns...")
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
    print("\nRemoved unnecessary columns.")

# Save the cleaned dataset
print(f"Saving cleaned data to {cleaned_data_path}...")
df.to_csv(cleaned_data_path, index=False)
print(f"Cleaned data saved successfully. Final dataset size: {df.shape}")