import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Binarizer, MinMaxScaler

print("✅ Naive Bayes Data Prep Script Running...")

# Load cleaned, normalized dataset
df = pd.read_csv("data/clean_normalized_data.csv")

# Minimum 5 samples per class to increase diversity
class_counts = df["category"].value_counts()
valid_classes = class_counts[class_counts >= 5].index
df = df[df["category"].isin(valid_classes)]

print(f"🧾 Using {len(valid_classes)} categories (>=5 samples each).")
print(f"📊 Total Samples After Filtering: {df.shape[0]}")

# ✅ Keep additional columns for traceability
meta = df[["description", "brand", "category"]]

# ✅ Features and target
features = ["calories", "protein", "fat", "carbs", 
            "calories_per_protein", "calories_per_fat", "calories_per_carb"]
X = df[features]
y = df["category"]

# ✅ Stratified train-test split
X_train, X_test, y_train, y_test, meta_train, meta_test = train_test_split(
    X, y, meta, test_size=0.5, stratify=y, random_state=42
)

# ✅ Ensure folders exist
os.makedirs("data", exist_ok=True)

# ✅ Save GNB format (continuous)
X_train.to_csv("data/nb_GNB_X_train.csv", index=False)
X_test.to_csv("data/nb_GNB_X_test.csv", index=False)
y_train.reset_index(drop=True).to_csv("data/nb_GNB_y_train.csv", index=False)
y_test.reset_index(drop=True).to_csv("data/nb_GNB_y_test.csv", index=False)
meta_train.reset_index(drop=True).to_csv("data/nb_GNB_meta_train.csv", index=False)
meta_test.reset_index(drop=True).to_csv("data/nb_GNB_meta_test.csv", index=False)
print("🧠 GNB datasets saved.")

# ✅ Multinomial NB (positive integers)
scaler = MinMaxScaler()
X_train_mnb = pd.DataFrame(scaler.fit_transform(X_train), columns=features).round(2) * 100
X_test_mnb = pd.DataFrame(scaler.transform(X_test), columns=features).round(2) * 100
X_train_mnb.to_csv("data/nb_MNB_X_train.csv", index=False)
X_test_mnb.to_csv("data/nb_MNB_X_test.csv", index=False)
print("🔢 MNB datasets saved.")

# ✅ Bernoulli NB (binary values)
binarizer = Binarizer(threshold=0.0)
X_train_bnb = pd.DataFrame(binarizer.fit_transform(X_train), columns=features)
X_test_bnb = pd.DataFrame(binarizer.transform(X_test), columns=features)
X_train_bnb.to_csv("data/nb_BNB_X_train.csv", index=False)
X_test_bnb.to_csv("data/nb_BNB_X_test.csv", index=False)
print("⚫️ BNB datasets saved.")

# ✅ Summary
print("✅ Data prep complete.")
print(f"🔎 Final Train Size: {X_train.shape[0]} | Test Size: {X_test.shape[0]}")
print(f"🏷️ Categories: {len(y.unique())}")