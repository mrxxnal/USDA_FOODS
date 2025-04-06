import pandas as pd
import numpy as np
import os
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import KBinsDiscretizer
import seaborn as sns
import matplotlib.pyplot as plt

print("✅ CNB Execution Started...")

# Create visuals and data directories if not exist
os.makedirs("visuals", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Load original GNB train/test
X_train = pd.read_csv("data/nb_GNB_X_train.csv")
X_test = pd.read_csv("data/nb_GNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

# Discretize into 10 categorical bins
discretizer = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
X_train_cnb = discretizer.fit_transform(X_train)
X_test_cnb = discretizer.transform(X_test)

# Train CNB model
model = CategoricalNB()
model.fit(X_train_cnb, y_train)
y_pred = model.predict(X_test_cnb)

# Evaluate
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"✅ CNB Accuracy: {acc:.4f}")
print("\n📋 Classification Report:\n", report)

# Save to data folder
with open("data/cnb_accuracy.txt", "w") as f:
    f.write(f"Categorical Naive Bayes Accuracy: {acc*100:.2f}%\n\n")
    f.write(report)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
top10 = y_test.value_counts().head(10).index.tolist()
filtered_labels = [label for label in top10 if label in model.classes_]
indices = [list(model.classes_).index(label) for label in filtered_labels]
cm_top = cm[np.ix_(indices, indices)]
cm_top_norm = cm_top.astype("float") / cm_top.sum(axis=1, keepdims=True)

# Plot
plt.figure(figsize=(12, 9))
sns.heatmap(cm_top_norm, annot=True, fmt=".2f", cmap="crest",
            xticklabels=filtered_labels, yticklabels=filtered_labels,
            cbar_kws={'label': 'Proportion'})
plt.title("Categorical Naive Bayes Confusion Matrix (Top 10 Normalized)")
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("visuals/CNB_confusion_matrix_top10.png")
print("🖼️ Saved ➜ visuals/CNB_confusion_matrix_top10.png")

print("✅ CNB Modeling Complete.")