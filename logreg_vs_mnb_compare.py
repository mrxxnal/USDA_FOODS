import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load preprocessed data
X_train = pd.read_csv('data/logreg_X_train.csv')
X_test = pd.read_csv('data/logreg_X_test.csv')
y_train = pd.read_csv('data/logreg_y_train.csv').squeeze()
y_test = pd.read_csv('data/logreg_y_test.csv').squeeze()

# Ensure folders exist
os.makedirs("visuals", exist_ok=True)
os.makedirs("data", exist_ok=True)  # NEW: ensure 'data' folder exists for saving reports

# -------------------------------------
# 🔍 Evaluation Function with Save Option
# -------------------------------------
def evaluate_model(name, y_true, y_pred, img_filename, txt_filename):
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, digits=4)
    acc = accuracy_score(y_true, y_pred)

    # Print
    print(f"\n🔎 Evaluation for {name}")
    print("Confusion Matrix:\n", cm)
    print("\nClassification Report:\n", report)
    print(f"Accuracy: {acc:.4f}")

    # Save Confusion Matrix as Image
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join("visuals", img_filename))
    plt.close()
    print(f"📁 Saved confusion matrix to visuals/{img_filename}")

    # NEW: Save metrics as text
    with open(os.path.join("data", txt_filename), "w") as f:
        f.write(f"🔎 {name} Evaluation\n\n")
        f.write("Confusion Matrix:\n")
        f.write(str(cm) + "\n\n")
        f.write("Classification Report:\n")
        f.write(report + "\n")
        f.write(f"Accuracy: {acc:.4f}\n")
    print(f"📄 Saved report to data/{txt_filename}")

# -------------------------------------
# 🔹 Logistic Regression
# -------------------------------------
logreg_model = LogisticRegression(max_iter=1000)
logreg_model.fit(X_train, y_train)
y_pred_logreg = logreg_model.predict(X_test)
evaluate_model("Logistic Regression", y_test, y_pred_logreg, "logreg_confusion.png", "logreg_report.txt")

# -------------------------------------
# 🔹 Multinomial Naive Bayes
# -------------------------------------
X_train_mnb = X_train - X_train.min()
X_test_mnb = X_test - X_train.min()

mnb_model = MultinomialNB()
mnb_model.fit(X_train_mnb, y_train)
y_pred_mnb = mnb_model.predict(X_test_mnb)
evaluate_model("Multinomial Naive Bayes", y_test, y_pred_mnb, "mnb_confusion.png", "mnb_report.txt")