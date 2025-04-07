import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ✅ Load SVM binary classification data
X_train = pd.read_csv("data/svm_X_train.csv")
X_test = pd.read_csv("data/svm_X_test.csv")
y_train = pd.read_csv("data/svm_y_train.csv").squeeze()
y_test = pd.read_csv("data/svm_y_test.csv").squeeze()

# 📁 Output folders
os.makedirs("visuals", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 📄 Master log file for terminal output
master_log_path = "data/svm_terminal_output.txt"
accuracies = []  # to track kernel, C, and accuracy

with open(master_log_path, "w") as master_log:

    # 📊 Kernels and costs to test
    kernels = ['linear', 'poly', 'rbf']
    C_values = [0.1, 1, 10]

    for kernel in kernels:
        for C in C_values:
            header = f"\n🔍 Training SVM with kernel='{kernel}', C={C}..."
            print(header)
            master_log.write(header + "\n")

            # 🧠 Train model
            model = SVC(kernel=kernel, C=C, gamma='scale')
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # 🎯 Evaluate
            acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred)

            # Log accuracy for visualization
            accuracies.append({
                "kernel": kernel,
                "C": C,
                "accuracy": acc
            })

            summary = f"✅ Accuracy: {acc:.4f}\nClassification Report:\n{report}"
            print(summary)
            master_log.write(summary + "\n")

            # 📝 Save individual report
            individual_report_path = f"reports/svm_{kernel}_C{C}_report.txt"
            with open(individual_report_path, "w") as f:
                f.write(f"SVM Kernel: {kernel}, C: {C}\n")
                f.write(f"Accuracy: {acc:.4f}\n\n")
                f.write(report)

            # 📊 Save confusion matrix
            plt.figure(figsize=(6, 4))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                        xticklabels=['Class 0', 'Class 1'],
                        yticklabels=['Class 0', 'Class 1'])
            plt.title(f"SVM ({kernel}) | C={C} | Acc={acc:.2%}")
            plt.xlabel("Predicted")
            plt.ylabel("True")
            plt.tight_layout()
            fig_path = f"visuals/svm_conf_matrix_{kernel}_C{C}.png"
            plt.savefig(fig_path)
            plt.close()

# 📈 Generate accuracy comparison bar chart
acc_df = pd.DataFrame(accuracies)
plt.figure(figsize=(10, 6))
sns.barplot(x="accuracy", y="kernel", hue="C", data=acc_df, palette="viridis")
plt.title("SVM Kernel Accuracy Comparison")
plt.xlabel("Accuracy")
plt.ylabel("Kernel")
plt.xlim(0, 1)
plt.tight_layout()
plt.savefig("visuals/svm_kernel_accuracy_comparison.png")
plt.close()