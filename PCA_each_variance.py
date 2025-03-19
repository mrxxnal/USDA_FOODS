import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

print("✅ Script started...")  # Debugging check

# Load the dataset
file_path = "data/pca_preprocessed_data.csv"  # Adjust path if needed
try:
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully...")  # Debugging check
except Exception as e:
    print(f"❌ Error loading data: {e}")
    exit()

# Ensure dataset is not empty
if df.empty:
    print("❌ DataFrame is empty. Exiting script.")
    exit()
else:
    print(f"✅ Data has {df.shape[0]} rows and {df.shape[1]} columns.")

# Check for missing values
print("✅ Checking for missing values...")
missing_values = df.isnull().sum().sum()
if missing_values > 0:
    print(f"❌ Warning: Dataset contains {missing_values} missing values.")
else:
    print("✅ No missing values found.")

# Scale the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print("✅ Data scaled...")

# Apply PCA
pca = PCA()
pca.fit(df_scaled)

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print("✅ Explained variance ratio per component:")
for i, var in enumerate(explained_variance, 1):
    print(f"   - Principal Component {i}: {var:.4f} ({var * 100:.2f}%)")

# Plot variance explained by each component & cumulative variance
plt.figure(figsize=(10, 6))

# Individual variance bar chart
plt.bar(range(1, len(explained_variance) + 1), explained_variance, alpha=0.6, label="Individual Variance")

# Cumulative variance line plot
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--', color='r', label="Cumulative Variance")

# Labels and formatting
plt.xlabel('Number of Principal Components')
plt.ylabel('Explained Variance')
plt.title('Variance Explained by Principal Components')
plt.legend()
plt.grid()

# Save figure
plt.savefig("visuals/pca_variance_explained.png")
print("✅ Variance illustration saved in 'visuals/' folder.")

# Show plot
plt.show()

print("✅ Script execution completed.")