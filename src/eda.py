import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
data_path = "/data/cleaned_data.csv"
visuals_path = "/visuals"

# Ensure visuals folder exists
os.makedirs(visuals_path, exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Basic Dataset Info
print("Dataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
missing_values = df.isnull().sum()
print(f"\nMissing Values:\n{missing_values}")

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig(f"{visuals_path}/correlation_heatmap.png")
plt.close()

# Distribution of calories
plt.figure(figsize=(8, 5))
sns.histplot(df['Calories'], bins=30, kde=True, color="blue")
plt.title("Calories Distribution")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.savefig(f"{visuals_path}/calories_distribution.png")
plt.close()

# Distribution of protein
plt.figure(figsize=(8, 5))
sns.histplot(df['Protein'], bins=30, kde=True, color="green")
plt.title("Protein Distribution")
plt.xlabel("Protein")
plt.ylabel("Frequency")
plt.savefig(f"{visuals_path}/protein_distribution.png")
plt.close()

# Distribution of fat
plt.figure(figsize=(8, 5))
sns.histplot(df['Fat'], bins=30, kde=True, color="red")
plt.title("Fat Distribution")
plt.xlabel("Fat")
plt.ylabel("Frequency")
plt.savefig(f"{visuals_path}/fat_distribution.png")
plt.close()

# Distribution of carbohydrates
plt.figure(figsize=(8, 5))
sns.histplot(df['Carbs'], bins=30, kde=True, color="purple")
plt.title("Carbohydrates Distribution")
plt.xlabel("Carbs")
plt.ylabel("Frequency")
plt.savefig(f"{visuals_path}/carbs_distribution.png")
plt.close()

# Count plot of categories
if 'Category' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(y=df['Category'], order=df['Category'].value_counts().index, palette="viridis")
    plt.title("Category Count")
    plt.xlabel("Count")
    plt.ylabel("Category")
    plt.savefig(f"{visuals_path}/category_count.png")
    plt.close()

# Calories by category
if 'Category' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Category', y='Calories', data=df, palette="Set3")
    plt.xticks(rotation=45, ha="right")
    plt.title("Calories by Category")
    plt.savefig(f"{visuals_path}/calories_by_category.png")
    plt.close()

# Pairplot for numerical features
numerical_features = ['Calories', 'Protein', 'Fat', 'Carbs']
sns.pairplot(df[numerical_features])
plt.savefig(f"{visuals_path}/pairplot_numerical.png")
plt.close()

# Mean nutrient distribution by category
if 'Category' in df.columns:
    nutrient_means = df.groupby('Category')[['Calories', 'Protein', 'Fat', 'Carbs']].mean().reset_index()
    nutrient_means.set_index('Category', inplace=True)
    nutrient_means.plot(kind='bar', figsize=(12, 8), colormap='tab10')
    plt.title("Mean Nutrient Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Mean Value")
    plt.savefig(f"{visuals_path}/nutrient_distribution_by_category.png")
    plt.close()

# Nutrient distribution scatter plots
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Protein', y='Calories', data=df, hue='Category', palette="deep")
plt.title("Calories vs Protein")
plt.xlabel("Protein")
plt.ylabel("Calories")
plt.savefig(f"{visuals_path}/calories_vs_protein.png")
plt.close()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Carbs', y='Fat', data=df, hue='Category', palette="cool")
plt.title("Fat vs Carbohydrates")
plt.xlabel("Carbohydrates")
plt.ylabel("Fat")
plt.savefig(f"{visuals_path}/carbs_vs_fat.png")
plt.close()

# Insights and Conclusions
print("\nEDA Completed. Visualizations saved in the 'visuals' folder.")