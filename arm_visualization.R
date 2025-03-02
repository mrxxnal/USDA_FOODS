# Load Required Libraries
library(arules)        # ARM Algorithm
library(arulesViz)     # Visualization
library(ggplot2)       # Enhanced visualizations
library(RColorBrewer)  # Color palettes
library(igraph)        # Network visualization
library(reshape2)      # Data transformation for heatmaps

# Define Output Directory
output_dir <- "visuals/"
if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}

# 1️⃣ Load Precomputed Transactions
transactions <- read.transactions("data/arm_prepared_data.csv", format = "basket", sep = ",")

# 2️⃣ Item Frequency Plot (Top 15 Frequent Items)
png(file = paste0(output_dir, "item_frequency_plot.png"), width = 1000, height = 700)
par(mar = c(5, 8, 4, 2))  # Adjust left margin to fit labels
itemFrequencyPlot(transactions, topN = 15, col = brewer.pal(9, "Set3"), 
                  main = "Top 15 Frequent Items", cex.names = 0.9, horiz = TRUE)
dev.off()

# 3️⃣ Load Precomputed ARM Rules
load("data/arm_rules.RData")  # Load the sorted rules

# 4️⃣ Scatter Plot: Support vs Confidence (Colored by Lift)
png(file = paste0(output_dir, "scatter_plot.png"), width = 1000, height = 700)
plot(rules_sorted_lift, measure = c("support", "confidence"), shading = "lift", 
     main = "Support vs Confidence (Shaded by Lift)")
dev.off()

# 5️⃣ Graph-Based Network Visualization of Top 10 Rules
png(file = paste0(output_dir, "network_plot.png"), width = 1000, height = 800)
plot(rules_sorted_lift[1:10], method = "graph", control = list(type = "items"), 
     main = "Association Rule Network (Top 10 Rules)")
dev.off()

# 6️⃣ Matrix Plot for Rule Visualization
png(file = paste0(output_dir, "matrix_plot.png"), width = 1000, height = 800)
plot(rules_sorted_support, method = "matrix", control = list(reorder = "measure"), 
     main = "Matrix Plot: Associations Between Items", col = terrain.colors(20))
dev.off()

# 7️⃣ Grouped Matrix Visualization
png(file = paste0(output_dir, "grouped_matrix.png"), width = 1200, height = 900)
plot(rules_sorted_lift, method = "grouped", 
     main = "Grouped Matrix of Top Association Rules")
dev.off()

# 8️⃣ Bar Plot: Top 15 Rules by Support
png(file = paste0(output_dir, "bar_plot_support.png"), width = 1200, height = 800)
par(mar = c(10, 4, 4, 2))  # Extend bottom margin for label visibility
top_support <- sort(rules_sorted_support, decreasing = TRUE)[1:15]
barplot(sort(quality(top_support)$support, decreasing = TRUE), 
        names.arg = labels(lhs(top_support)), las = 2, col = brewer.pal(9, "Blues"),
        main = "Top 15 Rules by Support", cex.names = 0.9, ylim = c(0, max(quality(top_support)$support) * 1.2))
dev.off()

# 9️⃣ Bar Plot: Top 15 Rules by Confidence
png(file = paste0(output_dir, "bar_plot_confidence.png"), width = 1200, height = 800)
par(mar = c(10, 4, 4, 2))  # Extend bottom margin for label visibility
top_confidence <- sort(rules_sorted_confidence, decreasing = TRUE)[1:15]
barplot(sort(quality(top_confidence)$confidence, decreasing = TRUE), 
        names.arg = labels(lhs(top_confidence)), las = 2, col = brewer.pal(9, "Reds"),
        main = "Top 15 Rules by Confidence", cex.names = 0.9, ylim = c(0, max(quality(top_confidence)$confidence) * 1.2))
dev.off()

# 🔟 Bar Plot: Top 15 Rules by Lift
png(file = paste0(output_dir, "bar_plot_lift.png"), width = 1200, height = 800)
par(mar = c(10, 4, 4, 2))  # Extend bottom margin for label visibility
top_lift <- sort(rules_sorted_lift, decreasing = TRUE)[1:15]
barplot(sort(quality(top_lift)$lift, decreasing = TRUE), 
        names.arg = labels(lhs(top_lift)), las = 2, col = brewer.pal(9, "Purples"),
        main = "Top 15 Rules by Lift", cex.names = 0.9, ylim = c(0, max(quality(top_lift)$lift) * 1.2))
dev.off()

# ✅ Success Message
print("✅ All visualizations successfully generated in the 'visuals/' folder!")