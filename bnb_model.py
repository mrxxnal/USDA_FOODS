import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("✅ Bernoulli Naive Bayes Execution Started...")

# Create visuals dir if missing
os.makedirs("visuals", exist_ok=True)
os.makedirs("data", exist_ok=True)  # ensure data dir exists for saving results

# Load BNB binary features and labels (labels same as GNB)
X_train = pd.read_csv("data/nb_BNB_X_train.csv")
X_test = pd.read_csv("data/nb_BNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

# Fit model
model = BernoulliNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Accuracy and report
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\n✅ BNB Accuracy: {acc:.4f}")
print("\n📋 Classification Report:\n", report)

# Save accuracy + report to file
with open("data/bnb_accuracy.txt", "w") as f:
    f.write(f"Bernoulli Naive Bayes Accuracy: {acc*100:.2f}%\n\n")
    f.write(report)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# Top 10 actual categories
top10 = y_test.value_counts().head(10).index.tolist()
filtered_labels = [cat for cat in top10 if cat in model.classes_]
indices = [list(model.classes_).index(cat) for cat in filtered_labels]
cm_top = cm[np.ix_(indices, indices)]

# Normalize for better richness
cm_top_normalized = cm_top.astype("float") / cm_top.sum(axis=1, keepdims=True)

# Plot
plt.figure(figsize=(12, 9))
sns.heatmap(cm_top_normalized, annot=True, fmt=".2f", cmap="PuBuGn",
            xticklabels=filtered_labels, yticklabels=filtered_labels, cbar_kws={'label': 'Proportion'})
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.title("Bernoulli Naive Bayes Confusion Matrix (Top 10 Normalized)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save
plt.savefig("visuals/BNB_confusion_matrix_top10.png")
print("🖼️ Saved ➜ visuals/BNB_confusion_matrix_top10.png")

print("✅ BNB Modeling Complete.")