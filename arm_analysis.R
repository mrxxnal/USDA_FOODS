# Load necessary libraries
library(arules)        # For Association Rule Mining (Apriori Algorithm)
library(arulesViz)     # For Visualization
library(readr)         # For Reading CSV Files

# 1️⃣ Load Transaction Data
transactions <- read.transactions(
  "data/arm_prepared_data.csv", format = "basket", sep = ","
)

# 2️⃣ Apply Apriori Algorithm with Optimized Parameters
rules <- apriori(
  transactions,
  parameter = list(supp = 0.01, conf = 0.5, minlen = 2)
)

# 3️⃣ Sort and Extract Top 15 Rules for Each Metric
rules_sorted_support <- head(sort(rules, by = "support", decreasing = TRUE), 15)
rules_sorted_confidence <- head(sort(rules, by = "confidence", decreasing = TRUE), 15)
rules_sorted_lift <- head(sort(rules, by = "lift", decreasing = TRUE), 15)

# 4️⃣ Save Top 15 Rules for Each Metric
write(rules_sorted_support, file = "data/arm_top15_support.txt")
write(rules_sorted_confidence, file = "data/arm_top15_confidence.txt")
write(rules_sorted_lift, file = "data/arm_top15_lift.txt")

# 5️⃣ Export Rules for Future Analysis & Visualization
save(
  rules_sorted_support, 
  rules_sorted_confidence, 
  rules_sorted_lift, 
  file = "data/arm_rules.RData"
)

# ✅ Print Summary
message("✅ ARM Completed: Top 15 rules saved successfully!")