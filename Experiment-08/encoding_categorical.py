import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "House_ID": [1, 2, 3, 4, 5],
    "Location": ["New York", "California", "Texas", "California", "Texas"],
    "Type": ["Apartment", "Villa", "Apartment", "Villa", "Studio"]
}

df = pd.DataFrame(data)
print(" Original Dataset:\n", df)


le = LabelEncoder()
df["Location_LabelEncoded"] = le.fit_transform(df["Location"])
df["Type_LabelEncoded"] = le.fit_transform(df["Type"])
print("\n After Label Encoding:\n", df)


df_onehot = pd.get_dummies(df, columns=["Location", "Type"])
print("\n After One-Hot Encoding:\n", df_onehot)

print("\n Encoding complete! Both Label Encoding and One-Hot Encoding applied.")

