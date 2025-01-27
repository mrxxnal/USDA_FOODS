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

# Grouping categories into broader groups
category_mapping = {
    'Soda': 'Ultra-Processed',
    'Cookies & Biscuits': 'Ultra-Processed',
    'Ice Cream & Frozen Yogurt': 'Ultra-Processed',
    'Candy': 'Ultra-Processed',
    'Breads & Buns': 'Ultra-Processed',
    'Pizza': 'Ultra-Processed',
    'Frozen Patties and Burgers': 'Ultra-Processed',
    'Chips, Pretzels & Snacks': 'Ultra-Processed',
    'Other Snacks': 'Ultra-Processed',
    'Chocolate': 'Ultra-Processed',
    'Cakes, Cupcakes, Snack Cakes': 'Ultra-Processed',
    'French Fries, Potatoes & Onion Rings': 'Ultra-Processed',
    'Popcorn, Peanuts, Seeds & Related Snacks': 'Ultra-Processed',
    # Add more categories here for Ultra-Processed
    'Wholesome Snacks': 'Minimally Processed',
    'Prepared Pasta & Pizza Sauces': 'Minimally Processed',
    'Pickles, Olives, Peppers & Relishes': 'Minimally Processed',
    'Fresh Fruits & Vegetables': 'Minimally Processed',
    'Grains & Beans': 'Minimally Processed',
    'Nuts & Seeds': 'Minimally Processed',
    'Dairy Products': 'Minimally Processed',
    'Fish & Seafood': 'Minimally Processed',
    # Add more categories here for Minimally Processed
}

# Map the categories to broader groups
df['Broad_Category'] = df['Category'].map(category_mapping)

# Check if there are unmapped categories
unmapped_categories = df[df['Broad_Category'].isnull()]['Category'].unique()
if len(unmapped_categories) > 0:
    print(f"Warning: Unmapped categories found: {unmapped_categories}")

# Drop rows with unmapped categories
df = df.dropna(subset=['Broad_Category'])

# Proportion of Broad Categories
broad_category_counts = df['Broad_Category'].value_counts()

# Creating the pie chart
fig, ax = plt.subplots(figsize=(8, 6))
broad_category_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['#6C3483', '#2874A6', '#229954'],  # Professional color scheme
    legend=False,
    ax=ax
)
ax.set_title("Proportion of Ultra vs Healthy Foods Consumed in General")
ax.set_ylabel("")

# Adding a detailed legend
ax.legend(
    [
        "Ultra-Processed - Snacks, Chips, Soda, Candy",
        "Minimally Processed - Vegetables, Dairy, Fish, Natural Produce",
        "Healthy Foods - Fruits, Vegetables, Nuts"
    ],
    loc='center left',
    bbox_to_anchor=(1.2, 0.5),
    title="Category Examples"
)

# Save the visualization
plt.savefig(os.path.join(visuals_path, "proportion_processed_foods_grouped.png"), bbox_inches="tight")
plt.close()

print("\nEDA Completed. Visualizations saved in the 'visuals' folder.")