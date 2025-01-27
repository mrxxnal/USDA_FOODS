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

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# Check for missing values
missing_values = df.isnull().sum()
print(f"\nMissing Values:\n{missing_values}")

# Ensure required columns exist and are valid
required_columns = ['Category', 'Fat']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Error: Missing required columns: {missing_columns}")
    exit()

# Check if 'Category' column is categorical and 'Fat' column is numerical
try:
    df['Category'] = df['Category'].astype(str)  # Ensure 'Category' is a string
    df['Fat'] = pd.to_numeric(df['Fat'], errors='coerce')  # Convert 'Fat' to numeric
except Exception as e:
    print(f"Error converting columns: {e}")
    exit()

# Drop rows with missing or negative 'Fat' values
df = df[df['Fat'] >= 0].dropna(subset=['Fat'])

# Refined category mapping with more categories and tagging dairy as good fats
category_mapping = {
    # Good Fats
    "Nuts": "Natural Produce - Good Fats",
    "Seeds": "Natural Produce - Good Fats",
    "Avocado": "Natural Produce - Good Fats",
    "Olive Oil": "Condiments - Good Fats",
    "Fish": "Protein - Good Fats",
    "Coconut": "Natural Produce - Good Fats",
    "Milk": "Dairy - Good Fats",
    "Cheese": "Dairy - Good Fats",
    "Butter": "Dairy - Good Fats",
    "Yogurt": "Dairy - Good Fats",
    # Bad Fats
    "Chips": "Packaged Snacks - Bad Fats",
    "Candy": "Packaged Snacks - Bad Fats",
    "Chocolate": "Packaged Snacks - Bad Fats",
    "Fried Chicken": "Prepared Meals - Bad Fats",
    "Ice Cream": "Frozen Foods - Bad Fats",
    "Soda": "Beverages - Bad Fats",
    "Pizza": "Prepared Meals - Bad Fats",
    "Burgers": "Prepared Meals - Bad Fats",
    "Cookies": "Packaged Snacks - Bad Fats",
    "Cakes": "Packaged Snacks - Bad Fats",
    # Neutral or Other
    "Bread": "Bakery - Neutral",
    "Pasta Dishes": "Prepared Meals - Neutral",
    "Soup": "Canned Foods - Neutral",
    "Vegetables": "Natural Produce - Neutral",
    "Fruits": "Natural Produce - Neutral",
}

# Map categories to broader groups
df['Category_Grouped'] = df['Category'].map(category_mapping).fillna("Other")

# Aggregate data by grouped categories for better interpretation
try:
    aggregated_data = df.groupby('Category_Grouped')['Fat'].mean().reset_index()

    # Sort data for better visualization
    aggregated_data = aggregated_data.sort_values(by='Fat', ascending=False)

    # Plotting the average fat content for each grouped category
    plt.figure(figsize=(16, 20))  # Increased height for better clarity
    sns.barplot(data=aggregated_data, x='Fat', y='Category_Grouped', palette='coolwarm')
    plt.title("Average Fat Content by Food Category Group")
    plt.xlabel("Average Fat Content (grams)")
    plt.ylabel("Food Category Group")
    plt.tight_layout()
    plt.savefig(os.path.join(visuals_path, "average_fat_by_category_group_expanded.png"))
    plt.close()
    print("Visualization saved: average_fat_by_category_group_expanded.png")
except Exception as e:
    print(f"Error generating visualization: {e}")

print("\nEDA Completed. Visualizations saved in the 'visuals' folder.")