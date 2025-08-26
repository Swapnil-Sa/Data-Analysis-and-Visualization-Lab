
import pandas as pd

# File path to dataset
file_path = "/content/sample_data/california_housing_test.csv"

df = pd.read_csv(file_path)
print("✅ Dataset Loaded Successfully!")
print("Original Shape:", df.shape)

# Step 1: Check Missing Values

print("\n🔍 Checking Missing Values:")
print(df.isnull().sum())

# Step 2: Handle Missing Values

# Option 1: Fill missing values with median
df = df.fillna(df.median(numeric_only=True))

# Option 2: Drop rows with missing values

print("\n✅ Missing Values Handled (using median):")
print(df.isnull().sum())

# Step 3: Remove Duplicates

df = df.drop_duplicates()
print("\n✅ Duplicates Removed!")
print("New Shape:", df.shape)

# Step 4: Preview Cleaned Data

print("\n📌 Cleaned Dataset Preview:")
print(df.head())
