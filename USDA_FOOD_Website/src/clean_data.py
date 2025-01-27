import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# Define file paths
raw_data_path = "data/raw_data.csv"
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
print("Initial dataset preview:")
print(df.head())
print(df.info())

# Step 1: Handle Missing Values
print("\nHandling missing values...")
missing_values_summary = df.isnull().sum()
print("Missing values summary before handling:\n", missing_values_summary)

# Fill missing values with default values
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

# Verify missing values have been handled
print("\nMissing values summary after handling:\n", df.isnull().sum())

# Step 2: Remove Duplicate Rows
print("\nChecking for duplicate rows...")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")
if duplicate_count > 0:
    print("Removing duplicate rows...")
    df = df.drop_duplicates()
    print(f"After removing duplicates: {df.shape}")

# Step 3: Identify and Handle Outliers
print("\nIdentifying and handling outliers...")
numerical_cols = ['Calories', 'Protein', 'Fat', 'Carbs']

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers_count = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
    print(f"{col}: Found {outliers_count} outliers.")

    # Remove outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(f"After removing outliers in {col}: {df.shape}")

# Step 4: Remove Unnecessary Columns
if 'Unnamed: 0' in df.columns:
    print("\nRemoving unnecessary columns...")
    df = df.drop(columns=['Unnamed: 0'])
    print("Unnecessary columns removed.")

# Step 5: Feature Generation
print("\nGenerating additional features...")
df['Calories_per_Protein'] = df['Calories'] / (df['Protein'] + 1e-5)  # Avoid division by zero
df['Calories_per_Fat'] = df['Calories'] / (df['Fat'] + 1e-5)  # Avoid division by zero
df['Calories_per_Carb'] = df['Calories'] / (df['Carbs'] + 1e-5)  # Avoid division by zero
print("New features generated successfully.")

# Step 6: Normalize Data
print("\nNormalizing data using StandardScaler...")
scaler = StandardScaler()
scaled_cols = ['Calories', 'Protein', 'Fat', 'Carbs']
df[scaled_cols] = scaler.fit_transform(df[scaled_cols])
print("Data normalized successfully.")

# Step 7: Discretization (Binning)
print("\nPerforming discretization (binning)...")
df['Calories_Bin'] = pd.qcut(df['Calories'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
print("Discretization completed successfully.")

# Save the cleaned dataset
print(f"\nSaving cleaned data to {cleaned_data_path}...")
df.to_csv(cleaned_data_path, index=False)
print(f"Cleaned data saved successfully. Final dataset size: {df.shape}")

# Summary of the cleaned dataset
print("\nCleaned Dataset Preview:")
print(df.head())
print("\nColumns in the cleaned dataset:")
print(df.columns.tolist())