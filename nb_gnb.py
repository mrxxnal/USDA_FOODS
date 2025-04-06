import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("✅ Gaussian Naive Bayes Execution Started...")

# 🔹 Ensure visuals and data directories exist
os.makedirs("visuals", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 🔹 Load training and testing data
X_train = pd.read_csv("data/nb_GNB_X_train.csv")
X_test = pd.read_csv("data/nb_GNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

# 🔹 Train the GNB model
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 🔹 Accuracy and Classification Report
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\n✅ GNB Accuracy: {acc:.4f}")
print("\n📋 Classification Report:\n", report)

# 🔹 Save accuracy report to data folder
with open("data/gnb_accuracy.txt", "w") as f:
    f.write(f"Gaussian Naive Bayes Accuracy: {acc*100:.2f}%\n\n")
    f.write(report)

# 🔹 Confusion Matrix - full
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# 🔹 Extract top 10 most frequent actual categories in test set
top10 = y_test.value_counts().head(10).index.tolist()
filtered_labels = [label for label in top10 if label in model.classes_]
indices = [list(model.classes_).index(label) for label in filtered_labels]
cm_top = cm[np.ix_(indices, indices)]

# 🔹 Normalize the top-10 confusion matrix (optional but adds richness)
cm_top_normalized = cm_top.astype("float") / cm_top.sum(axis=1, keepdims=True)

# 🔹 Plot Top-10 Confusion Matrix
plt.figure(figsize=(12, 9))
sns.heatmap(cm_top_normalized, annot=True, fmt=".2f", cmap="YlGnBu",
            xticklabels=filtered_labels, yticklabels=filtered_labels, cbar_kws={'label': 'Proportion'})
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.title("Gaussian Naive Bayes Confusion Matrix (Top 10 Normalized)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 🔹 Save plot
plt.savefig("visuals/GNB_confusion_matrix_top10_rich.png")
print("🖼️ Saved Rich Confusion Matrix ➜ visuals/GNB_confusion_matrix_top10_rich.png")

print("✅ GNB Modeling Complete.")