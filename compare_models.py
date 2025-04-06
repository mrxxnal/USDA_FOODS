import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB, CategoricalNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import KBinsDiscretizer, MinMaxScaler

print("🚀 Model Comparison Script Initiated...\n")

# === Load universal labels ===
y_train = pd.read_csv("data/nb_GNB_y_train.csv").squeeze()
y_test = pd.read_csv("data/nb_GNB_y_test.csv").squeeze()

# Dictionary to hold results
results = {}

# === Decision Tree ===
X_train_dt = pd.read_csv("data/nb_GNB_X_train.csv")
X_test_dt = pd.read_csv("data/nb_GNB_X_test.csv")

dt_model = DecisionTreeClassifier(max_depth=10, criterion='entropy', random_state=42)
dt_model.fit(X_train_dt, y_train)
y_pred_dt = dt_model.predict(X_test_dt)
acc_dt = accuracy_score(y_test, y_pred_dt)
results['Decision Tree'] = acc_dt
print("🌳 Decision Tree Accuracy:", f"{acc_dt:.4f}")
print(classification_report(y_test, y_pred_dt))

# === Gaussian NB ===
gnb_model = GaussianNB()
gnb_model.fit(X_train_dt, y_train)
y_pred_gnb = gnb_model.predict(X_test_dt)
acc_gnb = accuracy_score(y_test, y_pred_gnb)
results['Gaussian NB'] = acc_gnb
print("📈 Gaussian NB Accuracy:", f"{acc_gnb:.4f}")
print(classification_report(y_test, y_pred_gnb))

# === Multinomial NB ===
X_train_mnb = pd.read_csv("data/nb_MNB_X_train.csv")
X_test_mnb = pd.read_csv("data/nb_MNB_X_test.csv")

mnb_model = MultinomialNB()
mnb_model.fit(X_train_mnb, y_train)
y_pred_mnb = mnb_model.predict(X_test_mnb)
acc_mnb = accuracy_score(y_test, y_pred_mnb)
results['Multinomial NB'] = acc_mnb
print("📊 Multinomial NB Accuracy:", f"{acc_mnb:.4f}")
print(classification_report(y_test, y_pred_mnb))

# === Bernoulli NB ===
X_train_bnb = pd.read_csv("data/nb_BNB_X_train.csv")
X_test_bnb = pd.read_csv("data/nb_BNB_X_test.csv")

bnb_model = BernoulliNB()
bnb_model.fit(X_train_bnb, y_train)
y_pred_bnb = bnb_model.predict(X_test_bnb)
acc_bnb = accuracy_score(y_test, y_pred_bnb)
results['Bernoulli NB'] = acc_bnb
print("⚪ Bernoulli NB Accuracy:", f"{acc_bnb:.4f}")
print(classification_report(y_test, y_pred_bnb))

# === Categorical NB ===
discretizer = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
X_train_cnb = discretizer.fit_transform(X_train_dt)
X_test_cnb = discretizer.transform(X_test_dt)

cnb_model = CategoricalNB()
cnb_model.fit(X_train_cnb, y_train)
y_pred_cnb = cnb_model.predict(X_test_cnb)
acc_cnb = accuracy_score(y_test, y_pred_cnb)
results['Categorical NB'] = acc_cnb
print("🧩 Categorical NB Accuracy:", f"{acc_cnb:.4f}")
print(classification_report(y_test, y_pred_cnb))

# === Logistic Regression ===
scaler = MinMaxScaler()
X_train_log = scaler.fit_transform(X_train_dt)
X_test_log = scaler.transform(X_test_dt)

lr_model = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='multinomial')
lr_model.fit(X_train_log, y_train)
y_pred_lr = lr_model.predict(X_test_log)
acc_lr = accuracy_score(y_test, y_pred_lr)
results['Logistic Regression'] = acc_lr
print("📉 Logistic Regression Accuracy:", f"{acc_lr:.4f}")
print(classification_report(y_test, y_pred_lr))

# === Summary ===
print("\n📋 Final Model Accuracy Summary:")
for model_name, acc in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{model_name}: {acc:.4f}")

# 🔍 Identify best model
best_model = max(results, key=results.get)
print(f"\n✅ Best Performing Model: {best_model} with Accuracy: {results[best_model]:.2%}")