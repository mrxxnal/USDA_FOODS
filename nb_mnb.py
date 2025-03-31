print("✅ MNB Script Started...")

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 🔹 Load MNB-prepared data
X_train = pd.read_csv("data/nb_MNB_X_train.csv")
X_test = pd.read_csv("data/nb_MNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

print("📦 MNB data successfully loaded...")

# 🔹 Train Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)
print("🤖 MultinomialNB model trained.")

# 🔹 Predict
y_pred = model.predict(X_test)

# 🔹 Evaluation
acc = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {acc:.4f}")
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))

# 🔹 Confusion Matrix (Top 10 categories only)
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
top_classes = model.classes_[:10]  # Slice top 10
cm_top = cm[:10, :10]

# 🔹 Plot and Save
plt.figure(figsize=(12, 8))
sns.heatmap(cm_top, annot=True, fmt='d', cmap='YlGnBu',
            xticklabels=top_classes, yticklabels=top_classes)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Multinomial Naive Bayes Confusion Matrix (Top 10 Categories)")
plt.tight_layout()
plt.savefig("visuals/MNB_confusion_matrix.png")
print("🖼️ Confusion matrix saved to 'visuals/MNB_confusion_matrix.png'")

print("✅ MNB Script Completed.")