import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv("data/cleaned_data.csv")

# Example visualization
sns.barplot(x="description", y="calories", data=data.head(10))
plt.title("Calories in Ultra-Processed Foods")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/calories_plot.png")
print("Visualization saved to visuals/calories_plot.png")