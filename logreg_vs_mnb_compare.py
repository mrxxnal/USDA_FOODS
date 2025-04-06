import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🚀 Load preprocessed data
X_train = pd.read_csv("data/logreg_X_train.csv")
X_test = pd.read_csv("data/logreg_X_test.csv")
y_train = pd.read_csv("data/logreg_y_train.csv").squeeze()
y_test = pd.read_csv("data/logreg_y_test.csv").squeeze()

# === Logistic Regression ===
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)
print(f"📈 Logistic Regression Accuracy: {acc_lr:.4f}")
print(classification_report(y_test, y_pred_lr))

# === Multinomial Naive Bayes ===
mnb_model = MultinomialNB()
mnb_model.fit(X_train, y_train)
y_pred_mnb = mnb_model.predict(X_test)
acc_mnb = accuracy_score(y_test, y_pred_mnb)
print(f"📊 Multinomial NB Accuracy: {acc_mnb:.4f}")
print(classification_report(y_test, y_pred_mnb))

# === Confusion Matrices ===
cm_lr = confusion_matrix(y_test, y_pred_lr)
cm_mnb = confusion_matrix(y_test, y_pred_mnb)

# ✅ Save confusion matrices
pd.DataFrame(cm_lr).to_csv("data/cm_logreg.csv", index=False)
pd.DataFrame(cm_mnb).to_csv("data/cm_mnb.csv", index=False)

# ✅ Save accuracies
with open("data/binary_logreg_accuracy.txt", "w") as f:
    f.write(f"{acc_lr:.4f}")

with open("data/binary_mnb_accuracy.txt", "w") as f:
    f.write(f"{acc_mnb:.4f}")

# 🎨 Visualization
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.heatmap(cm_lr, annot=True, fmt='d', cmap="Blues", xticklabels=["Cookies", "Candy"], yticklabels=["Cookies", "Candy"])
plt.title("Logistic Regression")
plt.xlabel("Predicted"); plt.ylabel("Actual")

plt.subplot(1, 2, 2)
sns.heatmap(cm_mnb, annot=True, fmt='d', cmap="Greens", xticklabels=["Cookies", "Candy"], yticklabels=["Cookies", "Candy"])
plt.title("Multinomial Naive Bayes")
plt.xlabel("Predicted"); plt.ylabel("Actual")

os.makedirs("visuals", exist_ok=True)
plt.tight_layout()
plt.savefig("visuals/logreg_vs_mnb_confusion.png")
plt.show()