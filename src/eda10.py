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

# Filter for relevant brands
top_brands = df['Brand'].value_counts().head(15).index
filtered_df = df[df['Brand'].isin(top_brands)]

# Convert necessary columns to numeric
filtered_df['Calories'] = pd.to_numeric(filtered_df['Calories'], errors='coerce')
filtered_df['Calories_per_Fat'] = pd.to_numeric(filtered_df['Calories_per_Fat'], errors='coerce')
filtered_df['Carbs'] = pd.to_numeric(filtered_df['Carbs'], errors='coerce')

# Prepare data for the bubble chart
bubble_data = filtered_df.groupby('Brand').agg({
    'Calories': 'mean',
    'Calories_per_Fat': 'mean',
    'Carbs': 'mean'
}).reset_index()

# Plot: Enhanced Bubble Chart with larger bubble sizes
plt.figure(figsize=(16, 10))
bubble_sizes = bubble_data['Carbs'] * 40  # Increase the scaling factor

scatter = plt.scatter(
    bubble_data['Calories'],
    bubble_data['Calories_per_Fat'],
    s=bubble_sizes,
    alpha=0.7,
    c=range(len(bubble_data)),
    cmap='plasma',
    edgecolors="black",
    linewidth=0.7
)

# Add brand names to the plot
for i, row in bubble_data.iterrows():
    plt.text(row['Calories'], row['Calories_per_Fat'], row['Brand'], fontsize=9, ha='right')

# Add grid and labels
plt.title("Brand Contribution: Calories vs. Nutrient Ratios", fontsize=20, weight='bold')
plt.xlabel("Average Calories", fontsize=14)
plt.ylabel("Average Calories per Fat", fontsize=14)
plt.grid(color="gray", linestyle="--", linewidth=0.5)

# Add color bar
cbar = plt.colorbar(scatter, aspect=40, pad=0.02)
cbar.set_label('Brand Index', rotation=270, labelpad=20, fontsize=12)

# Save the plot
bubble_chart_path = os.path.join(visuals_path, "enhanced_brand_contribution_bubble_chart_larger_bubbles.png")
plt.tight_layout()
plt.savefig(bubble_chart_path)
plt.close()

print(f"Enhanced bubble chart with larger bubbles saved at {bubble_chart_path}.")