import pandas as pd
import matplotlib.pyplot as plt
import os

# Base path
base_path = os.getcwd()

# Paths
data_path = "/Users/mrunal/USDA_FOOD/data/cleaned_data.csv"  # Full path to your CSV file
visuals_path = os.path.join(base_path, "visuals")

# Ensure visuals folder exists
os.makedirs(visuals_path, exist_ok=True)

# Load dataset
try:
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The dataset file was not found at {data_path}. Please check the path.")
    exit()

# Define a mapping for broader categories
category_mapping = {
    'Soda': 'Ultra-Processed - Beverages',
    'Cookies & Biscuits': 'Ultra-Processed - Snacks',
    'Ice Cream & Frozen Yogurt': 'Ultra-Processed - Desserts',
    'Candy': 'Ultra-Processed - Snacks',
    'Pizza': 'Ultra-Processed - Fast Food',
    'Chips, Pretzels & Snacks': 'Ultra-Processed - Snacks',
    # Add more mappings as needed
}

# Map categories to broader groups
df['Broad_Category'] = df['Category'].map(category_mapping)

# Filter for ultra-processed foods
ultra_processed = df[df['Broad_Category'].notna()]

# Count occurrences of each category
category_counts = ultra_processed['Category'].value_counts()

# Keep the top 15-20 categories and group the rest into "Others"
num_categories_to_show = 20
other_count = category_counts[num_categories_to_show:].sum()
category_counts = category_counts[:num_categories_to_show]
category_counts['Others'] = other_count

# Plot: Donut Chart
plt.figure(figsize=(10, 8))
colors = plt.cm.Paired(range(len(category_counts)))  # Use a colormap for distinct colors
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}  # Add white edges for better visibility
)
# Add a circle at the center to transform it into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

plt.title("Distribution of Categories in Ultra-Processed Foods", fontsize=16, weight='bold')
plt.tight_layout()

# Save the plot directly
donut_chart_path = os.path.join(visuals_path, "ultra_processed_categories_donut_chart.png")
plt.savefig(donut_chart_path)
plt.close()

print(f"Visualization saved at {donut_chart_path}.")
