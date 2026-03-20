import pandas as pd
# Load CSV file 
rfm = pd.read_csv("customer segmentation.csv")

print("First 5 Rows:")
print(rfm.head())

print("\nData Info:")
print(rfm.info())

print("\nNull Values:")
print(rfm.isnull().sum())



from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Select only RFM columns
rfm_features = rfm[['recency', 'frequency', 'monetary']]

# Scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)

# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print("Cluster added successfully!")
print(rfm.head())


import matplotlib.pyplot as plt

plt.figure()

plt.scatter(
    rfm['frequency'],
    rfm['monetary'],
    c=rfm['Cluster']  # color by cluster
)

plt.xlabel("Frequency")
plt.ylabel("Monetary")
plt.title("Customer Segments (K-Means Clusters)")

plt.colorbar(label="Cluster")
plt.show()



plt.figure()

scatter = plt.scatter(
    rfm['frequency'],
    rfm['monetary'],
    c=rfm['Cluster']
)

plt.xlabel("Frequency")
plt.ylabel("Monetary")
plt.title("Customer Segments")

plt.colorbar(scatter)
plt.show()


