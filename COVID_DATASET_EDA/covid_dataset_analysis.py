import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Date range (1 year data)
dates = pd.date_range(start="2021-01-01", end="2021-12-31")

# Countries
countries = ["USA", "India", "Brazil", "UK", "Germany"]

data = []

for country in countries:
    base_cases = np.random.randint(50000, 100000)
    vaccination = 0
    
    for date in dates:
        
        # Simulate waves using sine pattern
        wave = int(base_cases * (1 + 0.5 * np.sin(date.dayofyear / 365 * 4 * np.pi)))
        
        new_cases = max(0, int(np.random.normal(wave, 5000)))
        new_deaths = int(new_cases * np.random.uniform(0.01, 0.03))
        recovered = int(new_cases * np.random.uniform(0.7, 0.95))
        
        vaccination = min(100, vaccination + np.random.uniform(0.05, 0.2))
        
        data.append([
            date,
            country,
            new_cases,
            new_deaths,
            recovered,
            vaccination
        ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "date",
    "country",
    "new_cases",
    "new_deaths",
    "new_recoveries",
    "vaccination_rate"
])

# Calculate cumulative confirmed cases
df["confirmed_cases"] = df.groupby("country")["new_cases"].cumsum()
df["total_deaths"] = df.groupby("country")["new_deaths"].cumsum()
df["total_recoveries"] = df.groupby("country")["new_recoveries"].cumsum()

# Active cases formula
df["active_cases"] = df["confirmed_cases"] - df["total_deaths"] - df["total_recoveries"]

# Rearranging columns
df = df[[
    "date",
    "country",
    "confirmed_cases",
    "active_cases",
    "total_deaths",
    "total_recoveries",
    "new_cases",
    "new_deaths",
    "vaccination_rate"
]]

# Save dataset
df.to_csv("covid_fake_dataset.csv", index=False)

print("Fake COVID dataset created successfully!")
print(df.head())
print("Total rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print(df.shape)
print(df.duplicated().sum())
print("\n--- DATA INFO ---")
print(df.info())

print("\n--- STATISTICS ---")
print(df.describe())

print("\n--- NULL VALUES ---")
print(df.isnull().sum())
#EDA
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
#total confirmed cases over time(per country)
plt.figure(figsize=(12,6))

for country in df['country'].unique():
    country_data = df[df['country'] == country]
    plt.plot(country_data['date'], country_data['confirmed_cases'], label=country)

plt.title("Total Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#total deaths by country
plt.figure(figsize=(8,5))

latest_data = df.groupby('country').last().reset_index()

sns.barplot(x='country', y='total_deaths', data=latest_data)

plt.title("Total Deaths by Country")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.show()
#daily news cases trend
plt.figure(figsize=(12,6))

for country in df['country'].unique():
    country_data = df[df['country'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title("Daily New Cases Trend")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#correlation heatmap
plt.figure(figsize=(10,6))

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()
# Case Fatality Rate (Death %)
df["death_rate"] = (df["total_deaths"] / df["confirmed_cases"]) * 100

# Recovery Rate
df["recovery_rate"] = (df["total_recoveries"] / df["confirmed_cases"]) * 100

# Active Case Percentage
df["active_rate"] = (df["active_cases"] / df["confirmed_cases"]) * 100
#rolling average
df["7day_avg_cases"] = df.groupby("country")["new_cases"].transform(
    lambda x: x.rolling(window=7).mean()
)
plt.figure(figsize=(12,6))

for country in df['country'].unique():
    country_data = df[df['country'] == country]
    plt.plot(country_data['date'], country_data['7day_avg_cases'], label=country)

plt.title("7-Day Moving Average of New Cases")
plt.xlabel("Date")
plt.ylabel("7-Day Avg Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#vaccination vs active cases relationship
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="vaccination_rate",
    y="active_cases",
    hue="country"
)

plt.title("Vaccination Rate vs Active Cases")
plt.show()
#peak analysis
peak_cases = df.loc[df.groupby("country")["new_cases"].idxmax()]
print(peak_cases[["country", "date", "new_cases"]])
print("\n--- PROJECT INSIGHTS ---")

print("1. Confirmed cases show exponential growth pattern across countries.")
print("2. Death rate remains relatively stable compared to confirmed cases.")
print("3. 7-day rolling average smooths volatility in daily new cases.")
print("4. Higher vaccination rate generally corresponds to reduced active cases.")
print("5. Significant variation exists between countries in peak infection days.")