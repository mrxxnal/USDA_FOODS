import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("✅ Multinomial Naive Bayes Execution Started...")

# 🔹 Ensure visuals and data directories exist
os.makedirs("visuals", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 🔹 Load MNB-specific features (integer-like)
X_train = pd.read_csv("data/nb_MNB_X_train.csv")
X_test = pd.read_csv("data/nb_MNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

# 🔹 Train the MNB model
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 🔹 Accuracy and Classification Report
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\n✅ MNB Accuracy: {acc:.4f}")
print("\n📋 Classification Report:\n", report)

# 🔹 Save accuracy report to data folder
with open("data/mnb_accuracy.txt", "w") as f:
    f.write(f"Multinomial Naive Bayes Accuracy: {acc*100:.2f}%\n\n")
    f.write(report)

# 🔹 Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# 🔹 Get top 10 most frequent actual categories in test set
top10 = y_test.value_counts().head(10).index.tolist()
filtered_labels = [label for label in top10 if label in model.classes_]
indices = [list(model.classes_).index(label) for label in filtered_labels]
cm_top = cm[np.ix_(indices, indices)]

# 🔹 Normalize the confusion matrix
cm_top_normalized = cm_top.astype("float") / cm_top.sum(axis=1, keepdims=True)

# 🔹 Plot Confusion Matrix
plt.figure(figsize=(12, 9))
sns.heatmap(cm_top_normalized, annot=True, fmt=".2f", cmap="YlOrBr",
            xticklabels=filtered_labels, yticklabels=filtered_labels, cbar_kws={'label': 'Proportion'})
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.title("Multinomial Naive Bayes Confusion Matrix (Top 10 Normalized)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 🔹 Save Plot
plt.savefig("visuals/MNB_confusion_matrix_top10_rich.png")
print("🖼️ Saved Rich Confusion Matrix ➜ visuals/MNB_confusion_matrix_top10_rich.png")

print("✅ MNB Modeling Complete.")