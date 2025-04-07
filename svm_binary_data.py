import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

# ✅ Load normalized dataset
df = pd.read_csv("data/clean_normalized_data.csv")

# 🎯 Filter only Potato chips and Cookies and brownies
df['category'] = df.iloc[:, 1]
binary_df = df[df['category'].isin(['Potato chips', 'Cookies and brownies'])].copy()

# 🧠 Encode labels: Potato chips = 1, Cookies and brownies = 0
binary_df['label'] = binary_df['category'].map({'Potato chips': 1, 'Cookies and brownies': 0})

# 🧪 Drop non-feature columns: description, category, brand
X = binary_df.iloc[:, 3:-2]
y = binary_df['label']

# 🧼 Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 📦 Stratified Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, stratify=y, random_state=42
)

# 💾 Save datasets to data/
os.makedirs("data", exist_ok=True)
pd.DataFrame(X_train).to_csv("data/svm_X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("data/svm_X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("data/svm_y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("data/svm_y_test.csv", index=False)

print("✅ SVM binary data (Potato chips vs Cookies and brownies) saved to /data/")