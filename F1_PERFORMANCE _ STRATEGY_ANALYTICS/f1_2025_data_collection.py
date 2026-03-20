import os
import fastf1
import pandas as pd
import numpy as np


cache_dir = 'cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(cache_dir)

print(f"cache directory: {os.path.abspath(cache_dir)}")
# Load race session
session = fastf1.get_session(2025, "Bahrain", "R")

# Download session data
session.load()
# Get race results
results = session.results

# Display results
print(results)
# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save dataset
results_df.to_csv("bahrain_2025_results.csv", index=False)

print("Dataset saved successfully!")

# Show column names
print(results_df.columns)


clean_results = results_df[[
    "FullName",
    "TeamName",
    "GridPosition",
    "Position",
    "Points",
    "Laps",
    "Status"
]].copy()

# Show first 20 rows clearly
print(clean_results.to_string())
# Create Position Gain column using .loc to avoid warnings
clean_results.loc[:, "PositionGain"] = clean_results["GridPosition"] - clean_results["Position"]

print(clean_results.to_string())
import matplotlib.pyplot as plt

# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(clean_results["FullName"], clean_results["PositionGain"])

# Labels
plt.xlabel("Driver")
plt.ylabel("Position Gain")
plt.title("Driver Position Gain - Bahrain 2025")

# Rotate names for readability
plt.xticks(rotation=90)

# Show plot
plt.show()

# Get official race schedule
schedule = fastf1.get_event_schedule(2025)

print(schedule)
all_race_results = []
season_results = pd.DataFrame()

for _, event in schedule.iterrows():

    if event['EventFormat'] == 'conventional':  # skip testing events
        race_name = event['EventName']
        round_number = event['RoundNumber']

        try:
            print("Loading:", race_name)

            session = fastf1.get_session(2025, round_number, "R")
            session.load()

            race_results = session.results.copy()
            race_df = pd.DataFrame(race_results)

            race_df["RaceName"] = race_name
            race_df["Round"] = round_number

            all_race_results.append(race_df)

        except Exception as e:
            print("Error loading", race_name, e)
            # continue to next event without stopping
            continue

# combine after looping through schedule
if all_race_results:
    season_results = pd.concat(all_race_results, ignore_index=True)
else:
    print("No race results were collected.")

# Show output in requested format
output_df = season_results[["Round","RaceName","FullName","Position"]].copy()
output_df.rename(columns={"FullName": "Driver"}, inplace=True)
print(output_df.head(30).to_string(index=False))
# Save full season dataset
season_results.to_csv("f1_2025_full_season_results.csv", index=False)

print("Full season dataset saved successfully!")