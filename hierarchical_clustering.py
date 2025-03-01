# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from mpl_toolkits.mplot3d import Axes3D
import os

# Ensure the visuals folder exists
visuals_folder = "visuals"
os.makedirs(visuals_folder, exist_ok=True)

# Load the PCA reduced dataset (3D Data)
file_path = "data/pca_3D.csv"
df_pca = pd.read_csv(file_path)

# Perform hierarchical clustering
linkage_matrix = linkage(df_pca, method='ward')  # Ward's method minimizes variance

# Plot the dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix, truncate_mode="level", p=5)  # Truncate for better visualization
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Cluster Distance")
plt.grid()

# Save the dendrogram
dendrogram_path = os.path.join(visuals_folder, "hierarchical_dendrogram.png")
plt.savefig(dendrogram_path, dpi=300, bbox_inches="tight")
plt.show()

# Determine clusters using a cutoff distance
num_clusters = 5  # Manually chosen, can be adjusted
cluster_labels = fcluster(linkage_matrix, num_clusters, criterion='maxclust')

# Assign clusters to the dataset
df_pca['Cluster_HC'] = cluster_labels

# 3D Scatter Plot of Hierarchical Clusters
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df_pca['PC1'], df_pca['PC2'], df_pca['PC3'], c=df_pca['Cluster_HC'], cmap='viridis')
ax.set_title("Hierarchical Clustering (3D Visualization)")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

# Save the 3D visualization
hc_visualization_path = os.path.join(visuals_folder, "hierarchical_clustering.png")
plt.savefig(hc_visualization_path, dpi=300, bbox_inches="tight")
plt.show()

# Save clustered data for further analysis
hc_clustered_data_path = "data/hierarchical_clusters.csv"
df_pca.to_csv(hc_clustered_data_path, index=False)

# Print completion message
print(f"\n✅ Hierarchical Clustering Completed and Saved.")
print(f"✅ Dendrogram saved at: {dendrogram_path}")
print(f"✅ 3D Cluster Visualization saved at: {hc_visualization_path}")
print(f"✅ Clustered data saved at: {hc_clustered_data_path}")