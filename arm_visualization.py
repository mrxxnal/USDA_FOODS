import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_title("Association Rule Mining (ARM)", fontsize=22, fontweight='bold', pad=20)

# Key Concepts with Enhanced Formatting
concepts = [
    ("🛒 Support", "Frequency of an item in transactions\nHigher support means a common item", "lightblue"),
    ("📊 Confidence", "Probability of buying B when A is bought\nMeasures rule strength", "lightgreen"),
    ("📈 Lift", "Relationship between A and B\nLift >1 means a strong association", "lightyellow")
]

for i, (title, description, color) in enumerate(concepts):
    ax.text(-0.1, 1.1 - (i * 0.3), f"{title}:", fontsize=14, fontweight="bold", 
            bbox=dict(facecolor=color, edgecolor="black", boxstyle="round,pad=0.5"))
    ax.text(-0.1, 1.05 - (i * 0.3), description, fontsize=12, verticalalignment="top")

# Example Association Rules with a Structured List
ax.text(0.45, 1.05, "🔹 Example Rules:", fontsize=16, fontweight='bold', bbox=dict(facecolor="lightgray", alpha=0.8))
example_rules = [
    "✔️ {Milk, Bread} → {Butter}",
    "✔️ {Eggs, Flour} → {Cake}",
    "✔️ {Diapers} → {Beer}"
]

for i, rule in enumerate(example_rules):
    ax.text(0.45, 1.0 - (i * 0.1), rule, fontsize=14, color="black", bbox=dict(facecolor="white", edgecolor="black"))

# ARM Process Flow with Numbered Steps
ax.text(0.45, 0.55, "⚙️ Process of ARM:", fontsize=16, fontweight='bold', bbox=dict(facecolor="lightgray", alpha=0.8))
process_steps = [
    "1️⃣ Identify frequent itemsets",
    "2️⃣ Apply support threshold",
    "3️⃣ Generate association rules",
    "4️⃣ Evaluate using confidence & lift",
    "5️⃣ Filter strong rules for insights",
    "6️⃣ Apply results to recommendations"
]

for i, step in enumerate(process_steps):
    ax.text(0.45, 0.50 - (i * 0.08), step, fontsize=14, color="darkblue", bbox=dict(facecolor="white", edgecolor="black"))

# Hide axes for clean visualization
ax.axis("off")

# Save the improved image
plt.savefig("visuals/association_rule_mining_improved.png", bbox_inches="tight", dpi=300)
plt.show()