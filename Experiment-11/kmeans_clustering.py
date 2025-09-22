import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file_path = "/content/sample_data/california_housing_train.csv"
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

X = df[["median_income", "median_house_value"]] 

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

df["Cluster"] = kmeans.labels_

print("\nCluster Centroids (scaled space):")
print(kmeans.cluster_centers_)

plt.figure(figsize=(8,6))
sns.scatterplot(
    x=X["median_income"], 
    y=X["median_house_value"], 
    hue=df["Cluster"], 
    palette="Set1",
    s=50
)
plt.title("K-Means Clustering: Income vs House Value")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(
    centroids[:, 0], centroids[:, 1], 
    s=300, c="yellow", marker="X", edgecolor="black", label="Centroids"
)
plt.legend()
plt.show()

print("\n K-Means clustering experiment complete!")
