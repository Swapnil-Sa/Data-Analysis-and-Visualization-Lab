import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "/content/sample_data/california_housing_train.csv"
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

median_value = df["median_house_value"].median()
df["price_category"] = (df["median_house_value"] > median_value).astype(int)

print("\n Target Conversion Done:")
print(df["price_category"].value_counts())

X = df.drop(["median_house_value", "price_category"], axis=1)
y = df["price_category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel Evaluation")
print("Accuracy:", round(acc, 4))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Low Price", "High Price"], yticklabels=["Low Price", "High Price"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Logistic Regression")
plt.show()

