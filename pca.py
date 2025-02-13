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

# Plot 2D PCA
# Plot 2D PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_pca_2D["PC1"], y=df_pca_2D["PC2"], alpha=0.7, color="teal")
plt.xlabel("Calories & Macronutrient Contribution")
plt.ylabel("Macronutrient Ratios & Distribution")
plt.title(f"PCA 2D Projection ({explained_variance_2D:.2f}% Variance Retained)")
plt.grid(True)
pca_2D_plot_path = os.path.join(base_path, "visuals", "PCA_2D_plot.png")
plt.savefig(pca_2D_plot_path)
plt.show()

# Save 2D plot
pca_2D_plot_path = os.path.join(visuals_folder, "PCA_2D_plot.png")
plt.savefig(pca_2D_plot_path)
plt.show()

# Plot 3D PCA
import plotly.express as px
import matplotlib.pyplot as plt

# 🔹 Interactive 3D PCA Plot using Plotly (Better UI)
fig = px.scatter_3d(
    df_pca_3D, 
    x="PC1", 
    y="PC2", 
    z="PC3", 
    opacity=0.7, 
    color_discrete_sequence=["blue"]
)
fig.update_layout(
    title=f"PCA 3D Projection ({explained_variance_3D:.2f}% Variance Retained)",
    scene=dict(
        xaxis_title="Calories & Macronutrient Contribution",
        yaxis_title="Macronutrient Ratios & Distribution",
        zaxis_title="Carbohydrate & Fat Energy Balance"
    )
)
fig.show()

# 🔹 Static 3D PCA Plot using Matplotlib (Full Dataset)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Scatter plot with **full dataset**
ax.scatter(
    df_pca_3D["PC1"], df_pca_3D["PC2"], df_pca_3D["PC3"], 
    alpha=0.6, s=5, color="navy"
)

# 🔹 Proper Axis Labels Based on PCA Loadings
ax.set_xlabel("Calories & Macronutrient Contribution", fontsize=12)
ax.set_ylabel("Macronutrient Ratios & Distribution", fontsize=12)
ax.set_zlabel("Carbohydrate & Fat Energy Balance", fontsize=12)
ax.set_title(f"PCA 3D Projection ({explained_variance_3D:.2f}% Variance Retained)", fontsize=14)

# Save the 3D plot properly
pca_3D_plot_path = os.path.join(visuals_folder, "PCA_3D_plot.png")
plt.savefig(pca_3D_plot_path, dpi=300, bbox_inches="tight")

# Display the final plot
plt.show()