import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

# Calculate the average Carbs, Fat, and Protein
avg_nutrition = ultra_processed[["Carbs", "Fat", "Protein"]].mean()

# Prepare data for the radar chart
categories = avg_nutrition.index.tolist()
values = avg_nutrition.values.tolist()
values.append(values[0])  # Close the radar chart loop
angles = np.linspace(0, 2 * np.pi, len(categories) + 1, endpoint=True)

# Radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"polar": True})
ax.fill(angles, values, color="teal", alpha=0.25)
ax.plot(angles, values, color="teal", linewidth=2)
ax.set_yticks([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_title("Average Nutrition in Ultra-Processed Foods", fontsize=16, weight="bold")
ax.grid(color="gray", linestyle="--", linewidth=0.5)

# Save the chart
radar_chart_path = os.path.join(visuals_path, "ultra_processed_nutrition_radar_chart.png")
plt.savefig(radar_chart_path)
plt.close()

print(f"Radar chart saved at {radar_chart_path}.")