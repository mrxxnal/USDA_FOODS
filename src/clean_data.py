import pandas as pd

# Load raw data
raw_data = pd.read_csv("data/raw_data.csv")

# Drop unnecessary columns and handle missing values
cleaned_data = raw_data.dropna()

# Save cleaned data
cleaned_data.to_csv("data/cleaned_data.csv", index=False)
print("Data cleaned and saved to data/cleaned_data.csv")