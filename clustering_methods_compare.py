# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Define paths
file_path = "data/pca_3D.csv"
visuals_path = "visuals/"
os.makedirs(visuals_path, exist_ok=True)  # Ensure visuals folder exists

# Load PCA reduced dataset
df_pca = pd.read_csv(file_path)

# Initialize dictionary to store silhouette scores
silhouette_scores = {}

# K-Means Clustering Performance
best_k = 5  # Use the best k from previous analysis
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(df_pca)
silhouette_scores["K-Means"] = silhouette_score(df_pca, kmeans_labels)

# Hierarchical Clustering Performance
hierarchical = AgglomerativeClustering(n_clusters=best_k)
hierarchical_labels = hierarchical.fit_predict(df_pca)
silhouette_scores["Hierarchical"] = silhouette_score(df_pca, hierarchical_labels)

# DBSCAN Clustering Performance
dbscan = DBSCAN(eps=1.2, min_samples=5)  # Adjust parameters as needed
dbscan_labels = dbscan.fit_predict(df_pca)

# Only compute Silhouette Score if DBSCAN formed clusters
if len(set(dbscan_labels)) > 1:  # DBSCAN may classify everything as noise (-1)
    silhouette_scores["DBSCAN"] = silhouette_score(df_pca, dbscan_labels)
else:
    silhouette_scores["DBSCAN"] = -1  # Indicate failure to form clusters

# Find the best-performing clustering method
best_method = max(silhouette_scores, key=silhouette_scores.get)
best_score = silhouette_scores[best_method]

# Plot the performance comparison
plt.figure(figsize=(8, 5))
plt.bar(silhouette_scores.keys(), silhouette_scores.values(), color=['blue', 'green', 'red'])
plt.xlabel("Clustering Method")
plt.ylabel("Silhouette Score")
plt.title("Comparison of Clustering Methods")
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--')

# Annotate the best method
plt.text(best_method, best_score + 0.02, f"Best: {best_method}", fontsize=12, ha='center', fontweight='bold')

# Save the visualization
performance_plot_path = os.path.join(visuals_path, "clustering_performance_comparison.png")
plt.savefig(performance_plot_path, dpi=300, bbox_inches="tight")
plt.show()

print(f"✅ Clustering Performance Comparison saved at: {performance_plot_path}")

# Save the results in a text file for reference
results_path = os.path.join(visuals_path, "clustering_results.txt")
with open(results_path, "w") as f:
    for method, score in silhouette_scores.items():
        f.write(f"{method}: Silhouette Score = {score:.3f}\n")
    f.write(f"\nBest Performing Method: {best_method} with a score of {best_score:.3f}")

print(f"✅ Clustering results saved at: {results_path}")