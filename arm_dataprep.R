# Load necessary libraries
library(dplyr)         # Data manipulation
library(tidyr)         # Data transformation
library(arules)        # Association Rule Mining
library(readr)         # Reading CSV files

# 1️⃣ Load Raw Data
raw_data <- read_csv("data/raw_data.csv")

# 2️⃣ Select Relevant Columns (Remove Numerical & Brand Data)
arm_data <- raw_data %>%
  select(Description, Category, Calories, Protein, Fat, Carbs)  # Keep only relevant columns

# 3️⃣ Handle Missing Values Properly
arm_data <- arm_data %>%
  mutate(
    Calories = ifelse(is.na(Calories), 0, Calories),   # Replace NA in numeric columns with 0
    Protein  = ifelse(is.na(Protein), 0, Protein),
    Fat      = ifelse(is.na(Fat), 0, Fat),
    Carbs    = ifelse(is.na(Carbs), 0, Carbs),
    Category = ifelse(is.na(Category), "Unknown", Category) # Replace NA in categorical with "Unknown"
  )

# 4️⃣ Transform Numerical Attributes into Categories
arm_data <- arm_data %>%
  mutate(
    Calories = case_when(
      Calories == 0 ~ "Zero-Calorie",
      Calories <= 50 ~ "Low-Calorie",
      Calories <= 100 ~ "Medium-Calorie",
      Calories > 100 ~ "High-Calorie"
    ),
    Protein = case_when(
      Protein == 0 ~ "No-Protein",
      Protein < 2 ~ "Low-Protein",
      Protein >= 2 ~ "High-Protein"
    ),
    Fat = case_when(
      Fat == 0 ~ "No-Fat",
      Fat < 2 ~ "Low-Fat",
      Fat >= 2 ~ "High-Fat"
    ),
    Carbs = case_when(
      Carbs == 0 ~ "No-Carbs",
      Carbs < 10 ~ "Low-Carbs",
      Carbs >= 10 ~ "High-Carbs"
    )
  )

# 5️⃣ Convert to Transaction Format (Items Instead of Columns)
arm_transactions <- arm_data %>%
  select(-Description) %>%   # Remove Description (only keep categorical features)
  apply(1, function(x) paste(x, collapse = ","))  # Merge values as transaction items

# 6️⃣ **Remove Duplicates**
arm_transactions <- unique(arm_transactions)

# 7️⃣ Save the Preprocessed Data for ARM
writeLines(arm_transactions, "data/arm_prepared_data.csv")

# ✅ Print Success Message
print("✅ ARM Data Prepared and Duplicates Removed: Saved as data/arm_prepared_data.csv")