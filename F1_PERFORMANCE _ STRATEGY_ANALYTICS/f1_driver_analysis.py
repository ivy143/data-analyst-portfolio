import pandas as pd

# Load the dataset
df = pd.read_csv("f1_2025_full_season_results.csv")

# View first rows
print(df.head())
# Calculate average finishing position for each driver
avg_finish = df.groupby("FullName")["Position"].mean().reset_index()

# Rename column
avg_finish = avg_finish.rename(columns={"Position": "AverageFinishPosition"})

# Sort by best finishing position
avg_finish = avg_finish.sort_values(by="AverageFinishPosition")

print(avg_finish)
# Calculate total points per driver
driver_points = df.groupby("FullName")["Points"].sum().reset_index()

# Rename column for clarity
driver_points = driver_points.rename(columns={"Points": "TotalPoints"})

# Sort by highest points
driver_points = driver_points.sort_values(by="TotalPoints", ascending=False)

print(driver_points)

import matplotlib.pyplot as plt

# Create bar chart
plt.figure(figsize=(12,6))

plt.bar(driver_points["FullName"], driver_points["TotalPoints"])

# Labels and title
plt.xlabel("Driver")
plt.ylabel("Total Points")
plt.title("F1 2025 Championship Standings")

# Rotate driver names
plt.xticks(rotation=90)

# Show chart
plt.show()
import numpy as np

import numpy as np

# calculate consistency score (standard deviation of points per race)
consistency = df.groupby("FullName")["Points"].std().reset_index()

# rename column
consistency = consistency.rename(columns={"Points": "ConsistencyScore"})

# sort by most consistent (lowest score = most consistent)
consistency = consistency.sort_values("ConsistencyScore")

print(consistency)
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.bar(consistency["FullName"], consistency["ConsistencyScore"])

plt.xlabel("Driver")
plt.ylabel("Consistency Score")
plt.title("F1 Driver Consistency Score")

plt.xticks(rotation=90)

plt.show()

# driver performance index
# Average points per driver
avg_points = df.groupby("FullName")["Points"].mean().reset_index()
avg_points = avg_points.rename(columns={"Points": "AvgPoints"})

# Average finish position
avg_position = df.groupby("FullName")["Position"].mean().reset_index()
avg_position = avg_position.rename(columns={"Position": "AvgPosition"})

# Merge all metrics
performance = avg_points.merge(avg_position, on="FullName")
performance = performance.merge(consistency, on="FullName")

# Calculate Driver Performance Index
performance["DPI"] = (
    performance["AvgPoints"] * 0.5
    + (1 / performance["AvgPosition"]) * 20
    + (1 / (performance["ConsistencyScore"] + 1)) * 10
)

# Sort by best performance
performance = performance.sort_values(by="DPI", ascending=False)

print(performance)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.bar(performance["FullName"], performance["DPI"])

plt.xlabel("Driver")
plt.ylabel("Driver Performance Index")
plt.title("F1 Driver Performance Index")

plt.xticks(rotation=90)

plt.show()
# TEAM PERFORMANCE
# calculate total points per team
team_performance = df.groupby("TeamName")["Points"].sum().reset_index()

# rename column
team_performance = team_performance.rename(columns={"Points": "TotalTeamPoints"})

# sort by best team
team_performance = team_performance.sort_values(by="TotalTeamPoints", ascending=False)

print(team_performance)
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.bar(team_performance["TeamName"], team_performance["TotalTeamPoints"])

plt.xlabel("Team")
plt.ylabel("Total Points")
plt.title("F1 Team Performance Comparison")

plt.xticks(rotation=45)

plt.show()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# copy performance dataset
ml_data = performance.copy()

# fix missing values
ml_data = ml_data.fillna(0)

# features
X = ml_data[["AvgPoints", "AvgPosition", "ConsistencyScore"]]

# target
y = ml_data["DPI"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# prediction
ml_data["PredictedScore"] = model.predict(X)

# show top drivers
predicted_drivers = ml_data.sort_values(by="PredictedScore", ascending=False)

print(predicted_drivers[["FullName", "PredictedScore"]])
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.bar(predicted_drivers["FullName"], predicted_drivers["PredictedScore"])

plt.xticks(rotation=90)

plt.title("Predicted Top F1 Drivers")
plt.ylabel("Predicted Performance Score")

plt.show()