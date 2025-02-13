import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Define Paths
base_path = os.path.dirname(__file__)  # Get current file path
data_path = os.path.join(base_path, "../data/cleaned_data.csv")
visuals_path = os.path.join(base_path, "../visuals")

# Ensure visuals directory exists
os.makedirs(visuals_path, exist_ok=True)

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

# Save preprocessed data
preprocessed_path = os.path.join(visuals_path, "data /pca_preprocessed_data.csv")
df_scaled.to_csv(preprocessed_path, index=False)
print(f"Preprocessed Data Saved: {preprocessed_path}")