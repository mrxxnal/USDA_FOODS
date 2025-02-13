import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Define Paths
base_path = os.path.dirname(__file__)  # Get current file path
data_path = "/Users/mrunal/USDA_FOOD/data/cleaned_data.csv"
data_folder = os.path.join(base_path, "data")  # Target 'data' folder

# Ensure data directory exists
os.makedirs(data_folder, exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Drop categorical columns (Keep only numerical features)
df_numeric = df.select_dtypes(include=[np.number])

# Handle missing values (drop rows with NaN)
df_numeric.dropna(inplace=True)

# Standardize Data (Mean=0, Variance=1)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

# Convert back to DataFrame
df_scaled = pd.DataFrame(df_scaled, columns=df_numeric.columns)

# Save preprocessed data inside "data" folder
preprocessed_path = os.path.join(data_folder, "pca_preprocessed_data.csv")
df_scaled.to_csv(preprocessed_path, index=False)

print(f"✅ Preprocessed Data Saved: {preprocessed_path}")