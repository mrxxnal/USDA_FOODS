import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Base path
base_path = os.getcwd()

# Paths
data_path = os.path.join(base_path, "../data/cleaned_data.csv")
visuals_path = os.path.join(base_path, "../visuals")

# Ensure visuals folder exists
os.makedirs(visuals_path, exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Filter beverages
beverages = df[df["Category"].str.contains("Soda|Beverages", na=False, case=False)]

# Plot: Swarm Plot
plt.figure(figsize=(14, 8))
sns.swarmplot(
    data=beverages,
    x="Brand",
    y="Calories_per_Carb",
    hue="Calories_Bin",
    palette="viridis",
    dodge=True
)
plt.title("Sugar Content in Beverages by Brand", fontsize=16, weight='bold')
plt.xlabel("Brand", fontsize=12)
plt.ylabel("Calories per Carbohydrate (kcal)", fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.legend(title="Calories Bin", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
swarmplot_path = os.path.join(visuals_path, "swarmplot_sugar_content_by_brand.png")
plt.savefig(swarmplot_path)
plt.show()