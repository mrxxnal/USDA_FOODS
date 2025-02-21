import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# Load the raw data
raw_data_path = "data/raw_data.csv"
cleaned_data_path = "data/cleaned_data.csv"
clean_normalized_data_path = "data/clean_normalized_data.csv"

# Load the dataset
try:
    df = pd.read_csv(raw_data_path)
    print("✅ Raw data loaded successfully.")
except FileNotFoundError:
    print("❌ Error: raw_data.csv file not found. Please ensure the file is in the 'data' directory.")
    exit()

# Display initial info about the data
print(f"📊 Initial dataset size: {df.shape}")
print("Dataset preview:")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()
print(f"🧹 After removing duplicates: {df.shape}")

# Handle missing values
missing_values = df.isnull().sum()
print(f"🚦 Missing values before cleaning:\n{missing_values}")

# Replace missing values with suitable defaults or drop rows/columns
df['Calories'] = df['Calories'].fillna(0)  
df['Protein'] = df['Protein'].fillna(0)    
df['Fat'] = df['Fat'].fillna(0)            
df['Carbs'] = df['Carbs'].fillna(0)        
df['Brand'] = df['Brand'].fillna("Unknown")

# Drop rows with missing descriptions or categories as they are essential
df = df.dropna(subset=['Description', 'Category'])
print(f"🧮 After handling missing values: {df.shape}")

# Standardize column names (optional, for consistency)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Feature Engineering: Adding new calculated features
df['calories_per_protein'] = df['calories'] / (df['protein'] + 1e-5)
df['calories_per_fat'] = df['calories'] / (df['fat'] + 1e-5)
df['calories_per_carb'] = df['calories'] / (df['carbs'] + 1e-5)

# Save the cleaned data before normalization
df.to_csv(cleaned_data_path, index=False)
print(f"✅ Cleaned data saved to {cleaned_data_path}. Final dataset size: {df.shape}")

# Quick summary of the cleaned data
print("🧼 Cleaned dataset preview:")
print(df.head())

# Normalize all numerical features including newly engineered ones
numerical_columns = df.select_dtypes(include=[float, int]).columns
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save the fully cleaned and normalized data
df.to_csv(clean_normalized_data_path, index=False)
print(f"🎯 Preprocessed and normalized data saved at {clean_normalized_data_path}")