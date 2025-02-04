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

# Remove specific brands
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

# Remove brands that have only one product (to focus on significant brands)
brand_stats = brand_stats[brand_stats['total_products'] > 1]

# Sort by proportion_high and total_products for better visualization
brand_stats = brand_stats.sort_values(by=['proportion_high', 'total_products'], ascending=[False, False])

# Limit to top 20 brands for better readability
top_brands = brand_stats.head(20)

# Plotting
plt.figure(figsize=(16, 10))
ax = sns.barplot(
    data=top_brands,
    x='proportion_high',
    y='Brand',
    hue='total_products',  # Differentiating with number of products
    palette='coolwarm',
    dodge=False
)

# Add values to bars
for index, value in enumerate(top_brands['proportion_high']):
    ax.text(value + 0.02, index, f"{value:.2f}", color='black', ha="left", fontsize=12)

# Titles and labels
plt.title("Proportion of High-Calorie Products by Brand (Top 20)", fontsize=20, weight='bold')
plt.xlabel("Proportion of High-Calorie Products", fontsize=14)
plt.ylabel("Brand", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Save the plot
plot_path = os.path.join(visuals_path, "top_20_brands_high_calorie_filtered.png")
plt.tight_layout()
plt.savefig(plot_path)
plt.close()
print(f"Visualization saved: {plot_path}")