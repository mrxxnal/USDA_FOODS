import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the visuals folder exists
os.makedirs("visuals", exist_ok=True)

# Load the dataset
data_path = "data/raw_data.csv"
df = pd.read_csv(data_path)

# Check for missing values and handle them (drop or fill)
df = df.dropna(subset=["Calories", "Protein", "Fat", "Carbs"])

# Distribution plots for numerical features
def plot_distribution(column, title, filename):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True, bins=30, color='skyblue')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"visuals/{filename}.png")
    plt.close()

plot_distribution("Calories", "Distribution of Calories", "calories_distribution")
plot_distribution("Protein", "Distribution of Protein", "protein_distribution")
plot_distribution("Fat", "Distribution of Fat", "fat_distribution")
plot_distribution("Carbs", "Distribution of Carbs", "carbs_distribution")

# Box plots for numerical features grouped by category
def plot_box(column, title, filename):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Category", y=column, data=df)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"visuals/{filename}.png")
    plt.close()

plot_box("Calories", "Calories by Category", "calories_by_category")
plot_box("Protein", "Protein by Category", "protein_by_category")
plot_box("Fat", "Fat by Category", "fat_by_category")
plot_box("Carbs", "Carbs by Category", "carbs_by_category")

# Count plot for categories
plt.figure(figsize=(12, 6))
sns.countplot(y="Category", data=df, order=df["Category"].value_counts().index, palette="viridis")
plt.title("Count of Products by Category")
plt.xlabel("Count")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("visuals/category_count.png")
plt.close()

# Top brands by number of products
top_brands = df["Brand"].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_brands.values, y=top_brands.index, palette="muted")
plt.title("Top 10 Brands by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig("visuals/top_brands.png")
plt.close()

# Pairplot to explore relationships between numerical features
sns.pairplot(df[["Calories", "Protein", "Fat", "Carbs"]], diag_kind="kde")
plt.tight_layout()
plt.savefig("visuals/pairplot_numerical.png")
plt.close()

print("Visualizations saved to the 'visuals/' folder.")