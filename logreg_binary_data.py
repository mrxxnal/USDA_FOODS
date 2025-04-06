import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load the clean normalized data
df = pd.read_csv('data/clean_normalized_data.csv')

# Step 2: Filter for 'Candy' and 'Cookies & Biscuits'
df_filtered = df[df['category'].isin(['Candy', 'Cookies & Biscuits'])].copy()

# Step 3: Map labels to binary (0 = Candy, 1 = Cookies & Biscuits)
df_filtered['label'] = df_filtered['category'].map({
    'Candy': 0,
    'Cookies & Biscuits': 1
})

# Step 4: Drop irrelevant columns
columns_to_drop = ['description', 'category', 'brand']
df_filtered.drop(columns=columns_to_drop, inplace=True)

# Step 5: Define features and labels
X = df_filtered.drop(columns=['label'])
y = df_filtered['label']

# Step 6: Train-test split (stratified to ensure class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 7: Save processed data for modeling
X_train.to_csv('data/logreg_X_train.csv', index=False)
X_test.to_csv('data/logreg_X_test.csv', index=False)
y_train.to_csv('data/logreg_y_train.csv', index=False)
y_test.to_csv('data/logreg_y_test.csv', index=False)

# Step 8: Confirm label distribution
print("✅ Logistic Regression data is cleaned, split, and saved successfully!")
print("📊 Label counts in y_train:\n", y_train.value_counts())
print("📊 Label counts in y_test:\n", y_test.value_counts())