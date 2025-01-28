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

# Define a broader set of ultra-processed food categories
ultra_processed_categories = [
    'Soda', 'Cookies & Biscuits', 'Ice Cream & Frozen Yogurt', 'Candy', 
    'Pizza', 'Chips, Pretzels & Snacks', 'Cakes & Pastries', 'Processed Meats',
    'Ready-to-Eat Meals', 'Packaged Desserts', 'Energy Bars', 'Breakfast Cereals'
]
df_ultra_processed = df[df['Category'].isin(ultra_processed_categories)]

# Group by category and sum up calories
category_calories = df_ultra_processed.groupby('Category')['Calories'].sum().sort_values(ascending=False)

# Calculate cumulative percentage
cumulative_percentage = category_calories.cumsum() / category_calories.sum() * 100

# Create a Pareto chart
plt.figure(figsize=(14, 10))

# Bar chart for calorie contributions
bars = plt.bar(
    category_calories.index,
    category_calories.values,
    color='skyblue',
    alpha=0.8,
    label='Calories Contribution'
)

# Line plot for cumulative percentage
line = plt.plot(
    category_calories.index,
    cumulative_percentage.values,
    color='darkred',
    marker='o',
    linestyle='-',
    label='Cumulative Percentage'
)

# Highlight the 80% threshold
plt.axhline(80, color='darkblue', linestyle='--', label='80% Threshold')

# Add labels to bars for calorie values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height,
        f'{int(height)}',
        ha='center',
        va='bottom',
        fontsize=10
    )

# Title, labels, and legend
plt.title("Pareto Chart: Calorie Contribution by Ultra-Processed Categories", fontsize=18, weight='bold')
plt.xlabel("Category", fontsize=14)
plt.ylabel("Total Calories", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper left', fontsize=12)

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the chart
pareto_chart_path = os.path.join(visuals_path, "enhanced_pareto_chart_ultra_processed.png")
plt.tight_layout()
plt.savefig(pareto_chart_path)
plt.close()

print(f"Enhanced Pareto chart saved at {pareto_chart_path}.")