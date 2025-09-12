import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = "/content/sample_data/california_housing_test.csv"

# Load dataset
df = pd.read_csv(file_path)
print(" Dataset Loaded Successfully!")

bar_data = df.groupby("housing_median_age")["median_house_value"].mean().head(10)
plt.figure(figsize=(8, 5))
bar_data.plot(kind="bar", color="skyblue")
plt.title("Average House Value by Housing Median Age (Top 10)")
plt.xlabel("Housing Median Age")
plt.ylabel("Average House Value")
plt.savefig("bar_chart.png")
plt.show()  
print(" Bar Chart Saved as bar_chart.png")


plt.figure(figsize=(8, 5))
plt.plot(df["median_income"].head(100), df["median_house_value"].head(100),
         marker="o", linestyle="-", color="green")
plt.title("Median Income vs. Median House Value")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.savefig("line_graph.png")
plt.show()   # 👈 Show chart
print(" Line Graph Saved as line_graph.png")

# Pie Chart
df["housing_median_age"].value_counts().head(6).plot.pie(
    autopct="%1.1f%%", startangle=90, figsize=(6,6))
plt.title("Distribution of Housing Median Age")
plt.savefig("pie_chart.png")
plt.show()

print("\nAll visualizations created, saved, and displayed successfully!")
