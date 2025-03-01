import pandas as pd
import matplotlib.pyplot as plt

# Define the comparison data
data = {
    "Clustering Method": ["K-Means", "Hierarchical Clustering", "DBSCAN"],
    "Concept": [
        "Partitions data into k clusters by minimizing variance within clusters.",
        "Builds a nested hierarchy of clusters by merging or splitting groups based on distance.",
        "Groups points based on density, marking outliers as noise."
    ],
    "Advantages": [
        "✔️ Efficient for large datasets.\n✔️ Works well for well-separated clusters.\n✔️ Computationally fast.",
        "✔️ No need to specify k.\n✔️ Produces dendrograms for visualization.\n✔️ Captures hierarchical relationships.",
        "✔️ Automatically determines clusters.\n✔️ Detects arbitrary-shaped clusters.\n✔️ Identifies outliers."
    ],
    "Limitations": [
        "❌ Assumes spherical clusters.\n❌ Sensitive to outliers.\n❌ Requires specifying k.",
        "❌ Computationally expensive for large datasets.\n❌ Can be sensitive to minor data variations.\n❌ Difficult to scale.",
        "❌ Requires careful tuning of epsilon & minPts.\n❌ Struggles with varying densities.\n❌ May classify dense noise as clusters."
    ],
    "Best Use Cases": [
        "📌 When clusters are compact and well-separated.\n📌 When a fast and scalable solution is needed.",
        "📌 When understanding relationships between clusters is important.\n📌 Works well for small datasets.",
        "📌 When outlier detection is needed.\n📌 When clusters have irregular shapes.\n📌 When the number of clusters is unknown."
    ]
}

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

# Save as an HTML table
df.to_html("clustering_comparison.html", index=False)

# Save as CSV
df.to_csv("clustering_comparison.csv", index=False)

# Display DataFrame in Jupyter Notebook (if using Jupyter)
display(df)

# Save as an image
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis("off")
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center')

# Adjust font size
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0, 1, 2, 3, 4])

# Save the table as an image
plt.savefig("visuals/clustering_comparison_table.png", bbox_inches='tight', dpi=300)
plt.show()
