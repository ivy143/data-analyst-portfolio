import pandas as pd

# Create IPL fake dataset
data = [
    [1, 2023, "MI", "CSK", "CSK", "Mumbai", "Ravindra Jadeja", 180, 6, "2023-04-01"],
    [2, 2023, "RCB", "KKR", "RCB", "Bangalore", "Virat Kohli", 200, 5, "2023-04-02"],
    [3, 2023, "DC", "SRH", "SRH", "Delhi", "Bhuvneshwar Kumar", 150, 8, "2023-04-03"],
    [4, 2023, "GT", "RR", "GT", "Ahmedabad", "Shubman Gill", 210, 4, "2023-04-04"],
    [5, 2023, "PBKS", "LSG", "LSG", "Mohali", "KL Rahul", 175, 7, "2023-04-05"],
    [6, 2023, "CSK", "RCB", "CSK", "Chennai", "MS Dhoni", 190, 6, "2023-04-06"],
    [7, 2023, "MI", "GT", "MI", "Mumbai", "Suryakumar Yadav", 205, 5, "2023-04-07"],
    [8, 2023, "KKR", "RR", "RR", "Kolkata", "Jos Buttler", 198, 6, "2023-04-08"],
    [9, 2023, "SRH", "PBKS", "PBKS", "Hyderabad", "Shikhar Dhawan", 160, 9, "2023-04-09"],
    [10, 2023, "LSG", "DC", "DC", "Lucknow", "David Warner", 170, 8, "2023-04-10"],
    [11, 2024, "MI", "CSK", "MI", "Mumbai", "Rohit Sharma", 220, 3, "2024-04-01"],
    [12, 2024, "RCB", "RR", "RR", "Bangalore", "Sanju Samson", 185, 7, "2024-04-02"],
    [13, 2024, "GT", "SRH", "SRH", "Ahmedabad", "Travis Head", 195, 6, "2024-04-03"],
    [14, 2024, "PBKS", "DC", "DC", "Mohali", "Rishabh Pant", 165, 8, "2024-04-04"],
    [15, 2024, "LSG", "KKR", "KKR", "Lucknow", "Andre Russell", 210, 4, "2024-04-05"],
    [16, 2024, "CSK", "GT", "GT", "Chennai", "Rashid Khan", 175, 7, "2024-04-06"],
    [17, 2024, "RR", "MI", "RR", "Jaipur", "Yashasvi Jaiswal", 200, 5, "2024-04-07"],
    [18, 2024, "SRH", "RCB", "RCB", "Hyderabad", "Faf du Plessis", 190, 6, "2024-04-08"],
    [19, 2024, "DC", "CSK", "CSK", "Delhi", "Devon Conway", 180, 6, "2024-04-09"],
    [20, 2024, "KKR", "PBKS", "KKR", "Kolkata", "Nitish Rana", 170, 8, "2024-04-10"],
    [21, 2024, "MI", "LSG", "LSG", "Mumbai", "Marcus Stoinis", 175, 7, "2024-04-11"],
    [22, 2024, "RR", "SRH", "SRH", "Jaipur", "Pat Cummins", 205, 5, "2024-04-12"],
    [23, 2024, "RCB", "GT", "GT", "Bangalore", "Hardik Pandya", 210, 4, "2024-04-13"],
    [24, 2024, "CSK", "PBKS", "CSK", "Chennai", "Deepak Chahar", 160, 9, "2024-04-14"],
    [25, 2024, "DC", "MI", "MI", "Delhi", "Jasprit Bumrah", 190, 6, "2024-04-15"]
]

columns = [
    "match_id", "season", "team1", "team2", "winner",
    "venue", "player_of_match", "total_runs", "wickets", "match_date"
]

df = pd.DataFrame(data, columns=columns)

# Convert match_date to datetime
df["match_date"] = pd.to_datetime(df["match_date"])

# Save to CSV
df.to_csv("ipl_fake_dataset.csv", index=False)

print("IPL Fake Dataset Created Successfully ✅")
print(df.head())
df = pd.read_csv("ipl_fake_dataset.csv")
df.info()
df.describe()
df["match_date"] = pd.to_datetime(df["match_date"])
df.info()
#EDA
#overview of the dataset
print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)
#check missing values
print(df.isnull().sum())
#team winning analysis
winning_counts = df["winner"].value_counts()
print(winning_counts)
print(df["winner"].value_counts(normalize=True) * 100)
#highest scoring matches
print(df.sort_values(by="total_runs", ascending=False).head())
#matches per season
print(df["season"].value_counts().sort_index())
print(df["winner"].value_counts())
#visulization
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="winner", order=df["winner"].value_counts().index)
plt.xticks(rotation=45)
plt.title("Match Wins by Team")
plt.show()
#average total runs per season
avg_runs_season = df.groupby("season")["total_runs"].mean()
print(avg_runs_season)
season_runs = df.groupby("season")["total_runs"].mean()

plt.figure(figsize=(8,5))
season_runs.plot(kind="bar")
plt.title("Average Total Runs Per Season")
plt.ylabel("Average Runs")
plt.show()
#kpis
total_matches = df.shape[0]
total_seasons = df["season"].nunique()
total_teams = pd.concat([df["team1"], df["team2"]]).nunique()
highest_score = df["total_runs"].max()

print("Total Matches:", total_matches)
print("Total Seasons:", total_seasons)
print("Total Teams:", total_teams)
print("Highest Match Score:", highest_score)
#top performing teams
wins = df["winner"].value_counts()
print(wins)
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
wins.plot(kind="bar")
plt.title("Total Wins by Team")
plt.ylabel("Number of Wins")
plt.show()
# toss imapact analysis
toss_win_match_win = df[df["toss_winner"] == df["winner"]]
impact_percentage = (toss_win_match_win.shape[0] / df.shape[0]) * 100

print("Toss Impact Percentage:", impact_percentage)
#run distribution
plt.figure(figsize=(8,5))
plt.hist(df["total_runs"], bins=10)
plt.title("Distribution of Total Match Runs")
plt.xlabel("Total Runs")
plt.ylabel("Frequency")
plt.show()
#season growth trend
season_trend = df.groupby("season")["total_runs"].mean()

plt.figure(figsize=(8,5))
season_trend.plot()
plt.title("Average Runs Trend by Season")
plt.ylabel("Average Runs")
plt.show()
#venue analysis
venue_matches = df["venue"].value_counts()
print(venue_matches)
