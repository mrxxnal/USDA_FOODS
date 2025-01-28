import pandas as pd
import matplotlib.pyplot as plt
import os

# Base path
base_path = os.getcwd()

# Paths
data_path = "/Users/mrunal/USDA_FOOD/data/cleaned_data.csv"  # Full path to your CSV file
visuals_path = os.path.join(base_path, "visuals")

# Load dataset
try:
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The dataset file was not found at {data_path}. Please check the path.")
    exit()

# Filter for beverages
beverages = df[df["Category"].str.contains("Soda|Beverages", na=False, case=False)]

# Calculate average Calories_per_Carb for each brand
brand_avg = (
    beverages.groupby("Brand", as_index=False)["Calories_per_Carb"]
    .mean()
    .sort_values(by="Calories_per_Carb", ascending=False)
)

# Select the top 10 brands for visualization
top_brands = brand_avg.head(10)

# Plot: Vertical Bar Chart
plt.figure(figsize=(12, 8))
plt.barh(top_brands["Brand"], top_brands["Calories_per_Carb"], color="teal")
plt.title("Top 10 Brands by Average Sugar Content in Beverages", fontsize=16, weight="bold")
plt.xlabel("Average Calories per Carbohydrate (kcal)", fontsize=12)
plt.ylabel("Brand", fontsize=12)
plt.gca().invert_yaxis()  # Invert the y-axis to show the highest value at the top
plt.tight_layout()

# Save the plot directly
bar_chart_path = os.path.join(visuals_path, "beverages_sugar_content_bar_chart.png")
plt.savefig(bar_chart_path)
plt.close()  # Close the plot to avoid displaying it

print("Visualization saved at {bar_chart_path}.")