import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# 🔹 Define Paths
base_path = os.path.dirname(__file__)  # Get current script location
data_path = os.path.join(base_path, "data/pca_preprocessed_data.csv")  # Ensure correct path

# 🔹 Load the preprocessed dataset
df_scaled = pd.read_csv(data_path)

# 🔹 Perform PCA on the full dataset (ALL components)
full_pca = PCA()
full_pca.fit(df_scaled)

# 🔹 Calculate cumulative explained variance
cumulative_variance = np.cumsum(full_pca.explained_variance_ratio_) * 100

# 🔹 Find the number of components needed to reach 95% variance
num_components_95 = np.argmax(cumulative_variance >= 95) + 1  # +1 because Python is 0-indexed

# 🔹 Plot the cumulative explained variance
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--', color='b')
plt.axhline(y=95, color='r', linestyle='-', label="95% Variance Threshold")  # Horizontal line at 95%
plt.axvline(x=num_components_95, color='g', linestyle='--', label=f"Components Needed: {num_components_95}")  # Vertical line at threshold
plt.xlabel("Number of Principal Components", fontsize=12)
plt.ylabel("Cumulative Variance Explained (%)", fontsize=12)
plt.title("PCA: Number of Components Needed for 95% Variance Retention", fontsize=14)
plt.legend()
plt.grid()

# 🔹 Save the Variance Plot
variance_plot_path = os.path.join(base_path, "visuals/PCA_Variance_Analysis.png")
plt.savefig(variance_plot_path, dpi=300, bbox_inches="tight")
plt.show()

# 🔹 Display results
print(f"\n✅ To retain at least 95% variance, we need **{num_components_95}** principal components.")

# 🔹 Get Top 3 Eigenvalues (largest variance contributions)
top_3_eigenvalues = full_pca.explained_variance_[:3]
print("\n🔹 Top 3 Eigenvalues (Variance Contributions):")
print(top_3_eigenvalues)

# 🔹 Save results to a text file for reference
results_path = os.path.join(base_path, "visuals/PCA_Variance_Results.txt")
with open(results_path, "w") as file:
    file.write(f"Number of Components for 95% Variance: {num_components_95}\n")
    file.write(f"Top 3 Eigenvalues: {top_3_eigenvalues}\n")

print(f"\n✅ Variance results saved at: {results_path}")
print(f"✅ Variance plot saved at: {variance_plot_path}")