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

# Basic Dataset Info
print("Dataset Info:")
print(df.info())

# Check for required columns
required_columns = ['Calories', 'Protein', 'Category']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Error: Missing required columns: {missing_columns}")
    exit()

# Convert nutrient columns to numeric and drop invalid or missing values
for col in ['Calories', 'Protein']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=['Calories', 'Protein'])

# Simplified category grouping with "Other" removed
category_mapping = {
    'Soda': 'Ultra-Processed - Beverages',
    'Cookies & Biscuits': 'Ultra-Processed - Snacks',
    'Ice Cream & Frozen Yogurt': 'Ultra-Processed - Desserts',
    'Candy': 'Ultra-Processed - Snacks',
    'Breads & Buns': 'Minimally Processed - Bakery',
    'Pizza': 'Ultra-Processed - Fast Food',
    'Chips, Pretzels & Snacks': 'Ultra-Processed - Snacks',
    'Fresh Fruits & Vegetables': 'Healthy - Produce',
    'Grains & Beans': 'Healthy - Grains & Legumes',
    'Nuts & Seeds': 'Healthy - Nuts & Seeds',
    'Dairy Products': 'Minimally Processed - Dairy',
    'Fish & Seafood': 'Healthy - Protein',
    'Leafy Greens': 'Healthy - Produce',
    'Root Vegetables': 'Healthy - Produce',
    'Citrus Fruits': 'Healthy - Produce',
    'Berries': 'Healthy - Produce',
    'Tropical Fruits': 'Healthy - Produce',
    'Sauces': 'Minimally Processed - Condiments',
    'Soup': 'Minimally Processed - Prepared Meals',
}

# Map categories to broader groups
df['Broad_Category'] = df['Category'].map(category_mapping)

# Drop rows where categories are not mapped
df = df.dropna(subset=['Broad_Category'])

# Define color palettes for healthy, minimally processed, and ultra-processed categories
color_palette = {
    'Healthy - Produce': 'darkblue',
    'Healthy - Grains & Legumes': 'navy',
    'Healthy - Nuts & Seeds': 'mediumblue',
    'Healthy - Protein': 'royalblue',
    'Minimally Processed - Bakery': 'lightblue',
    'Minimally Processed - Dairy': 'skyblue',
    'Minimally Processed - Condiments': 'deepskyblue',
    'Minimally Processed - Prepared Meals': 'powderblue',
    'Ultra-Processed - Beverages': 'lightcoral',
    'Ultra-Processed - Snacks': 'indianred',
    'Ultra-Processed - Desserts': 'firebrick',
    'Ultra-Processed - Fast Food': 'darkred',
}

# Calories vs Protein (Scatter Plot)
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df,
    x='Protein',
    y='Calories',
    hue='Broad_Category',
    palette=color_palette,
    alpha=0.8,  # Adjust transparency for better visibility
    s=50  # Size of points
)
plt.title("Calories vs Protein by Food Category (Broad Groups)", fontsize=16, weight='bold')
plt.xlabel("Protein (grams)", fontsize=12)
plt.ylabel("Calories (kcal)", fontsize=12)
plt.legend(
    title="Broad Categories",
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    fontsize=10
)
plt.tight_layout()

# Save the scatter plot
plt.savefig(os.path.join(visuals_path, "calories_vs_protein_no_other.png"))
plt.close()
print("Visualization saved: calories_vs_protein_no_other.png")

print("\nEDA Completed. Visualizations saved in the 'visuals' folder.")