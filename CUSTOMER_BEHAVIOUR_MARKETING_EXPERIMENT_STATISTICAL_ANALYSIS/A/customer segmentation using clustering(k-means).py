import pandas as pd
import os
from sklearn.cluster import KMeans

# load dataset relative to script location
script_dir = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.normpath(os.path.join(script_dir, '..', 'customer_data.csv'))
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    raise FileNotFoundError(f"customer_data.csv not found at {csv_path}. Adjust path if necessary.")

# ensure necessary columns exist
required = ['age','income','spending_score']
missing = [c for c in required if c not in df.columns]
if missing:
    raise KeyError(f"Missing required columns for clustering: {missing}")

features = df[['age','income','spending_score']]
kmeans = KMeans(n_clusters=3, random_state=42)

df['customer_segment'] = kmeans.fit_predict(features)
print(df['customer_segment'].value_counts())
segment_analysis = df.groupby('customer_segment')[['age','income','spending_score']].mean()

print(segment_analysis)
import matplotlib.pyplot as plt

plt.scatter(df['income'], df['spending_score'], c=df['customer_segment'])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.show()