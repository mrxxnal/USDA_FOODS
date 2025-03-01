# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
import os

# Ensure the visuals folder exists
visuals_folder = "visuals"
os.makedirs(visuals_folder, exist_ok=True)

# Load the PCA reduced dataset (3D Data)
file_path = "data/pca_3D.csv"
df_pca = pd.read_csv(file_path)

# Standardize the dataset before applying DBSCAN
scaler = StandardScaler()
df_pca_scaled = scaler.fit_transform(df_pca)

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=10)  # Adjust parameters as needed
cluster_labels = dbscan.fit_predict(df_pca_scaled)

# Add cluster labels to the dataset
df_pca['Cluster_DBSCAN'] = cluster_labels

# 3D Scatter Plot of DBSCAN Clusters
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df_pca['PC1'], df_pca['PC2'], df_pca['PC3'], c=df_pca['Cluster_DBSCAN'], cmap='plasma', alpha=0.8)
ax.set_title("DBSCAN Clustering (3D Visualization)")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

# Save the 3D visualization
dbscan_visualization_path = os.path.join(visuals_folder, "dbscan_clustering.png")
plt.savefig(dbscan_visualization_path, dpi=300, bbox_inches="tight")
plt.show()

# Save clustered data for further analysis
dbscan_clustered_data_path = "data/dbscan_clusters.csv"
df_pca.to_csv(dbscan_clustered_data_path, index=False)

# Print completion message
print(f"\n✅ DBSCAN Clustering Completed and Saved.")
print(f"✅ 3D Cluster Visualization saved at: {dbscan_visualization_path}")
print(f"✅ Clustered data saved at: {dbscan_clustered_data_path}")