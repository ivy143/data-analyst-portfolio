import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="F1 Analytics Dashboard", layout="wide")

# Title
st.title("🏎️ Formula 1 Performance Analytics Dashboard")

# Load data
df = pd.read_csv("bahrain_2025_results.csv")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Overview", "Driver Analysis", "Team Analysis"],
        icons=["speedometer2", "person", "flag"],
        menu_icon="cast",
        default_index=0
    )

# ======================
# OVERVIEW PAGE
# ======================
if selected == "Overview":

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Drivers", df["FullName"].nunique())
    col2.metric("Total Teams", df["TeamName"].nunique())
    col3.metric("Total Points", int(df["Points"].sum()))

    st.divider()

    st.subheader("Driver Championship Points")

    driver_points = df.groupby("FullName")["Points"].sum().reset_index()

    fig = px.bar(
        driver_points,
        x="FullName",
        y="Points",
        color="Points",
        title="Driver Points Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================
# DRIVER ANALYSIS
# ======================
if selected == "Driver Analysis":

    driver = st.selectbox(
        "Select Driver",
        df["FullName"].unique()
    )

    driver_data = df[df["FullName"] == driver]

    st.subheader(f"Performance of {driver}")

    fig = px.bar(
        driver_data,
        x="TeamName",
        y="Points",
        color="Points",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================
# TEAM ANALYSIS
# ======================
if selected == "Team Analysis":

    st.subheader("Team Performance")

    team_points = df.groupby("TeamName")["Points"].sum().reset_index()

    fig = px.pie(
        team_points,
        names="TeamName",
        values="Points",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================
# DATASET VIEW
# ======================
st.divider()
st.subheader("Dataset Preview")
st.dataframe(df)
st.header("🏎️ Lap Time Telemetry Analysis")

# simulate lap data
import numpy as np

laps = list(range(1, 51))
lap_times = np.random.normal(92, 1.5, 50)

lap_df = pd.DataFrame({
    "Lap": laps,
    "LapTime": lap_times
})

fig = px.line(
    lap_df,
    x="Lap",
    y="LapTime",
    title="Lap Time Performance",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
st.header("🔧 Pit Stop Strategy")

pit_data = pd.DataFrame({
    "Driver": ["Driver A","Driver B","Driver C"],
    "PitStopTime": [2.3,2.8,2.5]
})

fig = px.bar(
    pit_data,
    x="Driver",
    y="PitStopTime",
    title="Pit Stop Time Comparison",
    template="plotly_dark",
    color="PitStopTime"
)

st.plotly_chart(fig, use_container_width=True)
st.header("⚔️ Driver vs Driver Comparison")

drivers = df["FullName"].unique()

driver1 = st.selectbox("Driver 1", drivers)
driver2 = st.selectbox("Driver 2", drivers, index=1)

compare_df = df[df["FullName"].isin([driver1, driver2])]

fig = px.bar(
    compare_df,
    x="FullName",
    y="Points",
    color="FullName",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
import time

st.header("📡 Live Race Simulation")

live_data = st.empty()

for i in range(5):
    lap = np.random.randint(1,50)
    speed = np.random.randint(280,340)

    live_data.metric("Current Lap", lap)
    live_data.metric("Speed km/h", speed)

    time.sleep(1)
    import fastf1
import fastf1.plotting

st.header("🏎️ Real F1 Race Data")

year = st.selectbox("Select Year", [2023, 2024])
race = st.text_input("Race Name", "Bahrain")

try:
    session = fastf1.get_session(year, race, "R")
    session.load()

    laps = session.laps

    lap_times = laps.groupby("Driver")["LapTime"].mean().reset_index()

    lap_times["LapTimeSeconds"] = lap_times["LapTime"].dt.total_seconds()

    fig = px.bar(
        lap_times,
        x="Driver",
        y="LapTimeSeconds",
        color="LapTimeSeconds",
        title="Average Lap Time by Driver",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

except:
    st.warning("Race data could not be loaded.")
    import fastf1
import matplotlib.pyplot as plt

st.header("🗺️ Track Map Visualization")

year = 2023
race = "Bahrain"

session = fastf1.get_session(year, race, 'Q')
session.load()

driver = st.selectbox("Select Driver for Track Map", session.drivers)

lap = session.laps.pick_driver(driver).pick_fastest()

pos = lap.get_pos_data()

fig, ax = plt.subplots()

ax.plot(pos['X'], pos['Y'], color="red")

ax.set_title("Track Map Racing Line")
ax.axis('off')

st.pyplot(fig)
st.header("🛞 Tyre Strategy Analysis")

laps = session.laps

tyre_data = laps.groupby(["Driver","Compound"]).size().reset_index(name="Laps")

fig = px.bar(
    tyre_data,
    x="Driver",
    y="Laps",
    color="Compound",
    title="Tyre Usage by Driver",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
st.header("⏱️ Sector Time Analysis")

sector_data = session.laps[["Driver","Sector1Time","Sector2Time","Sector3Time"]]

sector_data = sector_data.dropna()

sector_data["Sector1"] = sector_data["Sector1Time"].dt.total_seconds()
sector_data["Sector2"] = sector_data["Sector2Time"].dt.total_seconds()
sector_data["Sector3"] = sector_data["Sector3Time"].dt.total_seconds()

sector_avg = sector_data.groupby("Driver")[["Sector1","Sector2","Sector3"]].mean().reset_index()

fig = px.bar(
    sector_avg,
    x="Driver",
    y=["Sector1","Sector2","Sector3"],
    title="Average Sector Times",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
st.header("⚡ Fastest Lap")

fastest_lap = session.laps.pick_fastest()

st.metric(
    label="Fastest Driver",
    value=fastest_lap["Driver"]
)

st.metric(
    label="Lap Time",
    value=str(fastest_lap["LapTime"])
)
st.header("🏁 Race Position Animation")

laps = session.laps

position_data = laps[["LapNumber","Driver","Position"]].dropna()

fig = px.line(
    position_data,
    x="LapNumber",
    y="Position",
    color="Driver",
    title="Race Position Progression",
    template="plotly_dark"
)

fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)
st.header("🚀 Overtake Detection")

overtakes = position_data.sort_values(["Driver","LapNumber"])

overtakes["PositionChange"] = overtakes.groupby("Driver")["Position"].diff()

overtake_events = overtakes[overtakes["PositionChange"] < 0]

st.write("Detected Overtakes")

st.dataframe(overtake_events[["LapNumber","Driver","Position"]])
st.header("🔥 Driver Speed Heatmap")

driver = st.selectbox("Select Driver for Speed Analysis", session.drivers)

lap = session.laps.pick_driver(driver).pick_fastest()

car_data = lap.get_car_data().add_distance()

speed_data = car_data[["Distance","Speed"]]

fig = px.scatter(
    speed_data,
    x="Distance",
    y="Speed",
    color="Speed",
    title="Speed vs Distance",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
st.header("🔧 Pit Stop Timeline")

pit_laps = session.laps[session.laps["PitInTime"].notna()]

pit_data = pit_laps[["Driver","LapNumber"]]

fig = px.scatter(
    pit_data,
    x="LapNumber",
    y="Driver",
    title="Pit Stop Timeline",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
