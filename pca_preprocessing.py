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
visuals_folder = os.path.join(base_path, "visuals")  # Folder for visualizations

# Ensure directories exist
os.makedirs(data_folder, exist_ok=True)
os.makedirs(visuals_folder, exist_ok=True)

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
print(f" Preprocessed Data Saved: {preprocessed_path}")

# Apply PCA with 2 components
pca_2D = PCA(n_components=2)
df_pca_2D = pca_2D.fit_transform(df_scaled)

# Apply PCA with 3 components
pca_3D = PCA(n_components=3)
df_pca_3D = pca_3D.fit_transform(df_scaled)

# Convert to DataFrame
df_pca_2D = pd.DataFrame(df_pca_2D, columns=['PC1', 'PC2'])
df_pca_3D = pd.DataFrame(df_pca_3D, columns=['PC1', 'PC2', 'PC3'])

# Save PCA-transformed datasets inside "data" folder
pca_2D_path = os.path.join(data_folder, "pca_2D.csv")
pca_3D_path = os.path.join(data_folder, "pca_3D.csv")

df_pca_2D.to_csv(pca_2D_path, index=False)
df_pca_3D.to_csv(pca_3D_path, index=False)

print(f" PCA 2D Data Saved: {pca_2D_path}")
print(f" PCA 3D Data Saved: {pca_3D_path}")

# Explained variance for both models
explained_variance_2D = np.sum(pca_2D.explained_variance_ratio_) * 100
explained_variance_3D = np.sum(pca_3D.explained_variance_ratio_) * 100

print(f" Variance retained in 2D PCA: {explained_variance_2D:.2f}%")
print(f" Variance retained in 3D PCA: {explained_variance_3D:.2f}%")

# Compute PCA loadings
loadings = pd.DataFrame(pca_3D.components_, columns=df_numeric.columns, index=['PC1', 'PC2', 'PC3'])

# Display loadings
print("\n🔹 PCA Loadings (Feature Contributions):")
print(loadings.T)