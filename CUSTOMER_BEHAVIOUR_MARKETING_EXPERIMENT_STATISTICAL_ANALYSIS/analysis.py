import pandas as pd

df = pd.read_csv("customer_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# STATISTICAL ANALYSIS

print("\nMEAN VALUES")
print(df.mean(numeric_only=True))

print("\nMEDIAN VALUES")
print(df.median(numeric_only=True))

print("\nMODE VALUES")
print(df.mode(numeric_only=True))


#DISTRIBUTION ANALYSIS
import matplotlib.pyplot as plt
import seaborn as sns

print("\nCreating distribution plots...")

sns.histplot(df["age"], bins=20)
plt.title("Age Distribution")
plt.show()

sns.histplot(df["income"], bins=20)
plt.title("Income Distribution")
plt.show()

sns.histplot(df["spending_score"], bins=20)
plt.title("Spending Score Distribution")
plt.show()

#correlation analysis
print("\nCORRELATION MATRIX")

correlation = df.corr(numeric_only=True)

print(correlation)
plt.figure(figsize=(10,6))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()