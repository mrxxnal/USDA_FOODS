import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure 'assets' folder exists
os.makedirs('assets', exist_ok=True)

# Load the dataset
df = pd.read_csv('data/raw_data.csv')

# Set a modern theme for plots
sns.set_theme(style='whitegrid', palette='muted')

# 🎯 1. Visualize Missing Data (Improved Visualization)
plt.figure(figsize=(10, 6))

# Count missing values per column
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]

# Bar plot for missing values
sns.barplot(x=missing_values.index, y=missing_values.values, palette='magma')
plt.title('Missing Values by Feature', fontsize=14, fontweight='bold')
plt.xlabel('Features')
plt.ylabel('Number of Missing Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('assets/missing_data_example.jpeg')
plt.show()

# 🎯 2. Visualize Duplicate Rows (Improved Visualization)
duplicates = df[df.duplicated()]
print("\nExamples of Duplicate Rows:")
print(duplicates.head(3))

plt.figure(figsize=(8, 2))
plt.table(cellText=duplicates.head(3).values, colLabels=duplicates.columns, cellLoc='center', loc='center')
plt.axis('off')
plt.title('Examples of Duplicate Data', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('assets/duplicates_example.jpeg')
plt.show()

# 🎯 3. Violin & Strip Plot for Outliers (Enhanced Visualization)
numerical_data = df.select_dtypes(include=[np.number])
Q1 = numerical_data.quantile(0.25)
Q3 = numerical_data.quantile(0.75)
IQR = Q3 - Q1

# Identify all outliers without downsizing
outliers = numerical_data[((numerical_data < (Q1 - 1.5 * IQR)) | 
                           (numerical_data > (Q3 + 1.5 * IQR))).any(axis=1)]
print("\nExamples of Outliers:")
print(outliers.head(3))

plt.figure(figsize=(12, 6))

# Violin plot with strip plot for outliers
melted_outliers = outliers.melt(var_name='Feature', value_name='Value')
sns.violinplot(x='Feature', y='Value', data=melted_outliers, palette='Set3', inner='box')
sns.stripplot(x='Feature', y='Value', data=melted_outliers, color='k', alpha=0.6, size=3, jitter=True)

plt.title('Violin & Strip Plot for Outliers', fontsize=14, fontweight='bold')
plt.xlabel('Features')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('assets/outliers_example.jpeg')
plt.show()

# 🎯 4. Combine All Examples into One Image
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Missing data example
sns.barplot(x=missing_values.index, y=missing_values.values, palette='magma', ax=axes[0])
axes[0].set_title('Missing Values by Feature', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Features')
axes[0].set_ylabel('Number of Missing Values')
axes[0].tick_params(axis='x', rotation=45)

# Duplicates example as a table
axes[1].axis('off')
table = plt.table(cellText=duplicates.head(3).values, colLabels=duplicates.columns, cellLoc='center', loc='center', ax=axes[1])
table.scale(1, 1.5)
axes[1].set_title('Examples of Duplicate Data', fontsize=12, fontweight='bold')

# Violin & Strip plot for outliers
sns.violinplot(x='Feature', y='Value', data=melted_outliers, palette='Set3', inner='box', ax=axes[2])
sns.stripplot(x='Feature', y='Value', data=melted_outliers, color='k', alpha=0.6, size=3, jitter=True, ax=axes[2])
axes[2].set_title('Violin & Strip Plot for Outliers', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Features')
axes[2].set_ylabel('Values')
axes[2].tick_params(axis='x', rotation=45)