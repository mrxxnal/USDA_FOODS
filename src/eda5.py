import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Base path
base_path = os.path.dirname(__file__)

# Paths
data_path = os.path.join(base_path, "../data/cleaned_data.csv")
visuals_path = os.path.join(base_path, "../visuals")

# Ensure visuals folder exists
os.makedirs(visuals_path, exist_ok=True)

# Load dataset
try:
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The dataset file was not found. Please check the path.")
    exit()

# Check for required columns
required_columns = ['Brand', 'Calories', 'Calories_Bin']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Error: Missing required columns: {missing_columns}")
    exit()

# Remove specific brands if needed
brands_to_exclude = ["Kyo Footwear", "Kyo Footwear L.P."]
df = df[~df['Brand'].isin(brands_to_exclude)]

# Filter high-calorie products
high_calorie_bins = ['High', 'Very High']
df['High_Calorie'] = df['Calories_Bin'].isin(high_calorie_bins)

# Group by Brand and compute stats
brand_stats = df.groupby('Brand').agg(
    total_products=('Calories', 'count'),
    total_high_calorie=('High_Calorie', 'sum')
).reset_index()

# Calculate proportion of high-calorie products for each brand
brand_stats['proportion_high'] = brand_stats['total_high_calorie'] / brand_stats['total_products']

# Sort by proportion_high in descending order
brand_stats = brand_stats.sort_values(by='proportion_high', ascending=False)

# Limit to top 20 brands
top_brands = brand_stats.head(20)

# Normalize bubble sizes for better visualization
max_products = top_brands["total_products"].max()
top_brands["bubble_size"] = (top_brands["total_products"] / max_products) * 1000  # Scale sizes

# Create bubble chart
plt.figure(figsize=(16, 10))
scatter = plt.scatter(
    top_brands["proportion_high"],
    top_brands["Brand"],
    s=top_brands["bubble_size"],  # Bubble size represents the total number of products
    c=top_brands["proportion_high"],  # Color based on proportion
    cmap="coolwarm",
    alpha=0.8,
    edgecolors="black"
)

# Color bar
cbar = plt.colorbar(scatter)
cbar.set_label("Proportion of High-Calorie Products", fontsize=14)

# Labels & Formatting
plt.title("Proportion of High-Calorie Products by Brand (Top 20)", fontsize=18, weight='bold')
plt.xlabel("Proportion of High-Calorie Products", fontsize=14)
plt.ylabel("Brand", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Save the plot
plot_path = os.path.join(visuals_path, "top_20_brands_high_calorie_filtered.png")
plt.tight_layout()
plt.savefig(plot_path)
plt.close()
print(f"Visualization saved: {plot_path}")