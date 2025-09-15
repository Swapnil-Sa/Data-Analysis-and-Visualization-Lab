
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# File path
file_path = "/content/sample_data/california_housing_train.csv"

# Load dataset
df = pd.read_csv(file_path)
print("✅ Dataset Loaded Successfully!")
print("Shape:", df.shape)
print(df.head())

X = df.drop("median_house_value", axis=1)  
y = df["median_house_value"]               

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\n Model Evaluation")

print("R² Score:", round(r2, 4))
print("Mean Squared Error:", round(mse, 2))

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\n Coefficients Interpretation:")
print(coefficients)

print("\n Linear Regression experiment complete!")
