# decision_tree_modeling.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import numpy as np

from sklearn.tree import export_graphviz
import graphviz
import os

# ---------------------------- #
#           LOAD DATA         #
# ---------------------------- #
X_train = pd.read_csv("data/nb_MNB_X_train.csv")
X_test = pd.read_csv("data/nb_MNB_X_test.csv")
y_train = pd.read_csv("data/nb_GNB_y_train.csv")["category"]
y_test = pd.read_csv("data/nb_GNB_y_test.csv")["category"]

# ---------------------------- #
#      SIMPLIFIED BASELINE    #
# ---------------------------- #
clf_default = DecisionTreeClassifier(max_depth=3, min_samples_split=20, min_samples_leaf=10, random_state=42)
clf_default.fit(X_train, y_train)
y_pred_default = clf_default.predict(X_test)

# Accuracy and Evaluation
print("📊 Simplified Decision Tree Accuracy:", round(accuracy_score(y_test, y_pred_default) * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred_default))

# ---------------------------- #
#  INFORMATIVE CONFUSION MAT  #
# ---------------------------- #

# Encode class labels
le = LabelEncoder()
y_test_enc = le.fit_transform(y_test)
y_pred_enc = le.transform(y_pred_default)

# Compute confusion matrix
full_cm = confusion_matrix(y_test_enc, y_pred_enc)

# Identify most active 10 actual classes (with the most prediction activity)
row_sums = full_cm.sum(axis=1)
top10_actual_idx = np.argsort(row_sums)[::-1][:10]
top10_labels = le.inverse_transform(top10_actual_idx)

# Subset and normalize matrix
cm_top10 = full_cm[top10_actual_idx][:, top10_actual_idx]
cm_normalized = cm_top10.astype("float") / cm_top10.sum(axis=1, keepdims=True)

# Plot
plt.figure(figsize=(10, 8))
sns.heatmap(cm_normalized, annot=True, fmt=".2f", cmap="YlGnBu",
            xticklabels=top10_labels, yticklabels=top10_labels,
            linewidths=0.5, linecolor='gray', cbar_kws={'label': 'Normalized Proportion'})
plt.title("Normalized Confusion Matrix – Most Active 10 Classes")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("visuals/confusion_matrix_simplified_top10_active.png")
plt.show()

# ---------------------------- #
#   FILTER DATA TO TOP-10     #
# ---------------------------- #

# Filter both train and test data to match Top-10 active classes
top10_classes = list(top10_labels)
mask_train = y_train.isin(top10_classes)
mask_test = y_test.isin(top10_classes)

X_train_top10 = X_train[mask_train]
y_train_top10 = y_train[mask_train]
X_test_top10 = X_test[mask_test]
y_test_top10 = y_test[mask_test]

# ---------------------------- #
#     TREE MODEL VARIANTS     #
# ---------------------------- #

clf_var1 = DecisionTreeClassifier(max_depth=2, min_samples_split=30, random_state=42)
clf_var1.fit(X_train_top10, y_train_top10)

clf_var2 = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=15, random_state=42)
clf_var2.fit(X_train_top10, y_train_top10)

clf_var3 = DecisionTreeClassifier(max_features=2, max_depth=3, min_samples_leaf=12, random_state=42)
clf_var3.fit(X_train_top10, y_train_top10)

# ---------------------------- #
#        VISUALIZATION        #
# ---------------------------- #

def visualize_tree(model, title, filename):
    escaped_class_names = [c.replace("&", "&amp;") for c in sorted(model.classes_)]  # ✅ Fix here

    dot_data = export_graphviz(
        model,
        out_file=None,
        feature_names=X_train.columns,
        class_names=escaped_class_names,  # ✅ Use escaped names
        filled=True,
        rounded=True,
        special_characters=True,
        proportion=True,
        precision=2
    )

    graph = graphviz.Source(dot_data)
    output_path = f"visuals/{filename}"
    graph.format = "png"
    graph.render(output_path, cleanup=True)
    print(f"✅ Tree saved to {output_path}.png")

visualize_tree(clf_var1, "Simplified Tree – Variant 1 (max_depth=2)", "tree_variant1_simplified")
visualize_tree(clf_var2, "Simplified Tree – Variant 2 (entropy, min_leaf=15)", "tree_variant2_simplified")
visualize_tree(clf_var3, "Simplified Tree – Variant 3 (max_features=2)", "tree_variant3_simplified")