# 🍭 Step 1: Filter clean_normalized_data.csv for Candy, Cereal, and Apples

import pandas as pd

# Load the full dataset
df = pd.read_csv("data/clean_normalized_data.csv")

# Define the categories you want to include
selected_categories = [
    "Ice Cream & Frozen Yogurt",
    "Pizza",
    "Milk"
]

# Filter the dataset to only include the selected categories
filtered_df = df[df['category'].isin(selected_categories)].copy()

# Assign numeric labels for classification
label_mapping = {
    "Ice Cream & Frozen Yogurt": 0,
    "Pizza": 1,
    "Milk": 2
}
filtered_df["label"] = filtered_df["category"].map(label_mapping)

# ✅ Save the filtered data
filtered_df.to_csv("data/rf_filtered_data.csv", index=False)

# 🔎 Display the number of items per class
print(filtered_df["label"].value_counts())

from sklearn.model_selection import train_test_split

# 🔹 Drop non-numeric/text columns
X = filtered_df.drop(columns=["description", "category", "brand", "label"])
y = filtered_df["label"]

# ✂️ Stratified split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 💾 Save the train-test splits
X_train.to_csv("data/rf_X_train.csv", index=False)
X_test.to_csv("data/rf_X_test.csv", index=False)
y_train.to_csv("data/rf_y_train.csv", index=False)
y_test.to_csv("data/rf_y_test.csv", index=False)

# ✅ Confirm shapes and class balance
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
print("Train label distribution:\n", y_train.value_counts())
print("Test label distribution:\n", y_test.value_counts())