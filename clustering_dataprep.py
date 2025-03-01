# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# Load the normalized dataset
file_path = "data/clean_normalized_data.csv"  # Adjust path if needed
df = pd.read_csv(file_path)

# Display first few rows to check structure
print("Initial Data Preview:")
print(df.head())

# Separate labels (for later comparison)
labels = df[['category']]  # Keeping category as ground truth
df_numeric = df.drop(columns=['description', 'category', 'brand'])  # Remove categorical columns

# Ensure all remaining columns are numerical
assert df_numeric.select_dtypes(include=[np.number]).shape[1] == df_numeric.shape[1], "Dataset contains non-numeric columns!"

# OPTIONAL: Apply PCA to reduce to 3D
pca = PCA(n_components=3)
df_pca = pca.fit_transform(df_numeric)

# Convert PCA output to DataFrame
df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2', 'PC3'])

# Compute variance retained
variance_retained = np.sum(pca.explained_variance_ratio_) * 100

# Save numeric dataset without categorical columns
df_numeric.to_csv("data/clustering_data.csv", index=False)
labels.to_csv("data/original_labels.csv", index=False)

# Display results
print("\n✅ Data Preparation Completed.")
print(f"✅ Quantitative dataset saved as clustering_data.csv (Only numerical features).")
print(f"✅ Labels saved as original_labels.csv for later comparison.")
print(f"✅ PCA-reduced dataset (3D) saved as pca_3D.csv with {variance_retained:.2f}% variance retained.")