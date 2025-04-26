import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

# 📂 Create folders if they don't exist
os.makedirs("reports", exist_ok=True)
os.makedirs("visuals", exist_ok=True)

# 📥 Load data
X_train = pd.read_csv("data/rf_X_train.csv")
X_test = pd.read_csv("data/rf_X_test.csv")
y_train = pd.read_csv("data/rf_y_train.csv").squeeze()
y_test = pd.read_csv("data/rf_y_test.csv").squeeze()

# 🧠 Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 🔍 Predict and evaluate
y_pred = rf_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=["Ice Cream", "Pizza", "Milk"])
cm = confusion_matrix(y_test, y_pred)

# 📝 Save report
with open("reports/rf_report.txt", "w") as f:
    f.write(f"Random Forest Accuracy: {acc:.4f}\n\n")
    f.write("Classification Report:\n")
    f.write(report)

# 📊 Confusion matrix plot
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Purples", xticklabels=["Ice Cream", "Pizza", "Milk"], yticklabels=["Ice Cream", "Pizza", "Milk"])
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title(f"Random Forest Confusion Matrix | Accuracy = {acc:.2%}")
plt.tight_layout()
plt.savefig("visuals/rf_conf_matrix.png")
plt.close()

# 🌟 Feature Importance Plot
importances = rf_model.feature_importances_
feature_names = X_train.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x="Importance", y="Feature", data=importance_df.head(10), palette="mako")
plt.title("Top 10 Feature Importances - Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig("visuals/rf_feature_importances.png")
plt.close()

print("✅ Random Forest training complete. Report, confusion matrix, and feature importance plot saved.")