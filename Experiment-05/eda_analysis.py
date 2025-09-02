import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/content/sample_data/california_housing_test.csv"

# Load dataset
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

print("\n Summary Statistics:")
print(df.describe(include="all"))

print("\n Correlation Matrix:")
corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

df.hist(bins=30, figsize=(12, 10))
plt.suptitle("Feature Distributions", fontsize=16)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x="median_income", y="median_house_value", data=df, alpha=0.5)
plt.title("Median Income vs Median House Value")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="housing_median_age", y="median_house_value", data=df)
plt.title("Housing Age vs House Value")
plt.xticks(rotation=90)
plt.show()
