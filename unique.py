import pandas as pd

# Load the dataset
df = pd.read_csv("data/clean_normalized_data.csv")

# Extract and print unique values from the 'category' column
unique_categories = df.iloc[:, 1].unique()

print("🧾 Unique Categories in 'category' column:\n")
for i, cat in enumerate(unique_categories, 1):
    print(f"{i}. {cat}")