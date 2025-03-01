# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mpl_toolkits.mplot3d import Axes3D

# Define paths
file_path = "data/pca_3D.csv"
visuals_path = "visuals/"
os.makedirs(visuals_path, exist_ok=True)  # Ensure visuals folder exists

# Load PCA reduced dataset
df_pca = pd.read_csv(file_path)

# Determine best k using Silhouette Score
sil_scores = {}
for k in range(2, 8):  # Test k values from 2 to 7
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(df_pca)
    sil_score = silhouette_score(df_pca, cluster_labels)
    sil_scores[k] = sil_score

# Select the top 3 best k values based on silhouette score
best_k_values = sorted(sil_scores, key=sil_scores.get, reverse=True)[:3]
print(f"Best K values based on silhouette scores: {best_k_values}")

# Plot silhouette scores and save the figure
plt.figure(figsize=(8, 5))
plt.plot(sil_scores.keys(), sil_scores.values(), marker='o', linestyle='--')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score vs Number of Clusters")
plt.grid()
silhouette_plot_path = os.path.join(visuals_path, "KMeans_Silhouette_Scores.png")
plt.savefig(silhouette_plot_path, dpi=300, bbox_inches="tight")
plt.show()

print(f"✅ Silhouette Score plot saved at: {silhouette_plot_path}")

# Run K-Means for the best 3 k-values and visualize
fig = plt.figure(figsize=(18, 6))

for i, k in enumerate(best_k_values, 1):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df_pca[f'Cluster_k{k}'] = kmeans.fit_predict(df_pca)

    ax = fig.add_subplot(1, 3, i, projection='3d')
    ax.scatter(df_pca['PC1'], df_pca['PC2'], df_pca['PC3'], c=df_pca[f'Cluster_k{k}'], cmap='viridis')
    ax.set_title(f"K-Means Clustering (k={k})")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")

# Save the 3D clustering visualization
kmeans_plot_path = os.path.join(visuals_path, "KMeans_Clusters_3D.png")
plt.savefig(kmeans_plot_path, dpi=300, bbox_inches="tight")
plt.show()

print(f"✅ K-Means 3D Clusters plot saved at: {kmeans_plot_path}")

# Save clustered data for later comparison
df_pca.to_csv("data/kmeans_clusters.csv", index=False)
print("\n✅ K-Means Clustering Completed and Saved.")