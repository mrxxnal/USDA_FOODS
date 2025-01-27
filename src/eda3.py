import pandas as pd
import matplotlib.pyplot as plt
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

# Basic Dataset Info
print("Dataset Info:")
print(df.info())

# Check for required nutrient columns
nutrient_columns = ['Calories', 'Protein', 'Fat', 'Carbs']
missing_columns = [col for col in nutrient_columns if col not in df.columns]

if missing_columns:
    print(f"Error: Missing required columns: {missing_columns}")
    exit()

# Convert nutrient columns to numeric and drop invalid or missing values
for col in nutrient_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=nutrient_columns)

# Group categories into broader groups
category_mapping = {
    'Soda': 'Ultra-Processed - Beverages',
    'Cookies & Biscuits': 'Ultra-Processed - Snacks',
    'Ice Cream & Frozen Yogurt': 'Ultra-Processed - Desserts',
    'Candy': 'Ultra-Processed - Snacks',
    'Breads & Buns': 'Minimally Processed - Bakery',
    'Pizza': 'Ultra-Processed - Fast Food',
    'Frozen Patties and Burgers': 'Ultra-Processed - Fast Food',
    'Chips, Pretzels & Snacks': 'Ultra-Processed - Snacks',
    'Other Snacks': 'Ultra-Processed - Snacks',
    'Chocolate': 'Ultra-Processed - Desserts',
    'Cakes, Cupcakes, Snack Cakes': 'Ultra-Processed - Bakery',
    'French Fries, Potatoes & Onion Rings': 'Ultra-Processed - Sides',
    'Fresh Fruits & Vegetables': 'Healthy - Produce',
    'Grains & Beans': 'Healthy - Grains & Legumes',
    'Nuts & Seeds': 'Healthy - Nuts & Seeds',
    'Dairy Products': 'Healthy - Dairy',
    'Fish & Seafood': 'Healthy - Protein',
    'Leafy Greens': 'Healthy - Produce',
    'Root Vegetables': 'Healthy - Produce',
    'Citrus Fruits': 'Healthy - Produce',
    'Berries': 'Healthy - Produce',
    'Tropical Fruits': 'Healthy - Produce',
    'Other': 'Other'
}

df['Broad_Category'] = df['Category'].map(category_mapping).fillna('Other')

# Aggregate nutrients by broad categories
aggregated_data = df.groupby('Broad_Category')[nutrient_columns].mean()

# Normalize data for the radar chart
normalized_means = (aggregated_data - aggregated_data.min()) / (aggregated_data.max() - aggregated_data.min())
categories = normalized_means.columns.tolist()

# Plotting the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'polar': True})
for i, row in normalized_means.iterrows():
    ax.plot(range(len(categories)), row, label=i, linewidth=1.5)
    ax.fill(range(len(categories)), row, alpha=0.2)
ax.set_title("Nutrient Comparison by Food Category (Broad Groups)", fontsize=16, weight='bold')
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, fontsize=12)

# Modify legend with examples
legend_labels = normalized_means.index.tolist()
legend_labels = [label if label != 'Other' else 'Other (e.g., Sauces, Soup)' for label in legend_labels]

ax.legend(
    legend_labels,
    loc="upper right",
    bbox_to_anchor=(1.3, 1.1),
    title="Broad Categories (with examples)",
    fontsize=10
)
plt.tight_layout()

# Save the chart
plt.savefig(os.path.join(visuals_path, "nutrient_radar_chart_grouped.png"))
plt.close()
print("Visualization saved: nutrient_radar_chart_grouped.png")

print("\nEDA Completed. Visualizations saved in the 'visuals' folder.")