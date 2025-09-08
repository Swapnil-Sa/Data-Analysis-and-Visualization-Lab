
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# File path
file_path = "/content/sample_data/california_housing_test.csv"

# Load dataset
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully!")

plt.figure(figsize=(10, 6))
sns.boxplot(x="housing_median_age", y="median_house_value", data=df)
plt.title("Boxplot of Median House Value by Housing Median Age")
plt.xticks(rotation=90)
plt.savefig("boxplot.png")
plt.show()
print("Boxplot saved as boxplot.png")

# -------------------------------
# Violin Plot: Median Income vs. Median House Value
# -------------------------------
plt.figure(figsize=(10, 6))
sns.violinplot(x="housing_median_age", y="median_income", data=df, inner="quartile", palette="muted")
plt.title("Violin Plot of Median Income by Housing Median Age")
plt.xticks(rotation=90)
plt.savefig("violinplot.png")
plt.show()
print(" Violin Plot saved as violinplot.png")

print("\nSeaborn visualizations created, saved, and displayed successfully!")
